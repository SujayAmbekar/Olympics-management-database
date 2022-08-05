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

subframe2 = tk.Frame(root, bg='#0b1b2b', bd=10)
subframe2.place(relx=0.5, rely=0.6, relwidth=0.75, relheight=0.3, anchor='n')

label = tk.Label(subFrame1, bg='#0b1b2b')
label.place(relwidth=1, relheight=1)

Olympics_logo = ImageTk.PhotoImage((Image.open("Assets/olympics_logo.PNG")).resize(size=(160,73)))
logo = Label(subFrame1, image = Olympics_logo, bg='#0b1b2b')
logo.place(relx = 0, rely=0)

Heading = Label(subFrame1,text="OLYMPIC DATABASE",fg="white",bg="#0b1b2b",font=("Arial",30))
Heading.place(relx=0.30,rely=0.05)

c_btn=None
data =[]

def back():
    root.destroy()
    import loginc

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

flag = 0

wd=None
a1=None
a2=None
a3=None
a4=None
a5=None
a6=None
a7=None
a8=None

fname=None
lname=None
playerid=None
gender=None
age=None
height=None
weight=None
passportno=None

def globalInsert():
        global wd,a1,a3,a4,a5,a6,a7,a8,fname,lname,playerid,gender,age,height,weight,passportno
        wd = tk.Tk()
        wd.title('insert')
        wd.geometry('500x700')
        #if clicked_bttn!='athlete':
        a1 = tk.Label(wd, text ="First Name",font=("Arial",10))
        a1.place(relx=0.2, rely = 0.1)
        fname = tk.Entry(wd, width = 35,font=("Arial",10))
        fname.place(relx = 0.48, rely = 0.1, width = 150,height=20)

        a2 = tk.Label(wd, text ="Last Name",font=("Arial",10))
        a2.place(relx=0.2, rely = 0.15)
        lname = tk.Entry(wd, width = 35,font=("Arial",10))
        lname.place(relx = 0.48, rely = 0.15, width = 150,height=20)

        a3 = tk.Label(wd, text ="Player ID",font=("Arial",10))
        a3.place(relx=0.2, rely = 0.2)
        playerid = tk.Entry(wd, width = 35,font=("Arial",10))
        playerid.place(relx = 0.48, rely = 0.2, width = 150,height=20)

        a4 = tk.Label(wd, text ="Gender",font=("Arial",10))
        a4.place(relx=0.2, rely = 0.25)
        gender = tk.Entry(wd, width = 35,font=("Arial",10))
        gender.place(relx = 0.48, rely = 0.25, width = 150,height=20)

        a5 = tk.Label(wd, text ="Age",font=("Arial",10))
        a5.place(relx=0.2, rely = 0.3)
        age = tk.Entry(wd, width = 35,font=("Arial",10))
        age.place(relx = 0.48, rely = 0.3, width = 150,height=20)

        a6 = tk.Label(wd, text ="Height",font=("Arial",10))
        a6.place(relx=0.2, rely = 0.35)
        height = tk.Entry(wd, width = 35,font=("Arial",10))
        height.place(relx = 0.48, rely = 0.35, width = 150,height=20)

        a7 = tk.Label(wd, text ="Weight",font=("Arial",10))
        a7.place(relx=0.2, rely = 0.4)
        weight = tk.Entry(wd, width = 35,font=("Arial",10))
        weight.place(relx = 0.48, rely = 0.4, width = 150,height=20)

        a8 = tk.Label(wd, text ="Passport no",font=("Arial",10))
        a8.place(relx=0.2, rely = 0.45)
        passportno = tk.Entry(wd, width = 35,font=("Arial",10))
        passportno.place(relx = 0.48, rely = 0.45, width = 150,height=20)


        submitbtn = tk.Button(wd, text ="Enter",
                        bg ='white', command = insert_athlete)
        submitbtn.place(relx = 0.48, rely = 0.55, width = 55)
        wd.mainloop()

