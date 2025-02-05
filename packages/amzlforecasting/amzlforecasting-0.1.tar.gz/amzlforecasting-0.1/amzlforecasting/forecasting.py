import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from dateutil import parser
from pathlib import Path
import matplotlib.pyplot as plt


def load_data():
    station_mapping = Path(__file__).parent / 'data' / 'station_mapping.csv'
    station_geo_profile = Path(__file__).parent / 'data' / 'station_geo_profile.csv'
    return pd.read_csv(station_mapping), pd.read_csv(station_geo_profile)

### Working with Amazon timeseries data

def get_yearweek(date_input):

    if isinstance(date_input, str):
        try:
            date = parser.parse(date_input)
        except ValueError:
            raise ValueError(f"Unable to parse date string: {date_input}")
        
    elif isinstance(date_input, datetime):
        date = date_input
    else:
        raise TypeError("Input must be a datetime object or date string")
    
    date = date + timedelta(days=1)
    year, week, _ = date.isocalendar()
    yearweek = int(str(year)+str(week).zfill(2))
    
    return yearweek

def get_dow(date_input): 
    
    if isinstance(date_input, str):
        try:
            date = parser.parse(date_input)
        except ValueError:
            raise ValueError(f"Unable to parse date string: {date_input}")
        
    elif isinstance(date_input, datetime):
        date = date_input
    else:
        raise TypeError("Input must be a datetime object or date string")

    return (date.weekday() + 1) % 7

def get_week(date_input):
    
    if isinstance(date_input, str):
        try:
            date = parser.parse(date_input)
        except ValueError:
            raise ValueError(f"Unable to parse date string: {date_input}")
        
    elif isinstance(date_input, datetime):
        date = date_input
        
    date = date + timedelta(days=1)
    _, week, _ = date.isocalendar()
    
    return week
        
def get_date(year, week, dow=0):
    
    jan_first = datetime(year, 1, 1)
    jan_first_dow = jan_first.weekday()
    
    if jan_first_dow <= 2:
        first_wed = jan_first + timedelta(days=(2 - jan_first_dow))
    else:
        first_wed = jan_first + timedelta(days=(9 - jan_first_dow))
        
    start_of_first_week = first_wed - timedelta(days=3)
    start_of_week = start_of_first_week + timedelta(weeks=(week - 1))
    date = start_of_week + timedelta(days=dow)
    
    return date

def get_date_from_yearweek(yearweek, dow=0):
    
    year = yearweek // 100
    week = yearweek % 100
    
    return get_date(year, week, dow)

def create_week_range(start_week, end_week):
    
    if start_week <= end_week: 
        return list(range(start_week, end_week +1))
    else:
        return list(range(start_week, 53)) + list(range(1, end_week + 1))

def create_yearweek_range(start_yearweek, end_yearweek):
    
    start_year = start_yearweek // 100
    start_week = start_yearweek % 100
    end_year = end_yearweek // 100
    end_week = end_yearweek % 100

    result = []

    current_year = start_year
    current_week = start_week

    while True:
        result.append(current_year * 100 + current_week)
        if current_year == end_year and current_week == end_week:
            break
        current_week += 1
        if current_week > 52:
            current_week = 1
            current_year += 1
            
    return result

def create_date_range(start_date_input, end_date_input, format="DatetimeIndex"):
    
    def convert_to_datetime(date_input):
        if isinstance(date_input, str):
            return pd.to_datetime(date_input)
        elif isinstance(date_input, datetime):
            return pd.to_datetime(date_input)
        else:
            raise TypeError("Input must be a datetime object or date string")

    start_date = convert_to_datetime(start_date_input)
    end_date = convert_to_datetime(end_date_input)
    
    date_range = pd.date_range(start_date, end_date)
    
    if format == "DatetimeIndex":
        return date_range
    elif format == "list":
        return date_range.to_list()
    else:
        raise ValueError("Invalid format specified. Use 'DatetimeIndex' or 'list'.")
    
