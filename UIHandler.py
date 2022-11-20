import Dataset
from DataEventHandler import DataEventHandler
import tkinter as tk
from tkinter import ttk
from tkinter import *
import Dataset as ds
import pandas as pd
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt

class UIHandler(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.dataEventHandler = DataEventHandler()
        self.columns = []
        print('launching user interface')

        self.title("VizApp")
        self.geometry('800x1000')

        # create a notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True)

        # create frames
        self.frame1 = ttk.Frame(self.notebook, width=1200, height=1200)
        self.frame2 = ttk.Frame(self.notebook, width=1200, height=1200)
        self.frame3 = ttk.Frame(self.notebook, width=1200, height=1200)
        self.frame4 = ttk.Frame(self.notebook, width=1200, height=1200)
        self.frame5 = ttk.Frame(self.notebook, width=1200, height=1200)
        self.frame6 = ttk.Frame(self.notebook, width=1200, height=1200)

        self.frame1.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)
        self.frame3.pack(fill='both', expand=True)
        self.frame4.pack(fill='both', expand=True)
        self.frame5.pack(fill='both', expand=True)
        self.frame6.pack(fill='both', expand=True)

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

        # add frames to notebook

        self.notebook.add(self.frame1, text='Import file')
        self.notebook.add(self.frame2, text='Choose Data')
        self.notebook.add(self.frame3, text='Plot')
        self.notebook.add(self.frame4, text='Description')
        self.notebook.add(self.frame5, text='Correlation')
        self.notebook.add(self.frame6, text='Visual Mining')

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
        self.error_label = ttk.Label(self.frame1, text="Error:")
        self.error_label.pack()

        self.list_box_available_columns = Listbox(self.frame2, width=40, height=10, selectmode=MULTIPLE)
        self.list_box_available_columns.pack()
        self.columns_add_button = ttk.Button(self.frame2, text="Add Column(s)", command=self.add_column_clicked_event)
        self.columns_add_button.pack()
        self.list_box_columns_added = Listbox(self.frame2, width=40, height=10, selectmode=MULTIPLE)
        self.list_box_columns_added.pack()
        self.columns_remove_button = ttk.Button(self.frame2, text="Delete Column(s)", command=self.import_columns_clicked_event)
        self.columns_remove_button.pack()
        self.graph_data_button = ttk.Button(self.frame2, text="Graph Data", command=self.graph_data_clicked_event)
        self.graph_data_button.pack()
        self.error_label_columns = ttk.Label(self.frame2, text="Error:")
        self.error_label_columns.pack()

        self.color_id = 0
        self.color_array = ['b', 'g', 'r', 'c', 'm','k']

    def graph_data_clicked_event(self):
        print('graphing')
        self.dataEventHandler.set_current_columns(self.columns)

        df = self.dataEventHandler.get_dataset()

        for col in self.columns:
            if col != 'Datetime (UTC)' and col != 'Unix Timestamp (UTC)' and col != 'Timezone (minutes)':
                print(col)

                y = df[str(col)]
                x = df['Datetime (UTC)']
                print('plotting following values')
                print(x)
                print('----------------------')
                print(y)

                fig = plt.figure(figsize=(8, 3))
                plt.plot_date(pd.to_datetime(x), y, '-', color=self.color_array[self.color_id%6])
                self.color_id += 1

                # specify the window as master
                canvas = FigureCanvasTkAgg(fig, master=self.scrollable_frame)


                # navigation toolbar
                toolbarFrame = tk.Frame(self.scrollable_frame)
                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                canvas.draw()
                canvas.get_tk_widget().pack()
                toolbarFrame.pack()

    def add_column_clicked_event(self):
        self.columns = []
        for i in self.list_box_available_columns.curselection():
            print(self.list_box_available_columns.get(i))
            self.columns.append(self.list_box_available_columns.get(i))

        counter = 0
        for item in self.columns:
            self.list_box_columns_added.insert(counter, str(item))
            counter += 1

    def import_columns_clicked_event(self):
        print('hey')

    def load_fpath_clicked_event(self):
        print("clicked")
        fpath = self.fpath_field.get()
        print(fpath)
        self.dataEventHandler.set_dataset("C:\\Users\\tromb\Downloads\\Dataset (1)\Dataset\\")
        first_level_folders = self.dataEventHandler.get_first_level_folders()
        counter = 0
        for folder in first_level_folders:
            self.list_box_participants.insert(counter, str(folder))
            counter += 1

    def load_participants_clicked_event(self):
        print('loading')
        clicked_items = []
        for i in self.list_box_participants.curselection():
            print(self.list_box_participants.get(i))
            clicked_items.append(self.list_box_participants.get(i))
        self.dataEventHandler.set_first_directory(clicked_items[0])
        second_level_folders = self.dataEventHandler.get_second_level_folders()
        counter = 0
        for folder in second_level_folders:
            self.list_box_dates.insert(counter, str(folder))
            counter += 1

    def load_data_clicked_event(self):
        print('Graphing data...')
        clicked_items = []
        for i in self.list_box_dates.curselection():
            print(self.list_box_dates.get(i))
            clicked_items.append(self.list_box_dates.get(i))
        self.dataEventHandler.set_second_directory(clicked_items[0])
        self.load_data()

    def load_data(self):
        print('loading data')
        self.populate_columns()
        ##select columns
        ##data loaded in
        ##graph data with widget




    def populate_columns(self):
        columns = self.dataEventHandler.get_columns()
        counter = 0
        for col in columns:
            self.list_box_available_columns.insert(counter, str(col))
            counter += 1

