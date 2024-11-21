import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import calendar
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('Data Analysis with Python Projects/Page View Time Series Visualizer/fcc-forum-pageviews.csv', index_col = 'date')


# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
df.index = pd.to_datetime(df.index)


def draw_line_plot():
    fig, axes = plt.subplots(figsize = (20, 6))
    sns.lineplot(df, x = 'date', y = 'value')
    axes.set_position([0.06, 0.09, 0.93, 0.87])
    axes.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    axes.set_xlabel('Date')
    axes.set_ylabel('Page Views')
    ticks = pd.date_range(start = df.index.min(), end = df.index.max(), periods = 8)
    plt.xticks(ticks = ticks, labels = ticks.strftime('%Y-%m'))
    
    # Save image and return fig (don't change this part)
    fig.savefig('Data Analysis with Python Projects/Page View Time Series Visualizer/line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Month'] = df.index.month
    df_bar['Year'] = df.index.year
    df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean().unstack(level = 0).reset_index().melt(id_vars = 'Month', var_name = 'Year', value_name = 'value')
    df_bar['Month'] = df_bar['Month'].map(lambda i: calendar.month_name[i])

    # Draw bar plot
    fig, axes = plt.subplots(figsize = (15, 6))
    sns.barplot(data = df_bar, x = 'Year', y = 'value', hue = 'Month', palette = 'bright')
    axes.set_ylabel('Average Page Views')
    axes.set_xlabel('Years')

    # Save image and return fig (don't change this part)
    fig.savefig('Data Analysis with Python Projects/Page View Time Series Visualizer/bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    month_order = list(calendar.month_abbr[1:]) 
    df_box['month'] = pd.Categorical(df_box['month'], categories = month_order, ordered = True)

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize = (15, 6))
    sns.boxplot(df_box, hue = 'year', y = 'value', ax = axes[0], palette = 'bright')
    sns.boxplot(df_box, hue = 'month', y = 'value', ax = axes[1], palette = 'bright')
    axes[0].set_ylabel('Page Views')
    axes[1].set_ylabel('Page Views')
    axes[0].set_xlabel('Year')
    axes[1].set_xlabel('Month')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('Data Analysis with Python Projects/Page View Time Series Visualizer/box_plot.png')
    return fig