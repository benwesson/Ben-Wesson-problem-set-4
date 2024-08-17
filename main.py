'''
- You will run Problem Set 4 from this .py, so make sure to set things up to return outputs accordingly
- Go through each PART and write code / make updates as necessary to produce all required outputs
- Run main.py before you start
'''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import src.part1_etl as part1
import src.part2_plot_examples as part2
import src.part3_bar_hist as part3
import src.part4_catplot as part4
import src.part5_scatter as part5

def main():
    ##  PART 1: ETL  ##
    # ETL the datasets into dataframes
    directories = ['data/part2_plots', 'data/part3_plots', 'data/part4_plots', 'data/part5_plots']
    part1.create_directories(directories)
    
    pred_universe, arrest_events, charge_counts, charge_counts_by_offense = part1.extract_transform()
    #print(pred_universe)
    #print(charge_counts_by_offense)
    ##  PART 2: PLOT EXAMPLES  ##
    # Apply plot theme
    part2.seaborn_settings()

    # Generate plots
    part2.barplots(charge_counts, charge_counts_by_offense)
    part2.cat_plots(charge_counts, pred_universe)
    part2.histograms(pred_universe)
    part2.scatterplot(pred_universe)

    ##  PART 3: BAR PLOTS AND HISTOGRAMS  ##
    # 1
    part3.my_barplot(pred_universe)
    # 2
    part3.hue_barplot(pred_universe)
    # 3
    part3.my_hist(pred_universe)
    # 4
    part3.bin_hist(pred_universe)


    ##  PART 4: CATEGORICAL PLOTS  ##
    # 1
    part4.cat_felony(pred_universe,charge_counts_by_offense)
    # 2
    part4.cat_nonfelony(pred_universe,charge_counts_by_offense)
    
    # 3
    part4.cat_hue(pred_universe,charge_counts_by_offense)
    ##  PART 5: SCATTERPLOTS  ##
    # 1
    #print(pred_universe.columns)
    part5.predict_scatter(pred_universe)
    # 2 
    part5.arrest_scatter(pred_universe)
if __name__ == "__main__":
    main()
