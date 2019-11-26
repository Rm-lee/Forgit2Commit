from tkinter import filedialog
from tkinter import *
from tkinter import WORD
import watcher
import tkinter.font as tkFont

def browse_button():
    global folder_path  
    filename = filedialog.askdirectory()
    folder_path.set(filename)
   
def start_button():
    global output
    global branch_name
    branch_name.set(entr.get())
    output.set("watching: " + folder_path.get() + " in branch (" + branch_name.get() + ") for changes.")
    watcher.repo_path = folder_path.get()
    watcher.branch = entr.get()
    watcher.strt().set_repo_path()
    
    
if __name__ == '__main__':  
    root = Tk()
    root.title("ForGit2 Commit")
    root.geometry("400x200+500+500")
    root.grid_columnconfigure(3, minsize=150)
    root.grid_columnconfigure(1, minsize=150)
    root.grid_rowconfigure(1, minsize=100)
    root.configure(background='gray10')
    branch_name = StringVar()
    folder_path = StringVar()
    output = StringVar()
    path_entry = Entry(master=root,textvariable=folder_path,bg="gray25",fg="white")
    path_entry.grid(row=1, column=1,columnspan=2,sticky=W,padx=10)
    repobtn = Button(text="Browse", bg="gray25",fg="white", command=browse_button,font = "Helvetica 12 bold")
    button1 = Button(text="Watch", command=start_button,bg="gray25",fg="white",font = "Helvetica 12 bold")
    entr = Entry(root, text="branch",bg="gray25",fg="white")
    entr.grid(row=3,column=1,columnspan=2, sticky=W,padx=10)
    repobtn.grid(row=1, column=3,  sticky=W,padx=10)
    button1.grid(row=3, column=3, sticky=W,padx=10)
    lbWatching = Label(textvariable=output ,fg="green",bg="gray10",wraplength=300,font = "Helvetica 12 bold")
    lbWatching.grid(row=4, column=1,columnspan=6,sticky=W)
    lbDir = Label(text="Directory to watch" ,fg="green",bg="gray10",font = "Helvetica 10 bold")
    lbDir.grid(row=1, column=2,sticky=W)
    lbBranch = Label(text="Branch" ,fg="green",bg="gray10",font = "Helvetica 10 bold")
    lbBranch.grid(row=3, column=2,sticky=W)
    mainloop()
