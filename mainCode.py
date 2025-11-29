# ---------------------------------------------------------------------
# IMPORTED FUNCTIONS USED IN PROGRAM
# ---------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------
# Defined CSV file name and columns as well as colours used in program
#  -> make the code flexible if used dataset changed
#  -> or to reuse the same function for a different file.
# ---------------------------------------------------------------------


csv_in_use = "historicalData.csv"
date_column = "Date"
y_axis = "Close/Last"

# Colours for plots
colour_1 = "#2596be"

# ---------------------------------------------------------------------
# FUNCTION: Read CSV data into Dataframe
# ---------------------------------------------------------------------

def read_nordic_data():
    """

    Loads the csv dataset defined in 'csv_in_use'

    Returns
    -------

    pandas Dataframe -> converts csv to df containing line data with date_column as index

    """
    
   
    nordic_df = pd.read_csv(csv_in_use , parse_dates=[date_column],  index_col=date_column)
    return nordic_df

nordic_df = read_nordic_data()

# ---------------------------------------------------------------------
# FUNCTION: Gets min and max from index
# ---------------------------------------------------------------------

def min_max_index(csv_in_use, date_column):
    """getting min max of index as Timestamps"""
    df = pd.read_csv(csv_in_use)
    datetime_dates = pd.to_datetime(df[date_column])
    converted_datetime_dates = datetime_dates
    min_value = converted_datetime_dates.min()
    max_value = converted_datetime_dates.max()
    
    return min_value.strftime("%Y-%m-%d"), max_value.strftime("%Y-%m-%d")


# ---------------------------------------------------------------------
# FUNCTION: Plots line graph of year and close
# ---------------------------------------------------------------------

def plot_nordic_graph():

    plot_nordic_graph= nordic_df.plot(kind='line',y=y_axis, label=y_axis, color=colour_1, linestyle='-')
    plot_nordic_graph.set_title(f"OMX Nordic 40 {y_axis} in 2025")
    plt.show()


# ---------------------------------------------------------------------
# FUNCTION: Plots  graph of year and Dailly percentage change
# ---------------------------------------------------------------------


def plot_daily_pct_graph():
    """ plot of year vs daily percentage change"""
    nordic_pct_change = nordic_df[y_axis].pct_change()
    plt.plot(nordic_df.index, nordic_pct_change, color=colour_1, linestyle='-')
    plt.xlabel(date_column)
    plt.ylabel(y_axis)
    plt.title ("Plot of Year vs Daily Percentage Change")

    plt.show()


# ---------------------------------------------------------------------
# FUNCTION: Plots graph of year and STD of daily percentage change
# ---------------------------------------------------------------------

def plot_std_pct_graph():
    """ plot of year vs standard deviation of daily percentage change"""
    x = nordic_df.index # Date
    y = nordic_df[y_axis]
    e = nordic_df[y_axis].pct_change().abs() # Absolute value

    plt.title ("Plot of Year vs Standard Deviation of Daily Percentage Change")
    plt.errorbar(x, y, e, linestyle="-",)
    plt.show()


# run program
if __name__ == "__main__":

    # Get min and max_value of data set
    min_value, max_value = min_max_index(csv_in_use, date_column)
    print(min_value)
    print(max_value)
    plot_nordic_graph()
    plot_daily_pct_graph()
    plot_std_pct_graph()


