import tkinter as tk
from subprocess import getoutput
from os import name, system
from tkinter import messagebox, TclError, ttk
import pyperclip
outputer = "cowsay -f stegosaurus"
def tux():
    global cow
    global win2
    global outputer
    cow = getoutput("PATH='/opt/homebrew/bin:/usr/bin:/usr/local/bin:/bin'; fortune | cowsay -f tux")
    wisdom.config(text=cow)
    outputer = "cowsay -f tux"
    win2.destroy()
def cowsay():
    global outputer
    global win2
    global cow
    cow = getoutput("PATH='/opt/homebrew/bin:/usr/bin:/usr/local/bin:/bin'; fortune | cowsay")
    wisdom.config(text=cow)
    outputer = "cowsay"
    win2.destroy()
def moose():
    global cow
    global win2
    global outputer
    cow = getoutput("PATH='/opt/homebrew/bin:/usr/bin:/bin:/usr/local/bin'; fortune | cowsay -f moose")
    wisdom.config(text=cow)
    outputer = "cowsay -f moose"
    win2.destroy()
def dragon():
    global win2
    global outputer
    global cow
    cow = getoutput("PATH='/opt/homebrew/bin:/usr/bin:/bin:/usr/local/bin'; fortune | cowsay -f dragon")
    wisdom.config(text=cow)
    outputer = "cowsay -f dragon"
    win2.destroy()
def stegosaurus():
    global win2
    global outputer
    global cow
    cow = getoutput("PATH='/opt/homebrew/bin:/usr/bin:/bin:/usr/local/bin'; fortune | cowsay -f stegosaurus")
    wisdom.config(text=cow)
    outputer = "cowsay -f stegosaurus"
    win2.destroy()
def new_fortune_teller(arg):
    try:
       global win2
       if win2.winfo_exists() == 1:
           return
    except (NameError, TclError):
       win2 = tk.Tk()
       win2.resizable(False, False)
       label = ttk.Label(win2, text="select a new fortune teller:")
       label.pack()
       tb = ttk.Button(win2, text="tux", command=tux)
       tb.pack()
       cb = ttk.Button(win2, text="cow", command = cowsay)
       cb.pack()
       mb = ttk.Button(win2, text="moose", command=moose)
       mb.pack()
       db = ttk.Button(win2, text="dragon", command = dragon)
       sb = ttk.Button(win2, text="stegosaurus", command=stegosaurus)
       db.pack()
       sb.pack()
       win2.title('different fortune teller')
       win2.mainloop()
def new_fortune():
    global command
    global outputer
    global cow
    command = "PATH='/opt/homebrew/bin:/usr/bin:/bin:/usr/local/bin'; fortune | "+outputer
    cow = getoutput(command)
    wisdom.config(text=cow)
def copy(arg):
    global cow
    if not cow:
        return
    pyperclip.copy(cow)
if name == "nt":
   messagebox.showerror("ERROR", "ERROR: this program doens't support windows!")
else:
   check_cowsay = system("PATH='/opt/homebrew/bin:/usr/bin:/bin:/usr/local/bin'; which cowsay > /dev/null")
   check_fortune = system("PATH='/usr/bin:/bin:/opt/homebrew/bin:/usr/local/bin'; which fortune > /dev/null")
   if check_cowsay == 256 or check_fortune == 256:
      messagebox.showerror("ERROR", "cowsay or fortune isn't installed, please install before using this program")
   else:
       command = "PATH='/opt/homebrew/bin:/usr/bin:/bin:/usr/local/bin'; fortune | " + outputer
       cow = getoutput(command)
       window = tk.Tk()
       wisdom = tk.Label(justify=tk.LEFT, text=cow, font=("Courier", 12))
       wisdom.pack()
       window.bind("<KeyPress-d>", new_fortune_teller)
       window.bind("<KeyPress-c>", copy)
       button = ttk.Button(text="new fortune", command=new_fortune)
       button.pack()
       window.resizable(False, False)
       window.title("window of wisdom")
       window.mainloop()
