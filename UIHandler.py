import Dataset
import DataEventHandler
from tkinter import *

root = Tk()
lbl = Label(root, text="Enter filename: ")
txt = Entry(root, width=10)

dataset = Dataset()
dataEventHandler = DataEventHandler
dataEventHandler.set_dataset(dataset)

def load_data(fpath):
    print(fpath)
    dataset.set_fpath(fpath)
    dataEventHandler.update_dataset(dataset)


def button_clicked_event():
    fpath = txt.get()
    print(fpath)
    load_data(fpath)

def launch_user_interface():
    print('launching user interface')

    root.title("Welcome to VizApp")
    root.geometry('350x200')
    menu = Menu(root)
    item = Menu(menu)
    item.add_command(label='New')
    menu.add_cascade(label='File', menu=item)
    root.config(menu=menu)
    lbl.grid()
    txt.grid(column=1, row=0)
    btn = Button(root, text="Upload", fg="red", command=button_clicked_event)
    btn.grid(column=2, row=0)
    root.mainloop()