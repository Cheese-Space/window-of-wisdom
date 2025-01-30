import tkinter as tk
from subprocess import getoutput
from os import name
from tkinter import messagebox
if name == "nt":
    messagebox.showerror("ERROR", "ERROR: this program doesn't support windows")
else:
   check_cowsay = getoutput("which cowsay")
   check_fortune = getoutput("which fortune")
   if "which: no cowsay" in check_cowsay or not check_cowsay or "which: no fortune" in check_fortune or not check_fortune:
       messagebox.showerror("ERROR", "ERROR: cowsay or fortune isn't installed, please install before using!")
   else:
      cow = getoutput("fortune | cowsay -f stegosaurus")
      window = tk.Tk()
      wisdom = tk.Label(justify=tk.LEFT, text=cow, font=("Courier", 12))
      wisdom.pack()
      window.config(bg="black")
      window.resizable(False, False)
      window.title("window of wisdom")
      window.mainloop()
