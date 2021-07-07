#pip install cryptography
#pip install pillow
#pip install pymysql
#pip install tkinter

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from PL import *
from LaLiga import *
from Serie_A import *
from Bundesliga import *
from Ligue_1 import *
from teams import *

my_pass = "Shrenik@713"
my_database = "football"

con = pymysql.connect(host="localhost", user="system", password=my_pass, database=my_database)

cur = con.cursor()

root = Tk()
root.title("League")
root.minsize(width=1080, height=720)
root.geometry("1080x720")

same = True
n = 4.45
background_image = Image.open("League.jpg")
[ImageSizeWidth, ImageSizeHeight] = background_image.size

newImageSizeWidth = int(ImageSizeWidth*n)
if same:
    newImageSizeHeight = int(ImageSizeHeight*n)
else:
    newImageSizeHeight = int(ImageSizeHeight/n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg="black", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="The League Tables", bg="#ECE0FD", fg="black", font=('Constantia', 20))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Premier League", bg='#3D195B', fg='white', font=('PremierLeague', 16), command=prem)
btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="LaLiga", bg='black', fg='#ffffff', font=('Futura Maxi CG Bold', 16), command=laliga)
btn2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="Bundesliga", bg='#D20515', fg='black', font=('Interstate Regular', 16), command=bundesliga)
btn3.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Serie A", bg='#008FD7', fg='#002d71', font=('DIN Next ARABIC BOLD', 16), command=serie_a)
btn4.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Ligue 1", bg='#12233F', fg='white', font=('Open Sans', 16), command=ligue_1)
btn5.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn6 = Button(root, text="Teams", bg='#F78D42', fg='white', font=('Times New Roman', 16), command=teams)
btn6.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

root.mainloop()
