#! c:\[path to Python 3.6]\python.exe
import tkinter as tk
from tkinter import *
from tkinter import Label, filedialog, Text
from tkinter import font
from typing import Sized
from tkinter import ttk
from tkinter_custom_button import TkinterCustomButton

from PIL import ImageTk, Image
import os
from tkinter.constants import X
import psycopg2 as psql

class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)

root = tk.Tk()
root.title('Olympics Database')

currentTable = ""

mainFrame = Frame(root)
mainFrame.pack(fill=BOTH, expand=YES)
myCanvas = ResizingCanvas(mainFrame,width = 1920, height= 1000, bg="#212F3D", highlightthickness = 0)
myCanvas.pack(fill = BOTH, expand=YES)

subFrame1 = tk.Frame(root, bg='#117A65', bd=10)
subFrame1.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.9, anchor='n')

label = tk.Label(subFrame1, bg='#0b1b2b')
label.place(relwidth=1, relheight=1)

Olympics_logo = ImageTk.PhotoImage((Image.open("Assets/olympics_logo.PNG")).resize(size=(160,73)))
logo = Label(subFrame1, image = Olympics_logo, bg='#0b1b2b')
logo.place(relx = 0, rely=0)

Heading = Label(subFrame1,text="OLYMPIC DATABASE",fg="white",bg="#0b1b2b",font=("Arial",30))
Heading.place(relx=0.30,rely=0.05)

def back():
    root.destroy()
    import logincc

def athlete(cur):
    column = ('firstname','lastname','playerid','gender','age','height','weight','passportno')
    tree = ttk.Treeview(subFrame1,columns=column,show='headings',)
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading",background="#0b1b2b",foreground="white",font=(None,15))
    style.configure("Treeview",background="#117A65",fieldbackground="#0b1b2b",font=(None,10))
    tree.column("firstname",anchor=CENTER, stretch=NO, width=100)
    tree.heading('firstname', text='firstname')
    tree.column("lastname",anchor=CENTER, stretch=NO, width=100)
    tree.heading('lastname', text='lastname')
    tree.column("playerid",anchor=CENTER, stretch=NO, width=90)
    tree.heading('playerid', text='playerid')
    tree.column("gender",anchor=CENTER, stretch=NO, width=100)
    tree.heading('gender', text='gender')
    tree.column("age",anchor=CENTER, stretch=NO, width=50)
    tree.heading('age', text='age')
    tree.column("height",anchor=CENTER, stretch=NO, width=80)
    tree.heading('height', text='height')
    tree.column("weight",anchor=CENTER, stretch=NO, width=80)
    tree.heading('weight', text='weight')
    tree.column("passportno",anchor=CENTER, stretch=NO, width=120)
    tree.heading('passportno', text='passportno')
    '''
    add_frame = Frame(subFrame2)
    add_frame.pack(pady=20)

    #Labels
    l1 = Label(add_frame, text="FirstName")
    l1.grid(row=0, column=0)

    l2 = Label(add_frame, text="LastName")
    l2.grid(row=0, column=1)

    l3 = Label(add_frame, text="PlayerId")
    l3.grid(row=0, column=2)

    l4 = Label(add_frame, text="Gender")
    l4.grid(row=0, column=3)

    l4 = Label(add_frame, text="Age")
    l4.grid(row=0, column=4)

    l4 = Label(add_frame, text="Height")
    l4.grid(row=0, column=5)

    l4 = Label(add_frame, text="Weight")
    l4.grid(row=0, column=6)

    l4 = Label(add_frame, text="PassportNo")
    l4.grid(row=0, column=7)

    #Entry boxes
    firstname_box = Entry(add_frame)
    firstname_box.grid(row=1, column=0)

    lastname_box = Entry(add_frame)
    lastname_box.grid(row=1, column=1)

    id_box = Entry(add_frame)
    id_box.grid(row=1, column=2)

    gender_box = Entry(add_frame)
    gender_box.grid(row=1, column=3)

    age_box = Entry(add_frame)
    age_box.grid(row=1, column=4)

    height_box = Entry(add_frame)
    height_box.grid(row=1, column=5)

    weight_box = Entry(add_frame)
    weight_box.grid(row=1, column=6)

    passport_box = Entry(add_frame)
    passport_box.grid(row=1, column=7)'''
    
    tree.place(relx=0.14,rely=0.22)

    x = cur.fetchall()
    for i in x:
        firstname = i[0]
        lastname = i[1]
        playerid = i[2]
        gender = i[3]
        age = i[4]
        height = i[5]
        weight = i[6]
        passportno = i[7]
        value = (firstname,lastname,playerid,gender,age,height,weight,passportno)
        tree.insert('', tk.END,values=value)
    global currentTable
    currentTable = "display_athlete"

