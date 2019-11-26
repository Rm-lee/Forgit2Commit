from tkinter import filedialog
from tkinter import *
from tkinter import WORD
import watcher


def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

def repo_path_button():
    global output
    global branch_name
    branch_name.set(entr.get())
    output.set("watching: " + folder_path.get() + " in branch (" + branch_name.get() + ") for changes.")
    watcher.repo_path = path_entry.get()
    watcher.branch = entr.get()
    watcher.strt().set_repo_path()
    
    # labelWatch.set("watching {} for file changes.".format(os.path.abspath(watcher.repo_path)))  

if __name__ == '__main__':  

    root = Tk()
    root.title("ForGit2 Commit")
    root.geometry("400x200+500+500")
    root.grid_columnconfigure(3, minsize=300)
    root.grid_columnconfigure(1, minsize=300)
    root.grid_rowconfigure(1, minsize=100)
    branch_name = StringVar()
    folder_path = StringVar()
    output = StringVar()
    path_entry = Entry(master=root,textvariable=folder_path)
    path_entry.grid(row=1, column=1,columnspan=2,sticky=W)
    repobtn = Button(text="Pick Repo", bg="lightgreen", command=browse_button)
    button1 = Button(text="Watch", command=repo_path_button)
    entr = Entry(root, text="branch")
    entr.grid(row=3,column=1,columnspan=2, sticky=W)
    repobtn.grid(row=1, column=2,  sticky=E,pady=5)
    button1.grid(row=3, column=2, sticky=E)
    lbWatching = Label(textvariable=output ,fg="green",wraplength=300)
    lbWatching.grid(row=4, column=1,columnspan=6,sticky=W)
    mainloop()


                     





# import freesia
# from freesia import *
# 



#   
#     root = Window(title="Repo Watcher", bg="#F5F5F5")
#     root.geometry(500,200)
#     label = Label(root, text="Path to repo" ,font="helvetica 16 ")
#     labelPath = Label(root, text="e.g. ~/home/<user>/Projs/project1" ,font="helvetica 10",fg="#369636")
#     entr = Entry(root, text="",fg="black", bg="lightgrey")
#     entr.place(0.05, 0.3, anchor="W")
#     label.place(0.05, 0.1, anchor="W")
#     labelPath.place(0.41, 0.3, anchor="W") 
#     labelWatch = Label(root, text="" ,font="helvetica 10 ",fg="#369636")
#     labelWatch.place(0.05, 0.9, anchor="W")
#     label2 = Label(root, text="branch" ,font="helvetica 16 ",fg="black")
#     entr2 = Entry(root, text="master",bg="lightgrey",fg="black")
#     entr2.place(0.05, 0.7, anchor="W")
#     label2.place(0.05, 0.5, anchor="W")
#     widget2 = Button(root, text="Watch",fg="black",bg="lightgrey")
#     widget2.bind("<Button-1>",repo_path_button)
#     widget2.place(0.9, 0.6,anchor="E")
#     mainloop()
