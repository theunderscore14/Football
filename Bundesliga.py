from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import pymysql

my_pass = "Shrenik@713"
my_database = "football"
con = pymysql.connect(host="localhost", user="system", password=my_pass, database=my_database)

def bundesliga():
    root = Tk()
    root.title("Bundesliga")
    root.geometry("1080x720")

    bun = con.cursor()
    bun.execute("select Abbrevaition, played, win, draw, loss, gd, points from bpl order by points desc,gd desc")
    bund = ttk.Treeview(root)
    bund['show'] = 'headings'

    x = ttk.Style(root)
    x.theme_use("default")

    bund["columns"] = ("Abbrevaition", "played", "win", "draw", "loss", "gd", "points")
    bund.column("Abbrevaition", width=150, minwidth=50, anchor=tk.CENTER)
    bund.column("played", width=150, minwidth=50, anchor=tk.CENTER)
    bund.column("win", width=150, minwidth=50, anchor=tk.CENTER)
    bund.column("draw", width=150, minwidth=50, anchor=tk.CENTER)
    bund.column("loss", width=150, minwidth=50, anchor=tk.CENTER)
    bund.column("gd", width=200, minwidth=100, anchor=tk.CENTER)
    bund.column("points", width=150, minwidth=50, anchor=tk.CENTER)
    bund.heading("Abbrevaition", text="Team", anchor=tk.CENTER)
    bund.heading("played", text="Played", anchor=tk.CENTER)
    bund.heading("win", text="Won", anchor=tk.CENTER)
    bund.heading("draw", text="Draw", anchor=tk.CENTER)
    bund.heading("loss", text="Loss", anchor=tk.CENTER)
    bund.heading("gd", text="Goal Difference", anchor=tk.CENTER)
    bund.heading("points", text="Points", anchor=tk.CENTER)

    i = 0
    for rows in bun:
        bund.insert('', i, text="", values=(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6]))
        i = i + 1

    vsb = ttk.Scrollbar(root, orient="vertical")
    vsb.configure(command=bund.yview)
    bund.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    bund.pack(fill=BOTH, expand=1)

    root.mainloop()
