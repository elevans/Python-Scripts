from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

def ReadCSV (path):

    try:
        print("Reading file...")
        df = pd.read_csv(path, sep=',').drop(['row ID'], axis='columns')
    except:
        df = pd.read_csv(path, sep=',')

    return df

def TrackSumScatter (input_df, channel_name):

    # check for valid channel name
    df_col_names = list(input_df.columns.values)
    
    for x in df_col_names:
        if channel_name in df_col_names:
            continue
        else:
            print (channel_name + " was not found in the input file.")
            return None

    print("Suming track signals...")
    df_signal_sum = input_df.groupby('track').sum().reset_index()
    sns.relplot(x='track', y=channel_name, data=df_signal_sum)
    plt.show()

    return None