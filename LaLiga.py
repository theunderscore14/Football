from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import pymysql

my_pass = "Shrenik@713"
my_database = "football"
con = pymysql.connect(host="localhost", user="system", password=my_pass, database=my_database)

def laliga():
    root = Tk()
    root.title("LaLiga")
    root.geometry("1080x720")

    lal = con.cursor()
    lal.execute("select Abbrevaition, played, win, draw, loss, gd, points from spl order by points desc,gd desc")
    lali = ttk.Treeview(root)
    lali['show'] = 'headings'

    x = ttk.Style(root)
    x.theme_use("default")

    lali["columns"] = ("Abbrevaition", "played", "win", "draw", "loss", "gd", "points")
    lali.column("Abbrevaition", width=150, minwidth=50, anchor=tk.CENTER)
    lali.column("played", width=150, minwidth=50, anchor=tk.CENTER)
    lali.column("win", width=150, minwidth=50, anchor=tk.CENTER)
    lali.column("draw", width=150, minwidth=50, anchor=tk.CENTER)
    lali.column("loss", width=150, minwidth=50, anchor=tk.CENTER)
    lali.column("gd", width=200, minwidth=100, anchor=tk.CENTER)
    lali.column("points", width=150, minwidth=50, anchor=tk.CENTER)
    lali.heading("Abbrevaition", text="Team", anchor=tk.CENTER)
    lali.heading("played", text="Played", anchor=tk.CENTER)
    lali.heading("win", text="Won", anchor=tk.CENTER)
    lali.heading("draw", text="Draw", anchor=tk.CENTER)
    lali.heading("loss", text="Loss", anchor=tk.CENTER)
    lali.heading("gd", text="Goal Difference", anchor=tk.CENTER)
    lali.heading("points", text="Points", anchor=tk.CENTER)

    i = 0
    for rows in lal:
        lali.insert('', i, text="", values=(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6]))
        i = i + 1

    vsb = ttk.Scrollbar(root, orient="vertical")
    vsb.configure(command=lali.yview)
    lali.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    lali.pack(fill=BOTH, expand=1)

    root.mainloop()