def calculate_yearweek(yearweek, addition):
    # Convert yearweek to datetime
    year = int(str(yearweek)[:4])
    week = int(str(yearweek)[4:])
    
    # Create a datetime object for the first day of the given week
    date = datetime.strptime(f'{year}-W{week:02d}-1', "%Y-W%W-%w")
    
    # Add the specified number of weeks
    new_date = date + timedelta(weeks=addition)
    
    # Calculate the new year and week number
    new_year = new_date.isocalendar()[0]
    new_week = new_date.isocalendar()[1]
    
    # Format the result as yearweek
    return int(f"{new_year}{new_week:02d}")

    
### Forecast Auditing and Accuracy Measurement

def calculate_mape(actual, pred, method='custom'):
    """
    Calculate the Mean Absolute Percentage Error (MAPE) between actual and predicted values.
    
    Parameters:
    actual (array-like): Array of actual values
    pred (array-like): Array of predicted values
    method (str): 'standard' for traditional MAPE, 'custom' for company's custom MAPE
    
    Returns:
    float: MAPE value as a decimal (e.g., 0.05 for 5% MAPE)
    """
    actual = np.array(actual)
    pred = np.array(pred)
    
    if method == 'standard':
        # Avoid division by zero
        mask = actual != 0
        return np.mean(np.abs((actual[mask] - pred[mask]) / actual[mask]))
    elif method == 'custom':
        # Custom MAPE with prediction in denominator
        mask = pred != 0
        return np.mean(np.abs((actual[mask] - pred[mask]) / pred[mask]))
    else:
        raise ValueError("Method must be either 'standard' or 'custom'")
    
def calculate_delta(latest, prior):
    latest = np.array(latest)
    prior = np.array(prior)
    
    return np.divide(latest, prior, 
                     where=prior!=0, 
                     out=np.full_like(latest, np.nan, dtype=float)) - 1
    
calculate_pop = calculate_delta
calculate_bias = calculate_delta

def calculate_fill(actual, planned):
    actual = np.array(actual)
    planned = np.array(planned)
    
    return np.divide(actual, planned,
                     where=planned!=0,
                     out=np.zeros_like(actual, dtype=float))
    
calculate_utilization = calculate_fill
calculate_caps_position = calculate_fill

### Dataframe Feature Standardization

COLUMN_MAPPING = {
    'station': ['Station', 'station', 'Node', 'node', 'DS', 'ds', 'node_id', 'lm_node'],
    'date': ['Date', 'date', 'ofd', 'ofd_date', 'override_date', 'forecast_date'],
    'uvp_region': ['Super_region', 'super_region', 'destination_country'], 
    'week': ['Week', 'week', 'ofd_week'], 
    'dow': ['dow', 'DoW', 'DOW', 'ofd_dow'],
    'country': ['Country', 'country']
}

STATION_MAPPING, STATION_GEO_PROFILE = load_data()

def read_amzl_csv(filepath, pid=None):
    
    if pid == None:
        pid = filepath.split("\\")[-1].split(".")[0]
    
    COLUMNS_TO_DROP = ['Region', 'region', 'MSA', 'msa', 'Planner', 'planner']
    INDEX_COLUMNS = ['plan_id', 'country', 'region', 'station', 'forecast_planner', 'deliver_planner', 'week', 'dow', 'date']
    
    amzl_tsdf = pd.read_csv(filepath)
    amzl_tsdf = amzl_tsdf.drop(columns=[col for col in COLUMNS_TO_DROP if col in amzl_tsdf.columns])
    
    for standard_name, possible_names in COLUMN_MAPPING.items():
        for col in possible_names:
            if col in amzl_tsdf.columns:
                amzl_tsdf.rename(columns={col: standard_name}, inplace=True)
                break
    
    amzl_tsdf = amzl_tsdf.merge(STATION_MAPPING, on='station', how='left')
    amzl_tsdf['date'] = pd.to_datetime(amzl_tsdf['date'])
    amzl_tsdf['dow'] = amzl_tsdf['date'].apply(get_dow)
    amzl_tsdf['week'] = amzl_tsdf['date'].apply(get_yearweek)
    amzl_tsdf['plan_id'] = pid
    amzl_tsdf['country'] = 'US'
    
    amzl_tsdf.set_index(INDEX_COLUMNS, inplace=True)
    
    non_numeric_cols = amzl_tsdf.select_dtypes(exclude=['number']).columns.tolist()
    removed_columns = non_numeric_cols.copy()
    
    amzl_tsdf = amzl_tsdf.drop(columns=non_numeric_cols)
    
    return amzl_tsdf

