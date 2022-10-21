import pandas as pd


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
        try:
            self.dataframe = pd.read_csv(fpath)
            self.end_idx = len(self.dataframe['Datetime (UTC)'])
        except:
            print("Exception loading fpath as dataframe")
            self.dataframe = None

    def get_dataframe(self):
        if self.dataframe is None:
            return None
        else:
            return self.dataframe

    def set_dataframe(self, dataframe):
        self.dataframe = dataframe