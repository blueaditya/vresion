from tkinter import *
import os
import tkinter
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import shutil


def open_file():
    file = fd.askopenfilename(title='Choose a file of any type', filetypes=[
                              ("All files", "*.*")])

    os.startfile(os.path.abspath(file))


def delete_file():
    file = fd.askopenfilename(title='Choose a file to delete', filetypes=[
                              ("All files", "*.*")])

    os.remove(os.path.abspath(file))

    mb.showinfo(title='File Deleted',
                message='Your desired file has been deleted')


def copy_file():
    file_to_copy = fd.askopenfilename(
        title='Choose a file to copy', filetypes=[("All files", "*.*")])
    dir_to_copy_to = fd.askdirectory(title='In which folder to copy to?')

    try:
        shutil.copy(file_to_copy, dir_to_copy_to)
        mb.showinfo(
            title='File copied!', message='your file has been copied to your desired location')
    except:
        mb.showerror(
            title='Error!', message='We were unable to copy your file to the desired location. Please try again')


def open_folder():
    folder = fd.askdirectory(title='Select Folder to open')
    os.startfile(folder)


def delete_folder():
    folder_to_delete = fd.askdirectory(title='Choose the folder to delete')
    os.rmdir(folder_to_delete)
    mb.showinfo("Folder Deleted", "Your desited folder has been deleted.")


def move_folder():
    folder_to_move = fd.askdirectory(
        title='Choose the folder you want to copy.')
    mb.showinfo(message='You just selected the folder you want to move, now please select the destination where you want to move the folder to')
    destination = fd.askdirectory(title="Where to move the folder to")

    try:
        shutil.move(folder_to_move, destination)
        mb.showinfo(
            "Folder moved", 'Your desired folder has veen moved to the location you wanted')

    except:
        mb.showerror('Error', 'We could not move your folder')


def list_files_in_folder():

    folder = fd.askdirectory(
        title='Select the folder whose files you want to list')

    files = os.listdir(os.path.abspath(folder))

    # list_files_wn = Toplevel(root)
    # list_files_wn.title(f'Files in {folder}')
    # list_files_wn.geometry('250x250')
    # list_files_wn.resizable(0, 0)


def rename_file():

    file = fd.askopenfilename(title='Choose a file to rename', filetypes=[
                              ("All files", "*.*")])


# Initalizing Variable for Tkinter
title = 'Blueaditya File Manager'
background = 'Purple'

button_font = ("Times New Roman", 13)
button_background = "Turquoise"

# Initalizing the Tkinter window


root = Tk()
root.title(title)
root.geometry('250x400')
root.resizable(0, 0)
root.config(bg=background)

# Creating and placing the components in the window
Label(root, text=title, font=("Comic Sans MS", 15),
      bg=background, wraplength=250).place(x=20, y=0)
Button(root, text='Open a file', width=20, font=button_font,
       bg=button_background, command=open_file).place(x=30, y=50)
Button(root, text='Copy a file', width=20, font=button_font,
       bg=button_background, command=copy_file).place(x=30, y=90)
Button(root, text='Rename a file', width=20, font=button_font,
       bg=button_background, command=rename_file).place(x=30, y=130)
Button(root, text='Delete a file', width=20, font=button_font,
       bg=button_background, command=delete_file).place(x=30, y=170)
Button(root, text='Open a folder', width=20, font=button_font,
       bg=button_background, command=open_folder).place(x=30, y=210)
Button(root, text='Delete a folder', width=20, font=button_font,
       bg=button_background, command=delete_folder).place(x=30, y=250)
Button(root, text='Move a folder', width=20, font=button_font,
       bg=button_background, command=move_folder).place(x=30, y=290)
Button(root, text='List all files in a folder', width=20, font=button_font, bg=button_background,
       command=list_files_in_folder).place(x=30, y=330)
# Finalizing the window
root.update()
root.mainloop()
