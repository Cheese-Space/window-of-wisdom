import tkinter as tk
from subprocess import getoutput
from os import name
from tkinter import messagebox
from tkinter import ttk
import argparse
def new_fortune():
    global outputer
    cow = getoutput(f"fortune | cowsay {'-f ' + outputer if outputer else ''}")
    wisdom.config(text=cow)
parser = argparse.ArgumentParser(description="a window displaying a fortune")
parser.add_argument("-w", "--skip_nt_error", help="skip windows error", action="store_true")
parser.add_argument("-t", "--tux", help="makes tux say a fortune", action="store_true")
parser.add_argument("-c", "--cow", help="makes a cow say a fortune", action="store_true")
args = parser.parse_args()
if args.tux:
    outputer = "tux"
elif args.cow:
    outputer = "default"
else:
    outputer = "stegosaurus"
if args.skip_nt_error:
   cow = getoutput(f"fortune | cowsay {'-f ' + outputer if outputer else ''}")
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
      check_cowsay = getoutput("which cowsay")
      check_fortune = getoutput("which fortune")
      if "which: no cowsay" in check_cowsay or not check_cowsay or "which: no fortune" in check_fortune or not check_fortune:
          messagebox.showerror("ERROR", "cowsay or fortune isn't installed, please install before using this program")
      else:
         cow = getoutput(f"fortune | cowsay {'-f ' + outputer if outputer else ''}")
         window = tk.Tk()
         wisdom = tk.Label(justify=tk.LEFT, text=cow, font=("Courier", 12))
         wisdom.pack()
         button = ttk.Button(text="new fortune", command=new_fortune)
         button.pack()
         window.resizable(False, False)
         window.title("window of wisdom")
         window.mainloop()


