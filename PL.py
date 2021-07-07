from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import pymysql

my_pass = "Shrenik@713"
my_database = "football"
con = pymysql.connect(host="localhost", user="system", password=my_pass, database=my_database)

def prem():
    root = Tk()
    root.title("PL")
    root.geometry("1080x720")

    pre = con.cursor()
    pre.execute("select Abbrevaition, played, win, draw, loss, gd, points from pl order by points desc,gd desc")
    preme = ttk.Treeview(root)
    preme['show'] = 'headings'

    x = ttk.Style(root)
    x.theme_use("default")

    preme["columns"] = ("Abbrevaition", "played", "win", "draw", "loss", "gd", "points")
    preme.column("Abbrevaition", width=150, minwidth=50, anchor=tk.CENTER)
    preme.column("played", width=150, minwidth=50, anchor=tk.CENTER)
    preme.column("win", width=150, minwidth=50, anchor=tk.CENTER)
    preme.column("draw", width=150, minwidth=50, anchor=tk.CENTER)
    preme.column("loss", width=150, minwidth=50, anchor=tk.CENTER)
    preme.column("gd", width=200, minwidth=100, anchor=tk.CENTER)
    preme.column("points", width=150, minwidth=50, anchor=tk.CENTER)
    preme.heading("Abbrevaition", text="Team", anchor=tk.CENTER)
    preme.heading("played", text="Played", anchor=tk.CENTER)
    preme.heading("win", text="Won", anchor=tk.CENTER)
    preme.heading("draw", text="Draw", anchor=tk.CENTER)
    preme.heading("loss", text="Loss", anchor=tk.CENTER)
    preme.heading("gd", text="Goal Difference", anchor=tk.CENTER)
    preme.heading("points", text="Points", anchor=tk.CENTER)

    i = 0
    for rows in pre:
        preme.insert('', i, text="", values=(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6]))
        i = i + 1

    vsb = ttk.Scrollbar(root, orient="vertical")
    vsb.configure(command=preme.yview)
    preme.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    preme.pack(fill=BOTH, expand=1)

    root.mainloop()