### Tablular Data Handling
def join_tsdf(tsdf_1, tsdf_2):
    lsuffix = "_" + tsdf_1.index.get_level_values('plan_id').unique()[0]
    rsuffix = "_" + tsdf_2.index.get_level_values('plan_id').unique()[0]
    
    tsdf_1_temp = tsdf_1.reset_index(level='plan_id', drop=True)
    tsdf_2_temp = tsdf_2.reset_index(level='plan_id', drop=True)
    
    df_joined = tsdf_1_temp.join(tsdf_2_temp, lsuffix=lsuffix, rsuffix=rsuffix)
    df_joined['plan_id'] = 'joined_tsdf'
    df_joined = df_joined.set_index('plan_id', append=True)
    
    new_order = [df_joined.index.nlevels - 1] + list(range(df_joined.index.nlevels - 1))
    df_joined = df_joined.reorder_levels(new_order)
    
    return df_joined

def summarize_dataframe(df: pd.DataFrame):
    # Reset the index to flatten the multi-index columns
    df_flat = df.reset_index()
    summary = {}

    # Loop through each column in the flattened DataFrame
    for col in df_flat.columns:
        col_data = df_flat[col]
        
        if 'plan_id' in col:
            summary[col] = df_flat[col].iloc[0]
        elif 'week' in col and np.issubdtype(col_data.dtype, np.number):
            summary[col] = f"Week range: {col_data.min()} - {col_data.max()}"       
        elif 'date' in col:
            try:
                col_data = pd.to_datetime(col_data)
                summary[col] = f"Date range: {col_data.min().date()} - {col_data.max().date()}"
            except:
                pass
        elif 'dow' in col:
            pass
        elif np.issubdtype(col_data.dtype, np.number):
            summary[col] = f"Average: {col_data.mean()}"
        elif col_data.dtype == object:
            summary[col] = f"Unique values count: {col_data.nunique()}"
        else:
            summary[col] = "Data type not handled"
    
    return summary


## plotting

def plot_line(df, x_col, y_cols, title=None, xlabel=None, ylabel=None, legend=True):
    """
    Creates a line plot from a DataFrame.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the data.
        x_col (str): The name of the column to be used for the x-axis.
        y_cols (list of str): A list of column names to be plotted on the y-axis.
        title (str, optional): The title of the plot.
        xlabel (str, optional): The label for the x-axis.
        ylabel (str, optional): The label for the y-axis.
        legend (bool, optional): Whether to display the legend. Default is True.

    Returns:
        matplotlib.figure.Figure: The generated plot figure.
    """
    plt.figure(figsize=(22, 6))

    for y_col in y_cols:
        plt.plot(df[x_col], df[y_col], label=y_col)

    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    else:
        plt.xlabel(x_col)
    if ylabel:
        plt.ylabel(ylabel)
    else:
        plt.ylabel(", ".join(y_cols))
    
    if legend:
        plt.legend()

    plt.xticks(rotation=90)
    plt.grid(True)
    plt.tight_layout()

    # Show plot
    plt.show()

