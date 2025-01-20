import tkinter as tk
from subprocess import getoutput
from os import name

if name == "nt":
    error = tk.Tk()
    T2 = tk.Label(text="ERROR: this program doesn't support windows!")
    T2.pack()
    button = tk.Button(text="exit", command=error.destroy)
    button.pack()
    error.resizable(False, False)
    error.title("error!")
    error.mainloop()
else:
   check_cowsay = getoutput("which cowsay")
   check_fortune = getoutput("which fortune")
   if "which: no cowsay" in check_cowsay or not check_cowsay or "which: no fortune" in check_fortune or not check_fortune:
       error_window = tk.Tk()
       error_window.title("error!")
       T1 = tk.Label(text="ERROR: cowsay or fortune isn't installed, please install before using this program!")
       T1.pack()
       button = tk.Button(text="exit", command=error_window.destroy)
       button.pack()
       error_window.resizable(False, False)
       error_window.mainloop()
   else:
      cow = getoutput("fortune | cowsay -f stegosaurus")
      window = tk.Tk()
      wisdom = tk.Label(justify=tk.LEFT, text=cow, font=("Courier", 12))
      wisdom.pack()
      window.config(bg="black")
      window.resizable(False, False)
      window.title("window of wisdom")
      window.mainloop()