def coach(cur):
    column = ('firstname','lastname','coachid','gender','playerid','sport','passportno')
    tree = ttk.Treeview(subFrame1,columns=column,show='headings')
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading",background="#0b1b2b",foreground="white",font=(None,15))
    style.configure("Treeview",background="#117A65",fieldbackground="#0b1b2b", font=(None,10))
    tree.column("firstname",anchor=CENTER, stretch=NO, width=100)
    tree.heading('firstname', text='firstname')
    tree.column("lastname",anchor=CENTER, stretch=NO, width=100)
    tree.heading('lastname', text='lastname')
    tree.column("coachid",anchor=CENTER, stretch=NO, width=100)
    tree.heading('coachid', text='coachid')
    tree.column("gender",anchor=CENTER, stretch=NO, width=100)
    tree.heading('gender', text='gender')
    tree.column("playerid",anchor=CENTER, stretch=NO, width=100)
    tree.heading('playerid', text='playerid')
    tree.column("sport",anchor=CENTER, stretch=NO, width=100)
    tree.heading('sport', text='sport')
    tree.column("passportno",anchor=CENTER, stretch=NO, width=120)
    tree.heading('passportno', text='passportno')
    tree.place(relx=0.14,rely=0.22)

    x = cur.fetchall()
    for i in x:
        firstname = i[0]
        lastname = i[1]
        coachid = i[2]
        gender = i[3]
        playerid = i[4]
        sport = i[5]
        passportno = i[6]
        value = (firstname,lastname,coachid,gender,playerid,sport,passportno)
        tree.insert('', tk.END,values=value)
    global currentTable
    currentTable = "display_coach"

def country(cur):
    column = ('name','countryid','numberofparticipants','population','representative')
    tree = ttk.Treeview(subFrame1,columns=column,show='headings')
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading",background="#0b1b2b",foreground="white",font=(None,15))
    style.configure("Treeview",background="#117A65",fieldbackground="#0b1b2b", font=(None,10))
    tree.column("name",anchor=CENTER, stretch=NO, width=100)
    tree.heading('name', text='name')
    tree.column("countryid",anchor=CENTER, stretch=NO, width=130)
    tree.heading('countryid', text='countryid')
    tree.column("numberofparticipants",anchor=CENTER, stretch=NO, width=220)
    tree.heading('numberofparticipants', text='numberofparticipants')
    tree.column("population",anchor=CENTER, stretch=NO, width=120)
    tree.heading('population', text='population')
    tree.column("representative",anchor=CENTER, stretch=NO, width=150)
    tree.heading('representative', text='representative')
    tree.place(relx=0.14,rely=0.22)

    x = cur.fetchall()
    for i in x:
        name = i[0]
        countryid = i[1]
        numberofparticipants = i[2]
        population = i[3]
        representative = i[4]
        value = (name,countryid,numberofparticipants,population,representative)
        tree.insert('', tk.END,values=value)
    global currentTable
    currentTable = "display_country"

def schedule(cur):
    column = ('sportname','sportid','duration','date','starttime','endtime')
    tree = ttk.Treeview(subFrame1,columns=column,show='headings')
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading",background="#0b1b2b",foreground="white",font=(None,15))
    style.configure("Treeview",background="#117A65",fieldbackground="#0b1b2b", font=(None,10))
    tree.column("sportname",anchor=CENTER, stretch=NO, width=150)
    tree.heading('sportname', text='sportname')
    tree.column("sportid",anchor=CENTER, stretch=NO, width=100)
    tree.heading('sportid', text='sportid')
    tree.column("duration",anchor=CENTER, stretch=NO, width=100)
    tree.heading('duration', text='duration')
    tree.column("date",anchor=CENTER, stretch=NO, width=120)
    tree.heading('date', text='date')
    tree.column("starttime",anchor=CENTER, stretch=NO, width=125)
    tree.heading('starttime', text='starttime')
    tree.column("endtime",anchor=CENTER, stretch=NO, width=125)
    tree.heading('endtime', text='endtime')
    tree.place(relx=0.14,rely=0.22)

    x = cur.fetchall()
    for i in x:
        sportname = i[0]
        sportid = i[1]
        duration = i[2]
        date = i[3]
        startdate = i[4]
        enddate = i[5]
        value = (sportname,sportid,duration,date,startdate,enddate)
        tree.insert('', tk.END,values=value)
    global currentTable
    currentTable = "display_schedule"