def delete():
    global press_delete
    press_delete = True
    value = firstname_box.get()
    conn = psql.connect(host="localhost",database="olympics",user="postgres",password="bilva")
    if press_delete:
        t = (value,)
        cur=conn.cursor()
        cur.execute("DELETE from athlete where playerid = (%s);",t)
        press_delete = False
        conn.commit()
    firstname_box.delete(0, END)
    display_athlete()


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


def supportstaff(cur):
    column = ('name','staffid','gender','role')
    tree = ttk.Treeview(subFrame1,columns=column,show='headings',)
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading",background="#0b1b2b",foreground="white",font=(None,15))
    style.configure("Treeview",background="#117A65",fieldbackground="#0b1b2b",font=(None,10))
    tree.column("name",anchor=CENTER, stretch=NO, width=180)
    tree.heading('name', text='name')
    tree.column("staffid",anchor=CENTER, stretch=NO, width=180)
    tree.heading('staffid', text='staffid')
    tree.column("gender",anchor=CENTER, stretch=NO, width=180)
    tree.heading('gender', text='gender')
    tree.column("role",anchor=CENTER, stretch=NO, width=180)
    tree.heading('role', text='role')
    tree.place(relx=0.14,rely=0.22)
    x = cur.fetchall()
    for i in x:
        firstname = i[0]
        staffid = i[1]
        gender = i[2]
        role = i[3]
        value = (firstname,staffid,gender,role)
        tree.insert('', tk.END,values=value)
    global currentTable
    currentTable = "display_staff"

def facility(cur):
    column = ('name','facilityid','location','capacity')
    tree = ttk.Treeview(subFrame1,columns=column,show='headings')
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading",background="#0b1b2b",foreground="white",font=(None,15))
    style.configure("Treeview",background="#117A65",fieldbackground="#0b1b2b", font=(None,10))
    tree.column("name",anchor=CENTER, stretch=NO, width=180)
    tree.heading('name', text='name')
    tree.column("facilityid",anchor=CENTER, stretch=NO, width=180)
    tree.heading('facilityid', text='facilityid')
    tree.column("location",anchor=CENTER, stretch=NO, width=180)
    tree.heading('location', text='location')
    tree.column("capacity",anchor=CENTER, stretch=NO, width=180)
    tree.heading('capacity', text='capacity')
    tree.place(relx=0.14,rely=0.22)

    x = cur.fetchall()
    for i in x:
        name = i[0]
        facilityid = i[1]
        location = i[2]
        capacity = i[3]
        value = (name,facilityid,location,capacity)
        tree.insert('', tk.END,values=value)
    global currentTable
    currentTable = "display_facility"

def transport(cur):
    column = ('type','facilityid','transportid', 'capacity')
    tree = ttk.Treeview(subFrame1,columns=column,show='headings')
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading",background="#0b1b2b",foreground="white",font=(None,15))
    style.configure("Treeview",background="#117A65",fieldbackground="#0b1b2b", font=(None,10))
    tree.column("type",anchor=CENTER, stretch=NO, width=180)
    tree.heading('type', text='type')
    tree.column("facilityid",anchor=CENTER, stretch=NO, width=180)
    tree.heading('facilityid', text='facilityid')
    tree.column("transportid",anchor=CENTER, stretch=NO, width=180)
    tree.heading('transportid', text='transportid')
    tree.column("capacity",anchor=CENTER, stretch=NO, width=180)
    tree.heading('capacity', text='capacity')    
    tree.place(relx=0.14,rely=0.22)

    x = cur.fetchall()
    for i in x:
        type = i[0]
        facilityid = i[1]
        transportid = i[2]
        capacity = i[3]
        value = (type,facilityid,transportid,capacity)
        tree.insert('', tk.END,values=value)
    global currentTable
    currentTable = "display_transport"

