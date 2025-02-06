import pandas as pd
import os
from SAES.utils.statistical_checks import check_normality

def obtain_list_metrics(metrics: pd.DataFrame) -> pd.DataFrame:
    """
    Extracts a list of metric names from a given dataset.

    Args:
        metrics (pd.DataFrame): A path to a CSV file containing metrics or an existing DataFrame.

    Returns:
        pd.DataFrame: A NumPy array of metric names extracted from the "MetricName" column.

    Example:
        >>> from SAES.utils.csv_processor import obtain_list_metrics
        >>> 
        >>> # Metrics source
        >>> metrics = "metrics.csv"
        >>> 
        >>> metrics_list = obtain_list_metrics(metrics)
        >>> print(metrics_list)
        ['EP', 'HV', 'NHV', 'IGD+']
    """

    # Load the metrics DataFrame, either from a CSV file or as an existing DataFrame
    df_m = pd.read_csv(metrics, delimiter=",") if isinstance(metrics, str) else metrics

    return df_m["MetricName"].tolist()

def obtain_list_instances(data: pd.DataFrame) -> pd.DataFrame:
    """
    Extracts a list of instance names from a given dataset.

    Args:
        data (pd.DataFrame): A path to a CSV file containing data or an existing DataFrame.

    Returns:
        pd.DataFrame: A NumPy array of instance names extracted from the "Instance" column.

    Example:
        >>> from SAES.utils.csv_processor import obtain_list_instances
        >>> 
        >>> # Data source
        >>> experimentData = "experimentData.csv"
        >>> 
        >>> instances_list = obtain_list_instances(data)
        >>> print(instances_list)
        ['ZCAT1','ZCAT2',...,'ZCAT20']
    """

    # Load the data DataFrame, either from a CSV file or as an existing DataFrame
    df = pd.read_csv(data, delimiter=",") if isinstance(data, str) else data

    return df["Instance"].unique().tolist()

def process_csv(data: str | pd.DataFrame, metrics: str | pd.DataFrame) -> dict:
    """
    Processes two CSV or DataFrame inputs: one containing metrics information and the other containing data.
    This function loads the metrics and data, and then filters the data based on the metric names,
    storing the filtered data along with a flag indicating whether to maximize the metric.
    
    Args:
        data (str | pd.DataFrame): 
            Path to a CSV file or an existing DataFrame containing data.
            
        metrics (str | pd.DataFrame): 
            Path to a CSV file or an existing DataFrame containing metrics information.
    
    Returns:
        dict: A dictionary containing the filtered data and the 'Maximize' flag for each metric.

    Example:
        >>> from SAES.utils.csv_processor import process_csv
        >>> 
        >>> # Data source
        >>> experimentData = "experimentData.csv"
        >>> 
        >>> # Metrics source
        >>> metrics = "metrics.csv"
        >>> 
        >>> data = process_csv(experimentData, metrics)
    """

    # Load the metrics DataFrame, either from a CSV file or as an existing DataFrame
    df_m = pd.read_csv(metrics, delimiter=",") if isinstance(metrics, str) else metrics

    # Load the data DataFrame, either from a CSV file or as an existing DataFrame
    df = pd.read_csv(data, delimiter=",") if isinstance(data, str) else data

    # Initialize an empty dictionary to store the filtered data and the 'Maximize' flag
    data = {}

    # Iterate through each row in the metrics DataFrame
    for _, row in df_m.iterrows():
        # Extract the metric name and the 'Maximize' flag (whether to maximize the metric)
        metric = row["MetricName"]
        maximize = row["Maximize"]

        # Filter the data for the rows where the 'Metric' matches the current metric
        df_n = df[df["MetricName"] == metric].reset_index()

        # Store the filtered data and the 'Maximize' flag in a dictionary
        data[metric] = (df_n, maximize)

    return data

