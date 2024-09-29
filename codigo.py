import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

lower_limit = df['value'].quantile(0.025)
upper_limit = df['value'].quantile(0.975)
df_clean = df[(df['value'] >= lower_limit) & (df['value'] <= upper_limit)]

def draw_line_plot():
    plt.figure(figsize=(12, 6))
    plt.plot(df_clean.index, df_clean['value'], color='blue', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.savefig('line_plot.png')
    plt.show()

def draw_bar_plot():
    df['year'] = df.index.year
    df['month'] = df.index.month_name()
    df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()

    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df_bar[months_order]

    df_bar.plot(kind='bar', figsize=(12, 6))
    plt.title('Average Daily Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', bbox_to_anchor=(1, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    plt.show()

def draw_box_plot():
    df['year'] = df.index.year
    df['month'] = df.index.month

    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='value', data=df, order=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    
    plt.tight_layout()
    plt.savefig('box_plot.png')
    plt.show()
    
if __name__ == '__main__':
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()