def sportactivity(cur):
    column = ('sportname','activityno','numberofparticipants')
    tree = ttk.Treeview(subFrame1,columns=column,show='headings')
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading",background="#0b1b2b",foreground="white",font=(None,15))
    style.configure("Treeview",background="#117A65",fieldbackground="#0b1b2b", font=(None,10))
    tree.column("sportname",anchor=CENTER, stretch=NO, width=240)
    tree.heading('sportname', text='sportname')
    tree.column("activityno",anchor=CENTER, stretch=NO, width=240)
    tree.heading('activityno', text='activityno')
    tree.column("numberofparticipants",anchor=CENTER, stretch=NO, width=240)
    tree.heading('numberofparticipants', text='numberofparticipants')
    tree.place(relx=0.14,rely=0.22)

    x = cur.fetchall()
    for i in x:
        sportname = i[0]
        activityno = i[1]
        numberofparticipants = i[2]
        value = (sportname,activityno,numberofparticipants)
        tree.insert('', tk.END,values=value)
    global currentTable
    currentTable = "display_sportactivity"

def sport(cur):
    column = ('sportname','sportid','typeofsport')
    tree = ttk.Treeview(subFrame1,columns=column,show='headings')
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading",background="#0b1b2b",foreground="white",font=(None,15))
    style.configure("Treeview",background="#117A65",fieldbackground="#0b1b2b", font=(None,10))
    tree.column("sportname",anchor=CENTER, stretch=NO, width=240)
    tree.heading('sportname', text='sportname')
    tree.column("sportid",anchor=CENTER, stretch=NO, width=240)
    tree.heading('sportid', text='sportid')
    tree.column("typeofsport",anchor=CENTER, stretch=NO, width=240)
    tree.heading('typeofsport', text='typeofsport')
    tree.place(relx=0.14,rely=0.22)

    x = cur.fetchall()
    for i in x:
        sportname = i[0]
        sportid = i[1]
        typeofsport = i[2]
        value = (sportname,sportid,typeofsport)
        tree.insert('', tk.END,values=value)
    global currentTable
    currentTable = "display_sport"

def display_athlete():
    c_btn="athlete"
    conn = psql.connect(host="localhost",database="olympics",user="postgres",password="bilva")
    cur = conn.cursor()
    cur.execute("select * from athlete;")
    athlete(cur)
    conn.commit()
    conn.close()

def insert_athlete():
    conn = psql.connect(host="localhost",database="olympics",user="postgres",password="bilva")
    cur = conn.cursor()

    data.append(fname.get())
    data.append(lname.get())
    data.append(playerid.get())
    data.append(gender.get())
    data.append(age.get())
    data.append(height.get())
    data.append(weight.get())
    data.append(passportno.get())
        
    #print(data)

    t_data = (data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])

    try:
        cur.execute("insert into athlete values(%s,%s,%s,%s,%s,%s,%s,%s);",t_data)
        #cur.execute("insert into athlete values('Ravi','K','345','M',23,5.5,23,899);")
        tk.messagebox.showinfo("Inserted")
    except Exception as e:
        print(e)
        tk.messagebox.showinfo("Invalid data format")
    display_athlete()
    conn.commit()
    conn.close()


def display_coach():
    conn = psql.connect(host="localhost",database="olympics",user="postgres",password="bilva")
    cur = conn.cursor()
    cur.execute("select * from coach;")
    coach(cur)
    conn.commit()
    conn.close()

def display_country():
    conn = psql.connect(host="localhost",database="olympics",user="postgres",password="bilva")
    cur = conn.cursor()
    cur.execute("select * from country;")
    country(cur)
    conn.commit()
    conn.close()

def display_schedule():
    conn = psql.connect(host="localhost",database="olympics",user="postgres",password="bilva")
    cur = conn.cursor()
    cur.execute("select * from schedule;")
    schedule(cur)
    conn.commit()
    conn.close()