def process_csv_metrics(data: str | pd.DataFrame, metrics: str | pd.DataFrame, metric: str) -> tuple:
    """
    Processes the given CSV data and metrics to extract and return the data for a specific metric.
    
    Args:
        data (str | pd.DataFrame): 
            Path to CSV file or a DataFrame containing data.

        metrics (str | pd.DataFrame): 
            Path to CSV file or a DataFrame containing metric information.

        metric (str):
            The specific metric to extract from the data.
    
    Returns:
        pd.DataFrame: 
            A filtered DataFrame containing data for the specified metric.
        
        bool: 
            Whether the metric should be maximized (True) or minimized (False).
    
    Raises:
        ValueError: If the specified metric is not found in the metrics DataFrame.

    Example:
        >>> from SAES.utils.csv_processor import process_csv_metrics
        >>> 
        >>> # Data source
        >>> experimentData = "experimentData.csv"
        >>> 
        >>> # Metrics source
        >>> metrics = "metrics.csv"
        >>> 
        >>> # metric
        >>> metric = "HV"
        >>> 
        >>> df_n, maximize = process_csv_metrics(experimentData, metrics, metric)
    """

    # Load the metrics DataFrame, either from a CSV file or as an existing DataFrame
    df_m = pd.read_csv(metrics, delimiter=",") if isinstance(metrics, str) else metrics

    # Load the data DataFrame, either from a CSV file or as an existing DataFrame
    df = pd.read_csv(data, delimiter=",") if isinstance(data, str) else data

    try:
        # Retrieve the maximize flag (True/False) for the specified metric
        maximize = df_m[df_m["MetricName"] == metric]["Maximize"].values[0]

        # Filter the data DataFrame for the rows matching the specified metric
        df_n = df[df["MetricName"] == metric].reset_index()

        # Return the filtered data and the maximize flag
        return df_n, maximize
    except Exception as e:
        raise ValueError(f"Metric '{metric}' not found in the metrics DataFrame.") from e

def process_dataframe_basic(data: str | pd.DataFrame, metric: str, metrics: str | pd.DataFrame = None, output_path: str = None) -> tuple:
    """
    Saves a DataFrame as a CSV file in a 'CSVs' directory.

    Args:
        data (pd.DataFrame): 
            The input DataFrame containing 'Instance', 'Algorithm', and 'MetricValue' columns.
    
        metric (str): 
            The metric name to be included in the saved filenames.
    
        metrics (pd.DataFrame):
            A DataFrame containing metrics information.

        output_path (str):
            The path to save the CSV file. Defaults None.

    Returns:
        pd.DataFrame:
            The input DataFrame.

        bool
            The maximize flag for the specified metric.

    Example:
        >>> from SAES.utils.csv_processor import process_dataframe_basic
        >>> 
        >>> # Data source
        >>> experimentData = "experimentData.csv"
        >>> 
        >>> # metric
        >>> metric = "HV"
        >>> 
        >>> df, maximize = process_dataframe_basic(data, metric)
    """
    
    # Load the data DataFrame, either from a CSV file or as an existing DataFrame
    df = pd.read_csv(data, delimiter=",") if isinstance(data, str) else data
    df = df[df["MetricName"] == metric]

    if metrics is not None:
        # Load the metrics DataFrame, either from a CSV file or as an existing DataFrame
        df_m = pd.read_csv(metrics, delimiter=",") if isinstance(metrics, str) else metrics

        # Retrieve the maximize flag (True/False) for the specified metric
        maximize = df_m[df_m["MetricName"] == metric]["Maximize"].values[0]
    else:
        maximize = None
    
    output_dir = output_path if output_path else os.getcwd()

    # Check if the input & output directories exist, if not create them
    os.makedirs(os.path.join(output_dir, "CSVs"), exist_ok=True)

    # Save the data to a CSV file
    df.to_csv(os.path.join(output_dir, "CSVs", f"data_{metric}.csv"), index=False)

    return df, maximize

