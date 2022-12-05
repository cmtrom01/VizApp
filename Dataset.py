import pandas as pd
import os

class Dataset:
    def __init__(self, fpath=None):
        self.fpath = fpath
        self.dataframe = None
        self.time = 'EST'
        self.start_idx = 0
        self.end_idx = None
        self.min = 0
        self.max = None
        self.step = 5
        self.first_directory = None
        self.second_directory = None
        self.current_columns = ['Datetime (UTC)', 'Unix Timestamp (UTC)']

    def get_first_level_folders(self):
        print('Getting first level folders...')
        return_array = []
        for dir in os.listdir(self.fpath):
            print(dir)
            return_array.append(dir)
        return return_array

    def set_first_directory(self, first_directory):
        self.first_directory = first_directory
    def set_second_directory(self, second_directory):
        self.second_directory = second_directory
    def get_first_directory(self):
        return self.first_directory

    def get_second_level_folders(self):
        print('Getting first level folders...')
        return_array = []
        for root, dirs, files in os.walk(self.fpath + self.first_directory + '//', topdown=False):
            for name in dirs:
                return_array.append(name)
        return return_array

    def set_current_columns(self, columns):
        for col in columns:
            self.current_columns.append(col)
        self.dataframe = pd.read_csv(self.fpath + self.first_directory + '//' + self.second_directory + "//summary.csv", usecols=self.current_columns)
        print(self.dataframe)

    def get_current_columns(self):
        return self.current_columns

    def get_columns(self):
        df = pd.read_csv(self.fpath + self.first_directory + '//' + self.second_directory + "//summary.csv")
        print(df.columns.values.tolist())
        return df.columns.values.tolist()

    def get_start_idx(self):
        return self.start_idx
    def get_end_idx(self):
        return self.end_idx

    def set_start_idx(self, start_idx):
        self.start_idx = start_idx
    def set_end_idx(self, end_idx):
        self.end_idx = end_idx

    def increment_idx(self):
        self.start_idx = self.start_idx + self.step
        self.end_idx = self.end_idx - self.step
    def decrement_idx(self):
        self.start_idx = self.start_idx - self.step
        self.max = self.end_idx = self.end_idx + self.step

    def set_step(self, step):
        self.step = step

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time
    def get_fpath(self, fpath):
        if self.fpath is None:
            return None
        else:
            return self.fpath
    def set_fpath(self, fpath):
        self.fpath = fpath

    def get_dataframe(self):
        if self.dataframe is None:
            return None
        else:
            return self.dataframe

    def set_dataframe(self, dataframe):
        self.dataframe = dataframe