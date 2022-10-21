import Dataset
import DataEventHandler
from tkinter import *
import Dataset as ds
import pandas as pd
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

root = Tk()
lbl = Label(root, text="Enter filename: ")
txt = Entry(root, width=10)
mat_fig = Figure(figsize=(10, 5), dpi=100)
canvas = FigureCanvasTkAgg(mat_fig, master=root)

dataEventHandler = DataEventHandler

def load_data(fpath):
    print(fpath)
    dataEventHandler.set_dataset(fpath)
    visualize_data()

def visualize_data():
    mat_fig.clear()
    fig = dataEventHandler.get_graph_figure(mat_fig)
    canvas.draw_idle()





def load_data_clicked_event():
    fpath = txt.get()
    print(fpath)
    load_data("C:\\Users\\tromb\Downloads\\Dataset (1)\Dataset\\20200121\\312\\summary.csv")

def switch_time_clicked_event():
    dataEventHandler.switch_times()
    visualize_data()

def zoom_in_clicked_event():
    mat_fig.clear()
    fig = dataEventHandler.zoom_in(mat_fig)
    canvas.draw_idle()

def zoom_out_clicked_event():
    mat_fig.clear()
    fig = dataEventHandler.zoom_out(mat_fig)
    canvas.draw_idle()

def description_clicked_event():
    fpath = txt.get()

def sync_time_clicked_event():
    fpath = txt.get()

def query_clicked_event():
    fpath = txt.get()

def correlation_clicked_event():
    fpath = txt.get()
    cor = dataEventHandler.get_correlation()
    cor_lbl = Label(root, text=str(cor.round(3)))
    cor_lbl.grid(column=9, row=3)


def data_mining_clicked_event():
    fpath = txt.get()

def launch_user_interface():
    print('launching user interface')

    root.title("Welcome to VizApp")
    root.geometry('2000x2000')
    menu = Menu(root)
    item = Menu(menu)
    item.add_command(label='New')
    menu.add_cascade(label='File', menu=item)
    lbl.grid()
    txt.grid(column=1, row=0)
    btn = Button(root, text="Upload Dataset", fg="red", command=load_data_clicked_event)
    btn.grid(column=2, row=0)
    btn = Button(root, text="Switch Time", fg="blue", command=switch_time_clicked_event)
    btn.grid(column=3, row=0)
    btn = Button(root, text="Zoom Out", fg="green", command=zoom_out_clicked_event)
    btn.grid(column=4, row=0)
    btn = Button(root, text="Zoom In", fg="purple", command=zoom_in_clicked_event)
    btn.grid(column=5, row=0)
    btn = Button(root, text="Description", fg="orange", command=description_clicked_event)
    btn.grid(column=6, row=0)
    btn = Button(root, text="Sync Time", fg="black", command=sync_time_clicked_event)
    btn.grid(column=7, row=0)
    btn = Button(root, text="Query", fg="lime", command=query_clicked_event)
    btn.grid(column=8, row=0)
    btn = Button(root, text="Correlation", fg="navy", command=correlation_clicked_event)
    btn.grid(column=9, row=0)
    btn = Button(root, text="Data Mining", fg="brown", command=data_mining_clicked_event)
    btn.grid(column=10, row=0)

    # creating the Tkinter canvas
    # containing the Matplotlib figure

    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(column=2, row=10, columnspan=10)


    root.mainloop()