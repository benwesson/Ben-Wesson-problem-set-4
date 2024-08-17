import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
def predict_scatter(df):
    sns.lmplot(data = df,x = "prediction_felony",y ="prediction_nonfelony",hue="y_felony")
    plt.savefig('./data/part5_plots/predict_scatter.png', bbox_inches='tight')
    print("What can you say about the group of dots on the right side of the plot? : They had a higher predicited chance to commit felonies and many of them  ended up commiting felonies. Still smaller grouping then the left side of plot ")

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
def arrest_scatter(df):
    sns.lmplot(data = df,x = "prediction_felony",y ="y_felony")
    plt.savefig('./data/part5_plots/arrest_scatter.png', bbox_inches='tight')
    print("Would you say based off of this plot if the model is calibrated or not?  : I would say the model is not calibrated because I am trying to map a numeric value to a categorica; value in a scatter plot")