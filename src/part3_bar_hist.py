import matplotlib.pyplot as plt
import seaborn as sns
'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''



# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def my_barplot(df):
    sns.barplot(data=df,x = "fta",y="fta")
    plt.savefig('./data/part3_plots/fta_barplot.png', bbox_inches='tight')




# 2. Hue the previous barplot by sex
def hue_barplot(df):
    sns.barplot(data=df,x = "fta",y="fta",hue = 'sex')
    plt.savefig('./data/part3_plots/fta_hue_barplot.png', bbox_inches='tight')


# 3. Plot a histogram of age_at_arrest
def my_hist(df):
    sns.histplot(data = df, x ="age_at_arrest")
    plt.savefig('./data/part3_plots/age_at_arrest_histogram.png', bbox_inches='tight')

# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 
def bin_hist(df):
    sns.histplot(data = df, x ="age_at_arrest",bins = [18,21,30,40,100])
    plt.savefig('./data/part3_plots/age_at_arrest_bins_histogram.png', bbox_inches='tight')