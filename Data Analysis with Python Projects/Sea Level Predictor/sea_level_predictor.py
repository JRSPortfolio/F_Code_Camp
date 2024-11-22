import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

import numpy as np

# df = pd.read_csv('Data Analysis with Python Projects/Sea Level Predictor/epa-sea-level.csv')

# print(df.head())
# print(df.shape)

# plt.figure(figsize = (14, 7))
# plt.scatter(data = df, x = 'Year', y = 'CSIRO Adjusted Sea Level', s = 12)

# slope, intercept, r_value, p_value, std_err = linregress(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])

# y_fit = slope * df['Year'] + intercept

# pred_years = np.arange(df['Year'].iloc[-1] + 1, 2051)
# pred_years_vals = slope * pred_years + intercept

# plt.scatter(x = df['Year'], y = y_fit, s = 12)
# plt.scatter(x = pred_years, y = pred_years_vals, s =12)


# noaa_asl_df = df[['Year', 'NOAA Adjusted Sea Level']][df['Year'] >= 2000]
# noaa_slope, noaa_intercept, noaa_r_value, p_value, noaa_std_err = linregress(x = noaa_asl_df['Year'], y = noaa_asl_df['NOAA Adjusted Sea Level'])

# noaa_y_fit = noaa_slope * noaa_asl_df['Year'] + noaa_intercept
# noaa_pred_years = np.arange(noaa_asl_df['Year'].iloc[-1] + 1, 2051)
# noaa_pred_years_vals = noaa_slope * noaa_pred_years + noaa_intercept

# plt.scatter(x = noaa_asl_df['Year'], y = noaa_y_fit, s = 12)
# plt.scatter(x = noaa_pred_years, y = noaa_pred_years_vals, s = 12)

# plt.xlabel('Year')
# plt.ylabel('Sea Level (inches)')
# plt.title('Rise in Sea Level')

# plt.show()


def draw_plot():
    # Read data from file
    df = pd.read_csv('Data Analysis with Python Projects/Sea Level Predictor/epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data = df, x = 'Year', y = 'CSIRO Adjusted Sea Level', s =12)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
    y_fit = slope * df['Year'] + intercept

    pred_years = np.arange(df['Year'].iloc[-1] + 1, 2051)
    pred_years_vals = slope * pred_years + intercept

    plt.scatter(x = df['Year'], y = y_fit, s =12)
    plt.scatter(x = pred_years, y = pred_years_vals, s =12)

    # Create second line of best fit
    noaa_asl_df = df[['Year', 'NOAA Adjusted Sea Level']][df['Year'] >= 2000]
    noaa_slope, noaa_intercept, noaa_r_value, p_value, noaa_std_err = linregress(x = noaa_asl_df['Year'], y = noaa_asl_df['NOAA Adjusted Sea Level'])
    
    noaa_y_fit = noaa_slope * noaa_asl_df['Year'] + noaa_intercept
    noaa_pred_years = np.arange(noaa_asl_df['Year'].iloc[-1] + 1, 2051)
    noaa_pred_years_vals = noaa_slope * noaa_pred_years + noaa_intercept
    
    plt.scatter(x = noaa_asl_df['Year'], y = noaa_y_fit, s =12)
    plt.scatter(x = noaa_pred_years, y = noaa_pred_years_vals, s =12)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()