def process_dataframe_extended(data: str | pd.DataFrame, metric: str, metrics: str | pd.DataFrame = None, output_path: str = None) -> tuple:
    """
    Processes a CSV DataFrame by grouping data by 'Instance' and 'Algorithm', calculating either the mean or median 
    of the 'MetricValue' column based on normality, and saving the aggregated data and standard deviations as CSV files.
    
    Args:
        data (pd.DataFrame): 
            The input DataFrame containing 'Instance', 'Algorithm', and 'MetricValue' columns.
    
        metric (str): 
            The metric name to be included in the saved filenames.
    
        metrics (pd.DataFrame):
            A DataFrame containing metrics information.

        output_path (str):
            The path to save the CSV file. Defaults None.
    
    Returns:
        pd.DataFrame: A pivoted DataFrame with 'Instance' as index and 'Algorithm' as columns, showing aggregated metric values.
            - Example:
                +----------+-------------+-------------+-------------+-------------+---------+---------+---------+
                | Instance | AutoMOPSOD  | AutoMOPSORE | AutoMOPSOW  | AutoMOPSOZ  | NSGAII  | OMOPSO  | SMPSO   |
                +==========+=============+=============+=============+=============+=========+=========+=========+
                | DTLZ1    | 0.008063    | 1.501062    | 1.204757    | 2.071152    | 0.41337 | 1.00012 | 0.01157 |
                +----------+-------------+-------------+-------------+-------------+---------+---------+---------+
                | DTLZ2    | 0.004992    | 0.006439    | 0.009557    | 0.007497    | 0.01261 | 0.00634 | 0.00565 |
                +----------+-------------+-------------+-------------+-------------+---------+---------+---------+
                | ...      | ...         | ...         | ...         | ...         | ...     | ...     | ...     |
                +----------+-------------+-------------+-------------+-------------+---------+---------+---------+
    
        pd.DataFrame: 
            A pivoted DataFrame showing standard deviations or IQR of metric values.
                - Example: (Same structure as the aggregated DataFrame)
        
        str: 
            The aggregation type used ('Mean' or 'Median').
        
        bool: 
            The maximize flag for the specified metric.

    Example:
        >>> from SAES.utils.csv_processor import process_dataframe_extended
        >>> 
        >>> # Data source
        >>> experimentData = "experimentData.csv"
        >>> 
        >>> # metric
        >>> metric = "HV"
        >>> 
        >>> df_agg_pivot, df_stats_pivot, aggregation_type, maximize = process_dataframe_extended(data, metric)
    """

    # Load the data DataFrame, either from a CSV file or as an existing DataFrame
    df = pd.read_csv(data, delimiter=",") if isinstance(data, str) else data
    df = df[df["MetricName"] == metric]

    if metrics is not None:
        # Load the metrics DataFrame, either from a CSV file or as an existing DataFrame
        df_m = pd.read_csv(metrics, delimiter=",") if isinstance(metrics, str) else metrics

        # Retrieve the maximize flag (True/False) for the specified metric
        maximize = df_m[df_m["MetricName"] == metric]["Maximize"].values[0]
    else:
        maximize = None

    output_dir = output_path if output_path else os.getcwd()

    # Check if the input & output directories exist, if not create them
    os.makedirs(os.path.join(output_dir, "CSVs"), exist_ok=True)

    # Group by 'Instance' and 'Algorithm', then calculate the median or mean of the 'Metric Value' column
    normal = check_normality(df)

    if normal:
        df_agg = df.groupby(['Instance', 'Algorithm'])['MetricValue'].mean().reset_index()
        aggregation_type = "Mean"

        df_stats = df.groupby(['Instance', 'Algorithm'])['MetricValue'].std().reset_index()
    else:
        df_agg = df.groupby(['Instance', 'Algorithm'])['MetricValue'].median().reset_index()
        aggregation_type = "Median"

        Q1 = df.groupby(['Instance', 'Algorithm'])['MetricValue'].quantile(0.25).reset_index()
        Q3 = df.groupby(['Instance', 'Algorithm'])['MetricValue'].quantile(0.75).reset_index()

        Q3["MetricValue"] = Q3["MetricValue"] - Q1["MetricValue"]
        df_stats = Q3
    
    # Pivot the DataFrame to get 'Instance' as the index and 'Algorithm' as the columns with 'Metric Value' values
    df_agg_pivot = df_agg.pivot(index='Instance', columns='Algorithm', values='MetricValue')

    # Calculate the standard deviation DataFrame 
    df_stats_pivot = df_stats.pivot(index='Instance', columns='Algorithm', values='MetricValue')
    
    # Save the DataFrames to CSV files
    df_agg_pivot.to_csv(os.path.join(output_dir, "CSVs", f"data_{aggregation_type}_{metric}.csv"), index=False)
    df_stats_pivot.to_csv(os.path.join(output_dir, "CSVs", f"data_std_{aggregation_type}_{metric}.csv"), index=False)

    # Remove the index and column names for better presentation
    df_agg_pivot.index.name = None  
    df_agg_pivot.columns.name = None 

    # Return the DataFrames and the aggregation type
    return df_agg_pivot, df_stats_pivot, aggregation_type, maximize
