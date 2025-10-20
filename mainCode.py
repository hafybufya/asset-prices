import pandas as pd
import matplotlib.pyplot as plt

csv_in_use = "historicalData.csv"
date_column = "Date"
y_axis = "Close/Last"
# colors for plots
colour_1 = "#2596be"


def read_nordic_data():
    '''
    reads historicalData.csv file and parses the year column as a date and sets it as an index
    '''
   
    nordic_df = pd.read_csv(csv_in_use , parse_dates=[date_column],  index_col=date_column)
    return nordic_df

nordic_df = read_nordic_data()


def min_max_index():
    """getting min max of index"""
    df = pd.read_csv(csv_in_use)
    min_value = df[date_column].min()
    max_value = df[date_column].max()
    
    return min_value, max_value

#get min and max_value of data set
min_value, max_value = min_max_index()
print(min_value)
print(max_value)


def plot_nordic_graph():
#plotting both OECD women and UK same graph
    plot_nordic_graph= nordic_df.plot(kind='line',y=y_axis, label='"Close/Last"', color=colour_1, linestyle='-')
    plot_nordic_graph.set_title("Historical Data - OMX Nordic 40 (OMXN40) 2025")
    plt.show()

# plot_nordic_graph()


def plot_daily_pct_graph():
    """ plot of year vs daily percentage change"""
    nordic_pct_change = nordic_df[y_axis].pct_change()
    plt.plot(nordic_df.index, nordic_pct_change, color=colour_1, linestyle='-')
    plt.show()

# plot_daily_pct_graph()

def plot_std_pct_graph():
    """ plot of year vs standard deviation of daily percentage change"""
    x = nordic_df.index #date
    y = nordic_df[y_axis]
    e = nordic_df[y_axis].pct_change().abs() #absolute value

    plt.errorbar(x, y, e, linestyle="-",)
    plt.show()

plot_std_pct_graph()