from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import pymysql

my_pass = "Shrenik@713"
my_database = "football"
con = pymysql.connect(host="localhost", user="system", password=my_pass, database=my_database)

def serie_a():
    root = Tk()
    root.title("Serie A")
    root.geometry("1080x720")

    ser = con.cursor()
    ser.execute("select Abbrevaition, played, win, draw, loss, gd, points from ipl order by points desc,gd desc")
    sera = ttk.Treeview(root)
    sera['show'] = 'headings'

    x = ttk.Style(root)
    x.theme_use("default")

    sera["columns"] = ("Abbrevaition", "played", "win", "draw", "loss", "gd", "points")
    sera.column("Abbrevaition", width=150, minwidth=50, anchor=tk.CENTER)
    sera.column("played", width=150, minwidth=50, anchor=tk.CENTER)
    sera.column("win", width=150, minwidth=50, anchor=tk.CENTER)
    sera.column("draw", width=150, minwidth=50, anchor=tk.CENTER)
    sera.column("loss", width=150, minwidth=50, anchor=tk.CENTER)
    sera.column("gd", width=200, minwidth=100, anchor=tk.CENTER)
    sera.column("points", width=150, minwidth=50, anchor=tk.CENTER)
    sera.heading("Abbrevaition", text="Team", anchor=tk.CENTER)
    sera.heading("played", text="Played", anchor=tk.CENTER)
    sera.heading("win", text="Won", anchor=tk.CENTER)
    sera.heading("draw", text="Draw", anchor=tk.CENTER)
    sera.heading("loss", text="Loss", anchor=tk.CENTER)
    sera.heading("gd", text="Goal Difference", anchor=tk.CENTER)
    sera.heading("points", text="Points", anchor=tk.CENTER)

    i = 0
    for rows in ser:
        sera.insert('', i, text="", values=(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6]))
        i = i+1

    vsb = ttk.Scrollbar(root, orient="vertical")
    vsb.configure(command=sera.yview)
    sera.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    sera.pack(fill=BOTH, expand=1)

    root.mainloop()