def plot_scatter(df, x_col, y_col, c_col=False, l_col=False, k=5, title=None):
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    if c_col == False:
        ax.scatter(df[x_col], df[y_col], s=130, cmap='Blues', linestyle='-', edgecolors='black')
        
    else:
        ax.scatter(df[x_col], df[y_col], c=df[c_col], cmap='Blues', s=130, linestyle='-', edgecolors='black')
        
    if title:
        ax.set_title(title)
        
    if l_col:
        for i, row in df[-k:].iterrows():
            ax.text(row[x_col], row[y_col], row[l_col].astype(int), fontsize=12, ha='left')
            
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
        
    ax.set_facecolor('lightgray')
    
    plt.show()
    
    
def plot_scatter_w_marker(df, df2, x_col, y_col, quantiles=['mean', '0.6', '0.7'], c_col=False, l_col=False, k=5, title=None):
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    if c_col == False:
        ax.scatter(df[x_col], df[y_col], s=130, cmap='Blues', linestyle='-', edgecolors='black')
        
    else:
        ax.scatter(df[x_col], df[y_col], c=df[c_col], cmap='Blues', s=130, linestyle='-', edgecolors='black')
        
    if title:
        ax.set_title(title)
        
    if l_col:
        for i, row in df[-k:].iterrows():
            ax.text(row[x_col], row[y_col], row[l_col].astype(int), fontsize=12, ha='left')
            
    for q in quantiles:
                
        for idx, row in df2.iterrows():
            marker_color = 'red'
            marker_shape = 'x'
            marker_label = f"S{int(row['scenario'])}-{q} "
            marker_x = row['cost_offsets_b']
            marker_y = row[q]
            
            ax.scatter(marker_x, marker_y, color=marker_color, marker=marker_shape, s=100, label=marker_label)
            ax.text(marker_x, marker_y, marker_label, fontsize=12, ha='right', color='red')
        
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_facecolor('lightgray')
    
    plt.show()
    
def create_table(df, x_col, y_cols, title=None):
    """
    Creates a formatted table from a DataFrame with x-axis values as columns
    and y-axis data as rows, including a % delta row between first two rows.
    Drops any columns containing NA values in any row.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the data.
        x_col (str): The name of the column to be used for column headers.
        y_cols (list of str): A list of column names to be shown as rows.
        title (str, optional): The title of the table.

    Returns:
        pandas.DataFrame: A restructured DataFrame with x values as columns,
                         y values as rows, and an additional % delta row.
    """
    # Create a new DataFrame with x values as columns
    table_data = {}
    
    # Get unique x values maintaining order
    x_values = df[x_col].unique()
    
    # For each y column, create a row of data
    for y_col in y_cols:
        # Create a dictionary mapping x values to y values
        y_values = {x_val: df[df[x_col] == x_val][y_col].iloc[0] 
                   if not df[df[x_col] == x_val][y_col].empty 
                   else None
                   for x_val in x_values}
        table_data[y_col] = y_values
    
    # Create the table DataFrame
    table_df = pd.DataFrame(table_data).T
    
    # Set the column names to the x values
    table_df.columns = x_values
    
    # Drop columns with any NaN values
    table_df = table_df.dropna(axis=1, how='any')
    
    # Calculate % delta between first two rows if we have at least 2 rows
    if len(y_cols) >= 2:
        first_row = table_df.iloc[0]
        second_row = table_df.iloc[1]
        
        # Calculate percentage change
        delta_row = ((second_row - first_row) / first_row * 100).round(1)
        
        # Add % suffix to values
        delta_row = delta_row.apply(lambda x: f'{x:+.1f}%')
        
        # Add delta row to the DataFrame
        table_df.loc[f'Δ {y_cols[1]} vs {y_cols[0]} (%)'] = delta_row
    
    if title:
        print(f"\n{title}\n")
    
    return table_df
    
    
# eda
def multi_column_value_counts(df, columns):
    result = {}
    for column in columns:
        result[column] = df[column].value_counts()
    return pd.DataFrame(result)