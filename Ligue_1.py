from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import pymysql

my_pass = "Shrenik@713"
my_database = "football"
con = pymysql.connect(host="localhost", user="system", password=my_pass, database=my_database)

def ligue_1():
    root = Tk()
    root.title("Ligue 1")
    root.geometry("1080x720")

    lig = con.cursor()
    lig.execute("select Abbrevaition, played, win, draw, loss, gd, points from fpl order by points desc,gd desc")
    ligu = ttk.Treeview(root)
    ligu['show'] = 'headings'

    x = ttk.Style(root)
    x.theme_use("default")

    ligu["columns"] = ("Abbrevaition", "played", "win", "draw", "loss", "gd", "points")
    ligu.column("Abbrevaition", width=150, minwidth=50, anchor=tk.CENTER)
    ligu.column("played", width=150, minwidth=50, anchor=tk.CENTER)
    ligu.column("win", width=150, minwidth=50, anchor=tk.CENTER)
    ligu.column("draw", width=150, minwidth=50, anchor=tk.CENTER)
    ligu.column("loss", width=150, minwidth=50, anchor=tk.CENTER)
    ligu.column("gd", width=200, minwidth=100, anchor=tk.CENTER)
    ligu.column("points", width=150, minwidth=50, anchor=tk.CENTER)
    ligu.heading("Abbrevaition", text="Team", anchor=tk.CENTER)
    ligu.heading("played", text="Played", anchor=tk.CENTER)
    ligu.heading("win", text="Won", anchor=tk.CENTER)
    ligu.heading("draw", text="Draw", anchor=tk.CENTER)
    ligu.heading("loss", text="Loss", anchor=tk.CENTER)
    ligu.heading("gd", text="Goal Difference", anchor=tk.CENTER)
    ligu.heading("points", text="Points", anchor=tk.CENTER)

    i = 0
    for rows in lig:
        ligu.insert('', i, text="", values=(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6]))
        i = i + 1

    vsb = ttk.Scrollbar(root, orient="vertical")
    vsb.configure(command=ligu.yview)
    ligu.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    ligu.pack(fill=BOTH, expand=1)

    root.mainloop()