def display_athlete():
    conn = psql.connect(host="localhost",database="olympics",user="guest",password="guest")
    cur = conn.cursor()
    cur.execute("select * from athlete;")
    athlete(cur)
    conn.commit()
    conn.close()

def display_coach():
    conn = psql.connect(host="localhost",database="olympics",user="guest",password="guest")
    cur = conn.cursor()
    cur.execute("select * from coach;")
    coach(cur)
    conn.commit()
    conn.close()

def display_country():
    conn = psql.connect(host="localhost",database="olympics",user="guest",password="guest")
    cur = conn.cursor()
    cur.execute("select * from country;")
    country(cur)
    conn.commit()
    conn.close()

def display_schedule():
    conn = psql.connect(host="localhost",database="olympics",user="guest",password="guest")
    cur = conn.cursor()
    cur.execute("select * from schedule;")
    schedule(cur)
    conn.commit()
    conn.close()

def gold_win():
    column = ('firstname','lastname','gender','medal')

    conn = psql.connect(host="localhost",database="olympics",user="guest",password="guest")
    cur = conn.cursor()
    cur.execute('''select A.firstname, A.lastname, A.gender, M.medal
            from athlete AS A, win AS M
    where A.playerid = M.playerid AND M.medal = 'Gold';''')

    tree = ttk.Treeview(subFrame1,columns=column,show='headings')
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading",background="#0b1b2b",foreground="white",font=(None,15))
    style.configure("Treeview",background="#117A65",fieldbackground="#0b1b2b", font=(None,10))
    tree.column("firstname",anchor=CENTER, stretch=NO, width=180)
    tree.heading('firstname', text='firstname')
    tree.column("lastname",anchor=CENTER, stretch=NO, width=180)
    tree.heading('lastname', text='lastname')
    tree.column("gender",anchor=CENTER, stretch=NO, width=180)
    tree.heading('gender', text='gender')
    tree.column("medal",anchor=CENTER, stretch=NO, width=180)
    tree.heading('medal', text='medal')
    tree.place(relx=0.14,rely=0.22)

    x = cur.fetchall()
    for i in x:
        firstname = i[0]
        lastname = i[1]
        gender = i[2]
        medal = i[3]
        value = (firstname,lastname,gender,medal)
        tree.insert('', tk.END,values=value)
    global currentTable
    currentTable = "gold_win"
    conn.commit()
    conn.close()

def silver_win():
    column = ('firstname','lastname','gender','medal')

    conn = psql.connect(host="localhost",database="olympics",user="guest",password="guest")
    cur = conn.cursor()
    cur.execute('''select A.firstname, A.lastname, A.gender, M.medal
            from athlete AS A, win AS M
    where A.playerid = M.playerid AND M.medal = 'Silver';''')

    tree = ttk.Treeview(subFrame1,columns=column,show='headings')
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading",background="#0b1b2b",foreground="white",font=(None,15))
    style.configure("Treeview",background="#117A65",fieldbackground="#0b1b2b", font=(None,10))
    tree.column("firstname",anchor=CENTER, stretch=NO, width=180)
    tree.heading('firstname', text='firstname')
    tree.column("lastname",anchor=CENTER, stretch=NO, width=180)
    tree.heading('lastname', text='lastname')
    tree.column("gender",anchor=CENTER, stretch=NO, width=180)
    tree.heading('gender', text='gender')
    tree.column("medal",anchor=CENTER, stretch=NO, width=180)
    tree.heading('medal', text='medal')
    tree.place(relx=0.14,rely=0.22)

    x = cur.fetchall()
    for i in x:
        firstname = i[0]
        lastname = i[1]
        gender = i[2]
        medal = i[3]
        value = (firstname,lastname,gender,medal)
        tree.insert('', tk.END,values=value)
    global currentTable
    currentTable = "silver_win"
    conn.commit()
    conn.close()

