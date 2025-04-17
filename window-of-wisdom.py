


import tkinter as tk
from subprocess import getoutput
from os import name
from tkinter import messagebox
from tkinter import ttk
import argparse
def tux():
    global win2
    global outputer
    cow = getoutput("PATH='/opt/homebrew/bin:/usr/bin:/bin'; fortune | cowsay -f tux")
    wisdom.config(text=cow)
    outputer = "cowsay -f tux"
    win2.destroy()
def cowsay():
    global outputer
    global win2
    cow = getoutput("PATH='/opt/homebrew/bin:/usr/bin:/bin'; fortune | cowsay")
    wisdom.config(text=cow)
    outputer = "cowsay"
    win2.destroy()
def moose():
    cow = getoutput("PATH='/opt/homebrew/bin:/usr/bin:/bin'; fortune | cowsay -f moose")
    global win2
    global outputer
    wisdom.config(text=cow)
    outputer = "cowsay -f moose"
    win2.destroy()
def dragon():
    global win2
    global outputer
    cow = getoutput("PATH='/opt/homebrew/bin:/usr/bin:/bin'; fortune | cowsay -f dragon")
    wisdom.config(text=cow)
    outputer = "cowsay -f dragon"
    win2.destroy()
def stegosaurus():
    global win2
    global outputer
    cow = getoutput("PATH='/opt/homebrew/bin:/usr/bin:/bin'; fortune | cowsay -f stegosaurus")
    wisdom.config(text=cow)
    outputer = "cowsay -f stegosaurus"
    win2.destroy()
def new_fortune_teller():
    global win2
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
    command = "PATH='/opt/homebrew/bin:/usr/bin:/bin'; fortune | "+outputer
    cow = getoutput(command)
    wisdom.config(text=cow)
parser = argparse.ArgumentParser(description="a window displaying a fortune")
parser.add_argument("-w", "--skip_nt_error", help="skip windows error", action="store_true")
parser.add_argument("-t", "--tux", help="makes tux say a fortune", action="store_true")
parser.add_argument("-c", "--cow", help="makes a cow say a fortune", action="store_true")
parser.add_argument("-m", "--moose", help="makes a moose say a fortune", action="store_true")
parser.add_argument("-d", "--dragon", help="makes a dragon say a fortune", action="store_true")
args = parser.parse_args()
if args.tux:
    outputer = "cowsay -f tux"
elif args.cow:
    outputer = "cowsay"
elif args.moose:
    outputer = "cowsay -f moose"
elif args.dragon:
    outputer = "cowsay -f dragon"
else:
    outputer = "cowsay -f stegosaurus"
if args.skip_nt_error:
   command = "/bin/zsh fortune | " + outputer
   cow = getoutput(command)
   window = tk.Tk()
   wisdom = tk.Label(justify=tk.LEFT, text=cow, font=("Courier", 12))
   wisdom.pack()
   button = tk.Button(text="new fortune", command=new_fortune)
   button.pack()
   window.title('window of wisdom')
   window.resizable(False, False)
   window.mainloop()
else:
   if name == "nt":
       messagebox.showerror("ERROR", "ERROR: this program doens't support windows!")
   else:
       check_cowsay = getoutput("PATH='/opt/homebrew/bin:/usr/bin:/bin'; which cowsay")
       check_fortune = getoutput("PATH='/opt/homebrew/bin:/usr/bin:/bin'; /which fortune")
       if "which: no cowsay" in check_cowsay or not check_cowsay or "which: no fortune" in check_fortune or not check_fortune:
         messagebox.showerror("ERROR", "cowsay or fortune isn't installed, please install before using this program")
       else:
         command = "PATH='/opt/homebrew/bin:/usr/bin:/bin'; fortune | " + outputer
         cow = getoutput(command)
         window = tk.Tk()
         wisdom = tk.Label(justify=tk.LEFT, text=cow, font=("Courier", 12))
         wisdom.pack()
         button = ttk.Button(text="new fortune", command=new_fortune)
         button.pack()
         button2 = ttk.Button(text="diferent fortune teller", command=new_fortune_teller)
         button2.pack()
         window.resizable(False, False)
         window.title("window of wisdom")
         window.mainloop()
