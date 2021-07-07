from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import pymysql

my_pass = "Shrenik@713"
my_database = "football"
con = pymysql.connect(host="localhost", user="system", password=my_pass, database=my_database)

def teams():
    root = Tk()
    root.title("Teams")
    root.geometry("1440x720")

    club = con.cursor()
    club.execute("select * from teams order by team_id")
    clubs = ttk.Treeview(root)
    clubs['show'] = 'headings'

    x = ttk.Style(root)
    x.theme_use("default")

    clubs["columns"] = ("team_id", "team_name", "abbrevaition", "manager", "stadium", "established")
    clubs.column("team_id", width=200, minwidth=100, anchor=tk.CENTER)
    clubs.column("team_name", width=200, minwidth=200, anchor=tk.CENTER)
    clubs.column("abbrevaition", width=200, minwidth=150, anchor=tk.CENTER)
    clubs.column("manager", width=200, minwidth=150, anchor=tk.CENTER)
    clubs.column("stadium", width=200, minwidth=150, anchor=tk.CENTER)
    clubs.column("established", width=200, minwidth=150, anchor=tk.CENTER)
    clubs.heading("team_id", text="Team ID", anchor=tk.CENTER)
    clubs.heading("team_name", text="Team", anchor=tk.CENTER)
    clubs.heading("abbrevaition", text="Team Code", anchor=tk.CENTER)
    clubs.heading("manager", text="Manager", anchor=tk.CENTER)
    clubs.heading("stadium", text="Stadium", anchor=tk.CENTER)
    clubs.heading("established", text="Established", anchor=tk.CENTER)

    i = 0
    for rows in club:
        clubs.insert('', i, text="", values=(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5]))
        i = i + 1

    vsb = ttk.Scrollbar(root, orient="vertical")
    vsb.configure(command=clubs.yview)
    clubs.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    clubs.pack(fill=BOTH, expand=1)

    root.mainloop()