def bronze_win():
    column = ('firstname','lastname','gender','medal')

    conn = psql.connect(host="localhost",database="olympics",user="guest",password="guest")
    cur = conn.cursor()
    cur.execute('''select A.firstname, A.lastname, A.gender, M.medal
            from athlete AS A, win AS M
    where A.playerid = M.playerid AND M.medal = 'Bronze';''')

    tree = ttk.Treeview(subFrame1,columns=column,show='headings')
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading",background="#0b1b2b",foreground="white",font=(None,15))
    style.configure("Treeview",background="#117A65",fieldbackground="#0b1b2b", font=(None,10))
    tree.column("firstname",anchor=CENTER, stretch=NO, width=180)
    tree.heading('firstname', text='firstname')
    tree.column("lastname",anchor=CENTER, stretch=NO, width=180)
    tree.heading('lastname', text='lastname')
    tree.column("gender",anchor=CENTER, stretch=NO, width=180)
    tree.heading('gender', text='gender')
    tree.column("medal",anchor=CENTER, stretch=NO, width=180)
    tree.heading('medal', text='medal')
    tree.place(relx=0.14,rely=0.22)

    x = cur.fetchall()
    for i in x:
        firstname = i[0]
        lastname = i[1]
        gender = i[2]
        medal = i[3]
        value = (firstname,lastname,gender,medal)
        tree.insert('', tk.END,values=value)
    global currentTable
    currentTable = "bronze_win"
    conn.commit()

    conn.close()

def sort():
    conn = psql.connect(host="localhost",database="olympics",user="guest",password="guest")
    cur = conn.cursor()
    if(currentTable == "display_athlete"):
        cur.execute("select * from athlete order by firstname;")
        athlete(cur)
    if(currentTable == "display_coach"):
        cur.execute("select * from coach order by firstname;")
        coach(cur)    
    if(currentTable == "display_country"):
        cur.execute("select * from country order by name;")
        country(cur)      
    if(currentTable == "display_schedule"):
        cur.execute("select * from schedule order by sportname;")
        schedule(cur)  

showathlete = TkinterCustomButton(bg_color=None, fg_color="#212F3D", border_color="#117A65", hover_color="#34495E", text_font=None,
                            text="Athlete", text_color="white", corner_radius=0, border_width=4, width=80, height=35, hover=True, command= display_athlete)
showathlete.place(relx=0.135,rely=0.2)

showcoach = TkinterCustomButton(bg_color=None, fg_color="#212F3D", border_color="#117A65", hover_color="#34495E", text_font=None,
                            text="Coach", text_color="white", corner_radius=0, border_width=4, width=80, height=35, hover=True, command= display_coach)
showcoach.place(relx=0.2,rely=0.2)

showcountry = TkinterCustomButton(bg_color=None, fg_color="#212F3D", border_color="#117A65", hover_color="#34495E", text_font=None,
                            text="Country", text_color="white", corner_radius=0, border_width=4, width=80, height=35, hover=True, command= display_country)
showcountry.place(relx=0.265,rely=0.2)

showschedule = TkinterCustomButton(bg_color=None, fg_color="#212F3D", border_color="#117A65", hover_color="#34495E", text_font=None,
                            text="Schedule", text_color="white", corner_radius=0, border_width=4, width=80, height=35, hover=True, command= display_schedule)
showschedule.place(relx=0.33,rely=0.2)

sortBy = TkinterCustomButton(bg_color=None, fg_color="#212F3D", border_color="#117A65", hover_color="#34495E", text_font=None,
                            text="Sort", text_color="white", corner_radius=0, border_width=4, width=80, height=35, hover=True, command= sort)
sortBy.place(relx=0.680,rely=0.2)

gold = TkinterCustomButton(bg_color=None, fg_color="#212F3D", border_color="#117A65", hover_color="#34495E", text_font=None,
                            text="Gold", text_color="white", corner_radius=0, border_width=4, width=100, height=50, hover=True, command= gold_win)
gold.place(relx=0.60,rely=0.60)

silver = TkinterCustomButton(bg_color=None, fg_color="#212F3D", border_color="#117A65", hover_color="#34495E", text_font=None,
                            text="Silver", text_color="white", corner_radius=0, border_width=4, width=100, height=50, hover=True, command= silver_win)
silver.place(relx=0.680,rely=0.60)

bronze = TkinterCustomButton(bg_color=None, fg_color="#212F3D", border_color="#117A65", hover_color="#34495E", text_font=None,
                            text="Bronze", text_color="white", corner_radius=0, border_width=4, width=100, height=50, hover=True, command= bronze_win)
bronze.place(relx=0.760,rely=0.60)

back = TkinterCustomButton(bg_color=None, fg_color="#212F3D", border_color="#117A65", hover_color="#34495E", text_font=None,
                            text="Back", text_color="white", corner_radius=0, border_width=4, width=100, height=50, hover=True, command= back)
back.place(relx=0,rely=0)


root.mainloop()


