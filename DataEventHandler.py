from Dataset import Dataset
import numpy as np

class DataEventHandler:
    def __init__(self):
        self.dataset = Dataset()

    def get_dataset(self):
        return self.dataset.get_dataframe()

    def switch_time(self):
        self.dataset.switch_time()

    def set_dataset(self, fpath):
        self.dataset.set_fpath(fpath)
        print(self.dataset)

    def get_first_level_folders(self):
        return self.dataset.get_first_level_folders()

    def get_time(self):
        return self.dataset.get_time()

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

    def set_current_columns(self, columns):
        self.dataset.set_current_columns(columns)

    def get_statistics_for_data(self, data):
        statistics_dic = {}
        df = self.dataset.get_dataframe()
        for i in df:
            if i == data:
                statistics_dic["mean"] = np.mean(np.array(df[i]))
                statistics_dic["std"] = np.std(np.array(df[i]))

        return statistics_dic