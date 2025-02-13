import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest
from google.analytics.data_v1beta.types import OrderBy
from google.analytics.data_v1beta.types import Filter
from google.analytics.data_v1beta.types import FilterExpression
from google.analytics.data_v1beta.types import FilterExpressionList
from google.auth.exceptions import DefaultCredentialsError
import logging
from datetime import datetime, timedelta
import os
import numpy as np

class geoprocessing:
    
    def help(self):
        
        print("\n1. pull_ga")
        print("   - Description: Pull in GA4 data for geo experiments.")
        print("   - Usage: pull_ga(credentials_file, property_id, start_date, country, metrics)")
        print("   - Example: pull_ga('GeoExperiment-31c5f5db2c39.json', '111111111', '2023-10-15', 'United Kingdom', ['totalUsers', 'newUsers'])")

        print("\n2. process_itv_analysis")
        print("   - Description: Processes region-level data for geo experiments by mapping ITV regions, grouping selected metrics, merging with media spend data, and saving the result.")
        print("   - Usage: process_itv_analysis(raw_df, itv_path, cities_path, media_spend_path, output_path, test_group, control_group, columns_to_aggregate, aggregator_list")
        print("   - Example: process_itv_analysis(df, 'itv_regional_mapping.csv', 'Geo_Mappings_with_Coordinates.xlsx', 'IMS.xlsx', 'itv_for_test_analysis_itvx.csv', ['West', 'Westcountry', 'Tyne Tees'], ['Central Scotland', 'North Scotland'], ['newUsers', 'transactions'], ['sum', 'sum']")
        
        print("\n3. process_city_analysis")
        print("   - Description: Processes city-level data for geo experiments by grouping selected metrics, merging with media spend data, and saving the result.")
        print("   - Usage: process_city_analysis(raw_data, spend_data, output_path, test_group, control_group, columns_to_aggregate, aggregator_list)")
        print("   - Example: process_city_analysis(df, spend, 'output.csv', ['Barnsley'], ['Aberdeen'], ['newUsers', 'transactions'], ['sum', 'mean'])")
                
    def pull_ga(self, credentials_file, property_id, start_date, country, metrics):
        """
        Pulls Google Analytics data using the BetaAnalyticsDataClient.

        Parameters:
        credentials_file (str): Path to the JSON credentials file.
        property_id (str): Google Analytics property ID.
        start_date (str): Start date in 'YYYY-MM-DD' format.
        country (str): Country to filter the data by.
        metrics (list): List of metrics to retrieve (e.g., ["totalUsers", "sessions"]).

        Returns:
        pd.DataFrame: A pandas DataFrame containing the fetched data.
        """
        try:
            end_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

            if not os.path.exists(credentials_file):
                raise FileNotFoundError(f"Credentials file '{credentials_file}' not found.")
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_file

            try:
                client = BetaAnalyticsDataClient()
            except DefaultCredentialsError as e:
                raise DefaultCredentialsError(
                    f"Failed to initialize Google Analytics client: {e}"
                )

            def format_report(request):
                response = client.run_report(request)
                # Row index
                row_index_names = [header.name for header in response.dimension_headers]
                row_header = []
                for i in range(len(row_index_names)):
                    row_header.append([row.dimension_values[i].value for row in response.rows])

                row_index_named = pd.MultiIndex.from_arrays(np.array(row_header), names=np.array(row_index_names))
                # Row flat data
                metric_names = [header.name for header in response.metric_headers]
                data_values = []
                for i in range(len(metric_names)):
                    data_values.append([row.metric_values[i].value for row in response.rows])

                output = pd.DataFrame(data=np.transpose(np.array(data_values, dtype='f')),
                                    index=row_index_named, columns=metric_names)
                return output

            all_dfs = []
            offset_value = 0
            batch_size = 100000  

            while True:
                metric_objects = [Metric(name=metric) for metric in metrics]

                request = RunReportRequest(
                    property='properties/' + property_id,
                    dimensions=[Dimension(name="date"), Dimension(name="city")],
                    metrics=metric_objects,
                    order_bys=[OrderBy(dimension={'dimension_name': 'date'}),
                            OrderBy(dimension={'dimension_name': 'city'})],
                    date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
                    limit=batch_size,
                    offset=offset_value,
                    dimension_filter=FilterExpression(
                        and_group=FilterExpressionList(
                            expressions=[
                                FilterExpression(
                                    filter=Filter(
                                        field_name="country",
                                        string_filter=Filter.StringFilter(value=country),
                                    )
                                ),
                            ]
                        )
                    )
                )

                df = format_report(request)
                if df.empty:
                    break 

                df = df.reset_index()
                df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
                all_dfs.append(df)
                offset_value += batch_size

            if not all_dfs:
                return pd.DataFrame() 

            final_df = pd.concat(all_dfs, ignore_index=True)
            return final_df

        except FileNotFoundError as e:
            logging.error(f"FileNotFoundError: {e}")
            raise
        except DefaultCredentialsError as e:
            logging.error(f"DefaultCredentialsError: {e}")
            raise
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise

    def process_itv_analysis(self, raw_df, itv_path, cities_path, media_spend_path, output_path, test_group, control_group, columns_to_aggregate, aggregator_list):
        """
        Process ITV analysis by mapping geos, grouping data, and merging with media spend.
        
        Parameters:
            raw_df (pd.DataFrame): Raw input data containing columns such as 'geo', plus any metrics to be aggregated.
            itv_path (str): Path to the ITV regional mapping CSV file.
            cities_path (str): Path to the Geo Mappings Excel file.
            media_spend_path (str): Path to the media spend Excel file.
            output_path (str): Path to save the final output CSV file.
            group1 (list): List of geo regions for group 1.
            group2 (list): List of geo regions for group 2.
            columns_to_aggregate (list): List of columns in `raw_df` that need aggregation.
            aggregator_list (list): List of aggregation operations (e.g. ["sum", "mean", ...]) for corresponding columns.
        
        Returns:
            pd.DataFrame: The final merged and aggregated DataFrame.
        """

        # -----------------------
        # 1. Load and preprocess data
        # -----------------------
        itv = pd.read_csv(itv_path).dropna(subset=['Latitude', 'Longitude'])
        cities = pd.read_excel(cities_path).dropna(subset=['Latitude', 'Longitude'])
        
        itv['geometry'] = itv.apply(lambda row: Point(row['Longitude'], row['Latitude']), axis=1)
        cities['geometry'] = cities.apply(lambda row: Point(row['Longitude'], row['Latitude']), axis=1)
        
        itv_gdf = gpd.GeoDataFrame(itv, geometry='geometry')
        cities_gdf = gpd.GeoDataFrame(cities, geometry='geometry')
        
        # -----------------------
        # 2. Perform spatial join to match geos
        # -----------------------
        joined_gdf = gpd.sjoin_nearest(
            itv_gdf,
            cities_gdf,
            how='inner',
            distance_col='distance'
        )
        matched_result = joined_gdf[['ITV Region', 'geo']].drop_duplicates(subset=['geo'])
        
        # Handle unmatched geos
        unmatched_geos = set(cities_gdf['geo']) - set(matched_result['geo'])
        unmatched_cities_gdf = cities_gdf[cities_gdf['geo'].isin(unmatched_geos)]
        
        nearest_unmatched_gdf = gpd.sjoin_nearest(
            unmatched_cities_gdf,
            itv_gdf,
            how='inner',
            distance_col='distance'
        )
        
        unmatched_geo_mapping = nearest_unmatched_gdf[['geo', 'ITV Region', 'Latitude_right', 'Longitude_right']]
        unmatched_geo_mapping.columns = ['geo', 'ITV Region', 'Nearest_Latitude', 'Nearest_Longitude']
        
        matched_result = pd.concat([matched_result, unmatched_geo_mapping[['geo', 'ITV Region']]])
        
        # -----------------------
        # 3. Merge with raw data
        # -----------------------
        merged_df = pd.merge(raw_df, matched_result, on='geo', how='left')
        
        # Remove rows where geo is "(not set)"
        merged_df = merged_df[merged_df["geo"] != "(not set)"]
        
        # Replace 'geo' column with 'ITV Region'
        # - We'll keep the "ITV Region" naming for clarity, but you can rename if you like.
        merged_df = merged_df.drop(columns=['geo'])
        merged_df = merged_df.rename(columns={'ITV Region': 'geo'})
        
        # -----------------------
        # 4. Group and aggregate
        # -----------------------
        # Build the dictionary for aggregation: {col1: agg1, col2: agg2, ...}
        aggregation_dict = dict(zip(columns_to_aggregate, aggregator_list))
        
        # Perform the groupby operation
        grouped_df = merged_df.groupby(['date', 'geo'], as_index=False).agg(aggregation_dict)
        
        # -----------------------
        # 5. Filter for test & control groups
        # -----------------------
        filtered_df = grouped_df[grouped_df['geo'].isin(test_group + control_group)].copy()
        
        assignment_map = {city: 1 for city in test_group}
        assignment_map.update({city: 2 for city in control_group})
        filtered_df['assignment'] = filtered_df['geo'].map(assignment_map)
        
        # -----------------------
        # 6. Merge with media spend
        # -----------------------
        media_spend_df = pd.read_excel(media_spend_path).rename(columns={'Cost': 'cost'})
        
        # Merge on date and geo
        analysis_df = pd.merge(
            filtered_df,
            media_spend_df,
            on=['date', 'geo'],
            how='left'
        )
        
        # Fill missing cost with 0
        analysis_df['cost'] = analysis_df['cost'].fillna(0)
        
        # -----------------------
        # 7. Save to CSV
        # -----------------------
        analysis_df.to_csv(output_path, index=False)
        
        return analysis_df    
    
    def process_city_analysis(self, raw_data, spend_data, output_path, test_group, control_group, columns_to_aggregate, aggregator_list):
        """
        Process city-level analysis by grouping data, applying custom aggregations, 
        and merging with spend data.

        Parameters:
            raw_data (str or pd.DataFrame):
                - Raw input data as a file path (CSV/XLSX) or a DataFrame.
                - Must contain 'date' and 'city' columns, plus any columns to be aggregated.
            spend_data (str or pd.DataFrame):
                - Spend data as a file path (CSV/XLSX) or a DataFrame.
                - Must contain 'date', 'geo', and 'cost' columns.
            output_path (str): 
                - Path to save the final output file (CSV or XLSX).
            group1 (list): 
                - List of city regions to be considered "Test Group" or "Group 1".
            group2 (list): 
                - List of city regions to be considered "Control Group" or "Group 2".
            columns_to_aggregate (list): 
                - List of columns to apply aggregation to, e.g. ['newUsers', 'transactions'].
            aggregator_list (list): 
                - List of corresponding aggregation functions, e.g. ['sum', 'mean'].
                - Must be the same length as columns_to_aggregate.

        Returns:
            pd.DataFrame: The final merged, aggregated DataFrame.
        """

        def read_file(data):
            """Helper function to handle file paths or return DataFrame directly."""
            if isinstance(data, pd.DataFrame):
                return data
            ext = os.path.splitext(data)[1].lower()
            if ext == '.csv':
                return pd.read_csv(data)
            elif ext in ['.xlsx', '.xls']:
                return pd.read_excel(data)
            else:
                raise ValueError("Unsupported file type. Please use a CSV or XLSX file.")

        def write_file(df, file_path):
            """Helper function to write DataFrame to CSV or XLSX files."""
            ext = os.path.splitext(file_path)[1].lower()
            if ext == '.csv':
                df.to_csv(file_path, index=False)
            elif ext in ['.xlsx', '.xls']:
                df.to_excel(file_path, index=False, engine='openpyxl')
            else:
                raise ValueError("Unsupported file type. Please use a CSV or XLSX file.")

        # -----------------------
        # 1. Read and validate data
        # -----------------------
        raw_df = read_file(raw_data)
        spend_df = read_file(spend_data)

        # Columns we minimally need in raw_df
        required_columns = {'date', 'city'}
        # Ensure the columns to aggregate are there
        required_columns = required_columns.union(set(columns_to_aggregate))
        missing_in_raw = required_columns - set(raw_df.columns)
        if missing_in_raw:
            raise ValueError(
                f"The raw data is missing the following required columns: {missing_in_raw}"
            )

        # Validate spend data
        spend_required_columns = {'date', 'geo', 'cost'}
        missing_in_spend = spend_required_columns - set(spend_df.columns)
        if missing_in_spend:
            raise ValueError(
                f"The spend data is missing the following required columns: {missing_in_spend}"
            )

        # -----------------------
        # 2. Clean and prepare spend data
        # -----------------------
        # Convert cost column to numeric after stripping currency symbols and commas
        spend_df['cost'] = (
            spend_df['cost']
            .replace('[^\\d.]', '', regex=True)
            .astype(float)
        )

        # -----------------------
        # 3. Prepare raw data
        # -----------------------
        # Rename 'city' to 'geo' for consistency
        raw_df = raw_df.rename(columns={'city': 'geo'})

        # Filter only the relevant geos
        filtered_df = raw_df[raw_df['geo'].isin(test_group + control_group)].copy()

        # -----------------------
        # 4. Group and aggregate
        # -----------------------
        # Create a dictionary of {col: agg_function}
        if len(columns_to_aggregate) != len(aggregator_list):
            raise ValueError(
                "columns_to_aggregate and aggregator_list must have the same length."
            )
        aggregation_dict = dict(zip(columns_to_aggregate, aggregator_list))

        # Perform groupby using the aggregator dictionary
        grouped_df = filtered_df.groupby(['date', 'geo'], as_index=False).agg(aggregation_dict)

        # -----------------------
        # 5. Map groups (Test vs. Control)
        # -----------------------
        assignment_map = {city: "Test Group" for city in test_group}
        assignment_map.update({city: "Control Group" for city in control_group})
        grouped_df['assignment'] = grouped_df['geo'].map(assignment_map)

        # -----------------------
        # 6. Merge with spend data
        # -----------------------
        merged_df = pd.merge(
            grouped_df,
            spend_df,  # has date, geo, cost
            on=['date', 'geo'],
            how='left'
        )

        # Fill missing cost with 0
        merged_df['cost'] = merged_df['cost'].fillna(0)

        # -----------------------
        # 7. Write out results
        # -----------------------
        write_file(merged_df, output_path)

        return merged_df