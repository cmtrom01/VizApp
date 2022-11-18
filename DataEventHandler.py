from matplotlib.figure import Figure
import pandas as pd
from Dataset import Dataset
from dateutil import parser

class DataEventHandler:
    def __init__(self):
        self.dataset = Dataset()

    def set_dataset(self, fpath):
        self.dataset.set_fpath(fpath)
        print(self.dataset)

    def get_first_level_folders(self):
        return self.dataset.get_first_level_folders()

    def get_second_level_folders(self):
        return self.dataset.get_second_level_folders()

    def set_first_directory(self, first_directory):
        self.dataset.set_first_directory(first_directory)
    def set_second_directory(self, second_directory):
        self.dataset.set_second_directory(second_directory)
    def get_first_directory(self):
        self.dataset.get_first_directory()

    def get_columns(self):
        return self.dataset.get_columns()

    def graph_data(self):
        print('hey')
        columns = self.dataset.get_current_columns()
        df = self.dataset.get_dataframe()

        for col in columns:
            print(col)
        ##get columns
        ##plot graph for each column

    def set_current_columns(self, columns):
        self.dataset.set_current_columns(columns)

    '''
    def get_dataframe():
        return dataset.get_dataframe()
    
    def switch_times():
        time = dataset.get_time()
        if time == 'UTC':
            dataset.set_time('EST')
        else:
            dataset.set_time('UTC')
    
    def get_graph_figure(fig):
        df = dataset.get_dataframe()
        values_to_plot = df['Acc magnitude avg']
        time = dataset.get_time()
        if time == 'UTC':
            time = df['Datetime (UTC)']
            plot1 = fig.add_subplot(111)
            plot1.plot_date(pd.to_datetime(time), values_to_plot)
        else:
            time = pd.to_datetime(df['Datetime (UTC)']).dt.tz_convert('US/Central')
            plot1 = fig.add_subplot(111)
            plot1.plot_date(time, values_to_plot)
        return fig
    
    def get_correlation():
        df = dataset.get_dataframe()
        cor = df['Acc magnitude avg'].corr(df['Unix Timestamp (UTC)'])
        return cor
    
    def zoom_in(fig):
        dataset.increment_idx()
        start_idx = dataset.get_start_idx()
        end_idx = dataset.get_end_idx()
        df = dataset.get_dataframe()
        values_to_plot = df['Acc magnitude avg']
        time = dataset.get_time()
        if time == 'UTC':
            time = df['Datetime (UTC)']
            plot1 = fig.add_subplot(111)
            plot1.plot_date(pd.to_datetime(time)[start_idx:end_idx], values_to_plot[start_idx:end_idx])
        else:
            time = pd.to_datetime(df['Datetime (UTC)']).dt.tz_convert('US/Central')
            plot1 = fig.add_subplot(111)
            plot1.plot_date(time[start_idx:end_idx], values_to_plot[start_idx:end_idx])
        return fig
    
    def zoom_out(fig):
        dataset.decrement_idx()
        start_idx = dataset.get_start_idx()
        end_idx = dataset.get_end_idx()
        df = dataset.get_dataframe()
        values_to_plot = df['Acc magnitude avg']
        time = dataset.get_time()
        if time == 'UTC':
            time = df['Datetime (UTC)']
            plot1 = fig.add_subplot(111)
            plot1.plot_date(pd.to_datetime(time)[start_idx:end_idx], values_to_plot[start_idx:end_idx])
        else:
            time = pd.to_datetime(df['Datetime (UTC)']).dt.tz_convert('US/Central')
            plot1 = fig.add_subplot(111)
            plot1.plot_date(time[start_idx:end_idx], values_to_plot[start_idx:end_idx])
        return fig
    '''
