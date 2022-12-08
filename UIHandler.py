import numpy as np
from DataEventHandler import DataEventHandler
import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt

class UIHandler(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.dataEventHandler = DataEventHandler()
        self.columns = []
        print('launching user interface')

        self.title("Scientia")
        self.geometry('1200x1200')

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)

        self.frame1 = ttk.Frame(self.notebook, width=2000, height=2000)
        self.frame2 = ttk.Frame(self.notebook, width=2000, height=2000)
        self.frame3 = ttk.Frame(self.notebook, width=2000, height=2000)
        self.frame4 = ttk.Frame(self.notebook, width=2000, height=2000)
        self.frame5 = ttk.Frame(self.notebook, width=2000, height=2000)
        #self.frame6 = ttk.Frame(self.notebook, width=1200, height=1200)
        self.frame7 = ttk.Frame(self.notebook, width=2000, height=2000)

        self.frame1.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)
        self.frame3.pack(fill='both', expand=True)
        self.frame4.pack(fill='both', expand=True)
        self.frame5.pack(fill='both', expand=True)
        #self.frame6.pack(fill='both', expand=True)
        self.frame7.pack(fill='both', expand=True)

        self.container = self.frame3
        self.canvas = tk.Canvas(self.container)
        self.scrollbar = ttk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.container.pack()
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.notebook.add(self.frame1, text='Data Builder')
        self.notebook.add(self.frame2, text='Choose Variables')
        self.notebook.add(self.frame3, text='Plot(s)')
        self.notebook.add(self.frame4, text='Data Description')
        self.notebook.add(self.frame5, text='Correlation')
        #self.notebook.add(self.frame6, text='Visual Mining')
        self.notebook.add(self.frame7, text='Time Settings')

        self.fpath_label = ttk.Label(self.frame1, text="Enter file name:")
        self.fpath_label.pack()
        self.fpath_field = ttk.Entry(self.frame1, width=75)
        self.fpath_field.pack()
        self.fpath_upload_button = ttk.Button(self.frame1, text="Import File", command=self.load_fpath_clicked_event)
        self.fpath_upload_button.pack()
        self.list_box_participants = Listbox(self.frame1, width=40, height=10, selectmode=MULTIPLE)
        self.list_box_participants.pack()
        self.participants_upload_button = ttk.Button(self.frame1, text="Import Dataset", command=self.load_participants_clicked_event)
        self.participants_upload_button.pack()
        self.list_box_dates = Listbox(self.frame1, width=40, height=10, selectmode=MULTIPLE)
        self.list_box_dates.pack()
        self.data_upload_button = ttk.Button(self.frame1, text="Import Dataset", command=self.load_data_clicked_event)
        self.data_upload_button.pack()
        self.reset_data_button = ttk.Button(self.frame1, text="Reset All", command=None)
        self.reset_data_button.pack()
        self.error_label = ttk.Label(self.frame1, text="Error:")
        self.error_label.pack()

        self.list_box_available_columns = Listbox(self.frame2, width=40, height=10, selectmode=MULTIPLE)
        self.list_box_available_columns.pack()
        self.columns_add_button = ttk.Button(self.frame2, text="Add Column(s)", command=self.add_column_clicked_event)
        self.columns_add_button.pack()
        self.list_box_columns_added = Listbox(self.frame2, width=40, height=10, selectmode=MULTIPLE)
        self.list_box_columns_added.pack()
        self.columns_remove_button = ttk.Button(self.frame2, text="Delete Column(s)", command=None)
        self.columns_remove_button.pack()
        self.graph_data_button = ttk.Button(self.frame2, text="Graph Data", command=self.graph_data_clicked_event)
        self.graph_data_button.pack()
        self.error_label_columns = ttk.Label(self.frame2, text="Error:")
        self.error_label_columns.pack()

        self.time_text_label = ttk.Label(self.frame7, text="Current Time Format:")
        self.time_text_label.pack()
        self.time_label = ttk.Label(self.frame7, text="UTC")
        self.time_label.pack()
        self.switch_time_button = ttk.Button(self.frame7, text="Switch Time Format", command=self.switch_time)
        self.switch_time_button.pack()
        self.sync_time_button = ttk.Button(self.frame7, text="Sync Time Across Plots ", command=self.sync_time)
        self.sync_time_button.pack()

        self.variable = StringVar(self.frame4)
        self.variable.set("Select Data")  # default value
        self.description_option_menu = None
        self.description_button = None
        self.description_label = None
        self.corr_value_label = None



        self.color_id = 0
        self.color_array = ['b', 'g', 'r', 'c', 'm','k']

    def switch_time(self):
        self.dataEventHandler.switch_time()
        self.replot()
        self.time_label.config(text=self.dataEventHandler.get_time())

    def sync_time(self):
        self.replot()

    def self_description_button_clicked_event(self):

        df = self.dataEventHandler.get_dataset()
        start = self.agg_entry_one.get()
        end = self.agg_entry_two.get()

        if str(start) != "" and str(end) != "":
            data = self.dataEventHandler.get_statistics_for_data(self.variable.get(), df[(df['Datetime (UTC)'] > start) & (df['Datetime (UTC)'] < end)])
        else:
            data = self.dataEventHandler.get_statistics_for_data(self.variable.get(), df)

        text_str = "Data description for: " + str(self.variable.get()) + "\n" + "Mean: " + str(data['mean']) \
                   + "\n" + "Std dev: " + str(data["std"]) + "\n" + "Variance: " + str(data["variance"]) + "\n" \
                   + "Median: " + str(data["median"])

        self.description_label.config(text=text_str)


    def self_correlation_button_clicked_event(self):
        df = self.dataEventHandler.get_dataset()
        cor = df[self.correlation_option_menu.get(0)].corr(df[self.correlation_option_menu.get(1)])
        self.corr_value_label = ttk.Label(self.frame5, text=str(cor))
        self.corr_value_label.pack()

    def replot(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        df = self.dataEventHandler.get_dataset()
        for col in self.columns:
            if col != 'Datetime (UTC)' and col != 'Unix Timestamp (UTC)' and col != 'Timezone (minutes)':
                y = df[str(col)]
                if self.dataEventHandler.get_time() == 'UTC':
                    x = df['Datetime (UTC)']
                else:
                    x = pd.to_datetime(df['Datetime (UTC)']).dt.tz_convert('US/Eastern')
                fig = plt.figure(figsize=(8, 3))
                plt.plot_date(pd.to_datetime(x), y, '-', color=self.color_array[self.color_id%6])
                self.color_id += 1
                canvas = FigureCanvasTkAgg(fig, master=self.scrollable_frame)
                toolbarFrame = tk.Frame(self.scrollable_frame)
                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                canvas.draw()
                canvas.get_tk_widget().pack()
                toolbarFrame.pack()

    def graph_data_clicked_event(self):
        self.dataEventHandler.set_current_columns(self.columns)
        self.description_option_menu = OptionMenu(self.frame4, self.variable, *self.columns)
        self.description_option_menu.pack()
        self.correlation_option_menu = Listbox(self.frame5, width=40, height=10, selectmode=MULTIPLE)

        counter = 0

        for col in self.columns:
            self.correlation_option_menu.insert(counter, col)
            counter = counter + 1

        self.correlation_option_menu.pack()
        self.correlation_button = ttk.Button(self.frame5, text="Get Correlation", command=self.self_correlation_button_clicked_event)
        self.correlation_button.pack()
        self.description_label_agg = ttk.Label(self.frame4, text="Aggregate by date: (Enter in form yyyy-mm-dd until yyyy-mm-dd)")
        self.description_label_agg.pack()
        self.agg_entry_one = ttk.Entry(self.frame4, width=10)
        self.agg_entry_one.pack()
        self.description_label_hyp = ttk.Label(self.frame4, text="until")
        self.description_label_hyp.pack()
        self.agg_entry_two =  ttk.Entry(self.frame4, width=10)
        self.agg_entry_two.pack()
        self.description_button = ttk.Button(self.frame4, text="Get Description", command=self.self_description_button_clicked_event)
        self.description_button.pack()
        self.description_label = ttk.Label(self.frame4, text="")
        self.description_label.pack()

        df = self.dataEventHandler.get_dataset()

        for col in self.columns:
            if col != 'Datetime (UTC)' and col != 'Unix Timestamp (UTC)' and col != 'Timezone (minutes)':
                y = df[str(col)]
                x = df['Datetime (UTC)']
                fig = plt.figure(figsize=(8, 3))
                plt.plot_date(pd.to_datetime(x), y, '-', color=self.color_array[self.color_id%6])
                self.color_id += 1
                canvas = FigureCanvasTkAgg(fig, master=self.scrollable_frame)
                toolbarFrame = tk.Frame(self.scrollable_frame)
                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                canvas.draw()
                canvas.get_tk_widget().pack()
                toolbarFrame.pack()

    def add_column_clicked_event(self):
        self.columns = []
        for i in self.list_box_available_columns.curselection():
            self.columns.append(self.list_box_available_columns.get(i))

        counter = 0
        for item in self.columns:
            self.list_box_columns_added.insert(counter, str(item))
            counter += 1

    def load_fpath_clicked_event(self):
        fpath = self.fpath_field.get()
        self.dataEventHandler.set_dataset(fpath)
        first_level_folders = self.dataEventHandler.get_first_level_folders()
        counter = 0
        for folder in first_level_folders:
            self.list_box_participants.insert(counter, str(folder))
            counter += 1

    def load_participants_clicked_event(self):
        clicked_items = []
        for i in self.list_box_participants.curselection():
            clicked_items.append(self.list_box_participants.get(i))
        self.dataEventHandler.set_first_directory(clicked_items[0])
        second_level_folders = self.dataEventHandler.get_second_level_folders()
        counter = 0
        for folder in second_level_folders:
            self.list_box_dates.insert(counter, str(folder))
            counter += 1

    def load_data_clicked_event(self):
        clicked_items = []
        for i in self.list_box_dates.curselection():
            clicked_items.append(self.list_box_dates.get(i))
        self.dataEventHandler.set_second_directory(clicked_items[0])
        self.load_data()

    def load_data(self):
        self.populate_columns()

    def populate_columns(self):
        columns = self.dataEventHandler.get_columns()
        counter = 0
        for col in columns:
            self.list_box_available_columns.insert(counter, str(col))
            counter += 1
