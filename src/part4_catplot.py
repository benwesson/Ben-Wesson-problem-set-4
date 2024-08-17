import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''

##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do thisis that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony

# 2. Merge `felony_charge` with `pre_universe` into a new dataframe

# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes

##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.
def cat_felony(df1,df2):    
    merged_df = pd.concat([df1,df2],axis=1)
    sns.catplot(data = merged_df,x="offense_category",y="prediction_felony",kind='bar')
    plt.savefig('./data/part4_plots/cat_felony.png', bbox_inches='tight')

# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest
# 
# In a print statement, answer the following question: What might explain the difference between the plots?
def cat_nonfelony(df1,df2):    
    merged_df = pd.concat([df1,df2],axis=1)
    sns.catplot(data = merged_df,x="offense_category",y="prediction_nonfelony",kind='bar')
    plt.savefig('./data/part4_plots/cat_nonfelony.png', bbox_inches='tight')
    print("What might explain the difference between the plots? : Property is higher than predicted and violent and other are lower. Data could be trained on a location where felonies are more evenlly split, but is making predictions about an area where felonies are not evenly split ")
# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
# 
def cat_hue(df1,df2):    
    merged_df = pd.concat([df1,df2],axis=1)
    sns.catplot(data = merged_df,x="offense_category",y="prediction_felony",kind='bar',hue ="y_felony")
    plt.savefig('./data/part4_plots/cat_hue.png', bbox_inches='tight')
    print("what does it mean that prediction for arrestees with a current felony charge, but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, but who did get rearrested for a felony crime? ")
    print("It means that if you got arrested once for a felony charge you are predicted have a higher chance to commit a future felony than some who commited a felony then a misdemeanor")
# In a print statement, answer the following question: 
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime?