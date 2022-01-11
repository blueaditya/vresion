from tkinter import *
import os
import tkinter
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import shutil


def open_file():
    file = fd.askopenfilename(title='Choose a file of any type', filetypes=[("All files", "*.*")]

    os.startfile(os.path.abspath(file))


def delete_file():
    file=fd.askopenfilename(title='Choose a file to delete', filetypes=[("All files", "*.*")]

    os.remove(os.path.abspath(file))

    mb.showinfo(title='File Deleted',
                message='Your desired file has been deleted')

def copy_file():
    file_to_copy=fd.askopenfilename(title='Choose a file to copy', filetypes=[("All files", "*.*")]
    dir_to_copy_to=fd.askdirectory(title='In which folder to copy to?')

    try:
        shutil.copy(file_to_copy, dir_to_copy_to)
        mb.showinfo(
            title='File copied!', message='your file has been copied to your desired location')
    except:
        mb.showerror(
            title='Error!', message='We were unable to copy your file to the desired location. Please try again')

def open_folder():
    folder=fd.askdirectory(title='Select Folder to open')
    os.startfile(folder)


def delete_folder():


def move_folder():


def list_file_in_folder():


def rename_file():
