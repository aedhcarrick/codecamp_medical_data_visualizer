import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
def is_overweight(row):
    if (row['weight'] / ((row['height']*0.01) ** 2) > 25):
        return 1
    return 0

df['overweight'] = df.apply(is_overweight, axis=1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol'] > 1, 0, 1)
df['gluc'] = np.where(df['gluc'] > 1, 0, 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])
    print(df_cat)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat0 = pd.melt(df.loc[df.cardio == 0], value_vars=['cholesterol','gluc','smoke','alco','active','overweight']).groupby('variable').value_counts().to_frame()
    df_cat0.rename(columns = {0:"total"}, inplace=True)
    df_cat1 = pd.melt(df.loc[df.cardio == 1], value_vars=['cholesterol','gluc','smoke','alco','active','overweight']).groupby('variable').value_counts().to_frame()
    df_cat1.rename(columns = {0:"total"}, inplace=True)
    print(df_cat0)

    # Draw the catplot with 'sns.catplot()'
    cardio_fig1 = sns.catplot(x='variable', y='total', hue='value', data=df_cat0, row=0, col=0)
    cardio_fig2 = sns.catplot(x='variable', y='total', hue='value', data=df_cat1, row=0, col=1)


    # Get the figure for the output
    fig = cardio_fig1.get_figure()


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