def display_staff():
    conn = psql.connect(host="localhost",database="olympics",user="postgres",password="bilva")
    cur = conn.cursor()
    cur.execute("select * from supportstaff;")
    supportstaff(cur)
    conn.commit()
    conn.close()

def display_facility():
    conn = psql.connect(host="localhost",database="olympics",user="postgres",password="bilva")
    cur = conn.cursor()
    cur.execute("select * from facility;")
    facility(cur)
    conn.commit()
    conn.close()

def display_transport():
    conn = psql.connect(host="localhost",database="olympics",user="postgres",password="bilva")
    cur = conn.cursor()
    cur.execute("select * from transportation;")
    transport(cur)
    conn.commit()
    conn.close()

def display_sportactivity():
    conn = psql.connect(host="localhost",database="olympics",user="postgres",password="bilva")
    cur = conn.cursor()
    cur.execute("select * from sportactivity;")
    sportactivity(cur)
    conn.commit()
    conn.close()  

def display_sport():
    conn = psql.connect(host="localhost",database="olympics",user="postgres",password="bilva")
    cur = conn.cursor()
    cur.execute("select * from sport;")
    sport(cur)
    conn.commit()
    conn.close() 

firstname_box = Entry(subFrame1)
firstname_box.place(relx=0.75,rely=0.23,width=80)


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

showstaff = TkinterCustomButton(bg_color=None, fg_color="#212F3D", border_color="#117A65", hover_color="#34495E", text_font=None,
                            text="Staff", text_color="white", corner_radius=0, border_width=4, width=80, height=35, hover=True, command= display_staff)
showstaff.place(relx=0.395,rely=0.2)

showfacility = TkinterCustomButton(bg_color=None, fg_color="#212F3D", border_color="#117A65", hover_color="#34495E", text_font=None,
                            text="Facility", text_color="white", corner_radius=0, border_width=4, width=80, height=35, hover=True, command= display_facility)
showfacility.place(relx=0.46,rely=0.2)

showtransport = TkinterCustomButton(bg_color=None, fg_color="#212F3D", border_color="#117A65", hover_color="#34495E", text_font=None,
                            text="Transport", text_color="white", corner_radius=0, border_width=4, width=80, height=35, hover=True, command= display_transport)
showtransport.place(relx=0.525,rely=0.2)

showactivity = TkinterCustomButton(bg_color=None, fg_color="#212F3D", border_color="#117A65", hover_color="#34495E", text_font=None,
                            text="Activity", text_color="white", corner_radius=0, border_width=4, width=80, height=35, hover=True, command= display_sportactivity)
showactivity.place(relx=0.590,rely=0.2)

showsport = TkinterCustomButton(bg_color=None, fg_color="#212F3D", border_color="#117A65", hover_color="#34495E", text_font=None,
                            text="Sport", text_color="white", corner_radius=0, border_width=4, width=80, height=35, hover=True, command= display_sport)
showsport.place(relx=0.655,rely=0.2)

insertbttn = TkinterCustomButton(bg_color=None, fg_color="#212F3D", border_color="#117A65", hover_color="#34495E", text_font=None,
                            text="Insert", text_color="white", corner_radius=0, border_width=4, width=80, height=35, hover=True, command= globalInsert)
insertbttn.place(relx=0.2,rely=0.55)

delete_entry = TkinterCustomButton(bg_color=None, fg_color="#212F3D", border_color="#117A65", hover_color="#34495E", text_font=None,
                            text="Delete", text_color="white", corner_radius=0, border_width=4, width=100, height=50, hover=True, command= delete)
delete_entry.place(relx=0.72,rely=0.30)

back = TkinterCustomButton(bg_color=None, fg_color="#212F3D", border_color="#117A65", hover_color="#34495E", text_font=None,
                            text="Back", text_color="white", corner_radius=0, border_width=4, width=100, height=50, hover=True, command= back)
back.place(relx=0,rely=0)

root.mainloop()


