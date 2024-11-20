import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('Data Analysis with Python Projects/Medical Data Visualizer/medical_examination.csv')

# 2
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = df['BMI'].apply(lambda i: 1 if i > 25 else 0)

# 3
df['cholesterol'] = df['cholesterol'].apply(lambda i: 1 if i > 1 else 0)
df['gluc'] = df['gluc'].apply(lambda i: 1 if i > 1 else 0)
df = df.drop(columns = ['BMI'])
df = df.dropna(axis = 0)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df[['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']], var_name = 'Category', value_name = 'Value').groupby(['Category', 'Value']).size().unstack(fill_value = 0)

    # 6
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars =  ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name = 'Category', value_name = 'Value').groupby(['Category', 'Value', 'cardio']).size().unstack(fill_value = 0)
    

    # 7
    long_df = pd.melt(df_cat.reset_index(), id_vars = ['Category', 'Value'], var_name = 'cardio', value_name = 'Count')
    


    # 8
    fig = sns.catplot(long_df, x = 'Category', y = 'Count', hue = 'Value', col = 'cardio',kind = 'bar')


    # 9
    fig.savefig('Data Analysis with Python Projects/Medical Data Visualizer/catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))
                 & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]
    # df_heat = df[df['ap_lo'] <= df['ap_hi']]
    # df_heat =df_heat[df_heat['height'] >= df_heat['height'].quantile(0.025)]
    # df_heat =df_heat[df_heat['height'] <= df_heat['height'].quantile(0.975)]
    # df_heat = df_heat[df_heat['weight'] >= df_heat['weight'].quantile(0.025)]
    # df_heat = df_heat[df_heat['weight'] <= df_heat['weight'].quantile(0.975)]

    
    # 12
    corr = df_heat.corr()


    # 13
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    

    # 14
    fig, ax = plt.subplots(1, 1, figsize = (16, 10))

    # 15
    sns.heatmap(corr, annot = True, mask = mask, fmt = '.1f', ax = ax)

    
    # 16
    fig.savefig('Data Analysis with Python Projects/Medical Data Visualizer/heatmap.png')
    return fig