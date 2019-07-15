from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(style = 'darkgrid')

user_response_yes = ['y','Y','yes','YES','Yes']
user_response_no = ['n', 'N','no', 'NO','No']

def ReadCSV (input_CSV):

    # Reads CSV files and converts them to a panda DataFrame (long format)

    # read csv file and drop 'row ID' from dataframe. Note 'wf' = 'wide format'
    df_wf = pd.read_csv(input_CSV, sep=',').drop(['row ID'], axis='columns')
    
    # extract measurements and timepoints
    df_nuc = df_wf[['Mean_nucleus', 'Centroid Time', 'Label_Arr[1]']]
    df_cyto = df_wf[['Mean_cytoplasm', 'Centroid Time', 'Label_Arr[1]']]

    # add label column for nuc and cyto labels respectively
    df_nuc['label'] = 'Nuc'
    df_cyto['label'] = 'Cyto'

    # rename columns
    df_nuc.columns = ['signal', 'time', 'track','label']
    df_cyto.columns = ['signal', 'time', 'track','label']

    # create dataframe series
    frames = [df_nuc, df_cyto]

    # create new composite dataframe. Note 'lf' = 'long format'
    df_lf = pd.concat(frames)
    
    return df_lf

def IntensityScatterPlot (input_df_lf):

    user_input_intensity_plot = input('Generate intensity scatter plot? (y/n): ')

    if user_input_intensity_plot in user_response_yes:
        df_signal_sum = input_df_lf.groupby('track').sum().reset_index()
        sns.relplot(x='track', y='signal', hue='track', data=df_signal_sum) # displays each tracks total nuc and cyto signal over total time.
    else:
        print('Intensity scatter plot skipped...')

    plt.show()

    return None

def TrackFilter (input_df_lf):

    #TODO:  Recode to allow selection of values above or below a user defined threashold
    df_signal_sum = input_df_lf.groupby('track').sum().reset_index()
    sorted_tracks = []

    # filter dataset for tracks that meet the desired threshold - get track ID
    user_input_track_filter = input('Trim data? (y/n): ')

    if user_input_track_filter in user_response_yes:
        user_input_trim_select = int(input('Remove data points above (1) or below (2) threashold value: '))

        if user_input_trim_select == 1:
            sort_value = (float(input("Enter threashold value. Data points ABOVE this value will be removed: ")))
            for index, row in df_signal_sum.iterrows():
                if row['signal'] <= sort_value:
                    sorted_tracks.append(row['track'])
        elif user_input_trim_select == 2:
            sort_value = (float(input("Enter threashold value. Data points BELOW this value will be removed: ")))
            for index, row in df_signal_sum.iterrows():
                if row['signal'] >= sort_value:
                    sorted_tracks.append(row['track'])
        else:
            print("No selection made.  Skipping...")
            return input_df_lf

        sorted_tracks_unique = set(sorted_tracks) # just in case data output generates duplicate track names
        df_sorted = pd.DataFrame(columns=['signal', 'time', 'track', 'label'])

        for index, row in input_df_lf.iterrows():
            if row['track'] in sorted_tracks_unique:
                df_sorted = df_sorted.append({'signal':row['signal'],'time':row['time'],'track':row['track'],'label':row['label']}, ignore_index=True)
            else:
                None

        print(df_sorted)
        
        return df_sorted
    else:
        print('Trim data skipped...')
        return input_df_lf   

def ShadeErrorPlot (input_df_lf):
    user_input_shade_plot = input('Generate shade error plot? (y/n): ')

    if user_input_shade_plot in user_response_yes:
        sns.relplot(x='time', y='signal', hue='label', style='label', kind='line', data=input_df_lf)
        plt.show()
    else:
        print('Shade error plot skipped...')

def WriteDataFrame (input_df_lf):

    user_input_write_file = input('Write data to CSV? (y/n): ')

    if user_input_write_file in user_response_yes:
        user_file_name = input('Enter file name: ') + '.csv'
        input_df_lf.to_csv(user_file_name)
    else:
        print('Write file skipped...')

    return None
    
input_data = input("Enter CSV file path: ")
data = ReadCSV(input_data)
IntensityScatterPlot(data)
data = TrackFilter(data)
ShadeErrorPlot(data)
WriteDataFrame(data)