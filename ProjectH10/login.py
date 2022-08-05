import tkinter as tk
import tkinter.messagebox
import psycopg2 as psql
from tkinter import *
from PIL import ImageTk, Image

users=["Postgres","guest","tstaff"]

def submit():
     
    user = Username.get()
    passw = password.get()
    if user=="admin":
        user="postgres"
    login(user, passw)
  

def adminPage():
    root.destroy()
    import Admin

def athletePage():
    root.destroy()
    import Athlete

def staffPage():
    root.destroy()
    import Staff

def login(dbuser, passw):
    if passw and dbuser:
        try:
            db = psql.connect(
                host="localhost",
                database="olympics",
                user=dbuser,
                password=passw  
            )
            
            if dbuser=="postgres":
                adminPage()
            elif dbuser=="guest":
                athletePage()
            elif dbuser=="tstaff":
                staffPage()
            
            db.close()
        except Exception as e:
            print(e)
            msg="Username or Password incorrect"
            tk.messagebox.showinfo(msg)
            print(msg)
    elif passw=="" and dbuser=="":
        msg="fields cannot be blank"
        tk.messagebox.showinfo(msg)
    elif passw=="":
        msg="Password cannot be blank"
        tk.messagebox.showinfo(msg)
    elif dbuser=="":
        msg="Username cannot be blank"
        tk.messagebox.showinfo(msg)

        
  
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
root.title('Olympics DB(Login)')


mainFrame = Frame(root)
mainFrame.pack(fill=BOTH, expand=YES)
myCanvas = ResizingCanvas(mainFrame,width = 1920, height= 1000, highlightthickness = 0)
myCanvas.pack(fill = BOTH, expand=YES)

bg = ImageTk.PhotoImage((Image.open('Assets/bg2.png')).resize(size=(1920,1300)))
logo = Label(myCanvas, image = bg)
logo.pack()



# Defining the first row
lblfrstrow = tk.Label(root, text ="Username -",font=("Arial",20))
lblfrstrow.place(relx=0.40, rely = 0.45)
 
Username = tk.Entry(root, width = 35,font=("Arial",20))
Username.place(relx = 0.48, rely = 0.45, width = 150,height=40)
  
lblsecrow = tk.Label(root, text ="Password -",font=("Arial",20))
lblsecrow.place(relx=0.40,rely=0.5)
 
password = tk.Entry(root, width = 35,font=("Arial",20),show="*")
password.place(relx = 0.48, rely = 0.5, width = 150, height=40)
 
submitbtn = tk.Button(root, text ="Login",
                      bg ='white', command = submit)
submitbtn.place(relx = 0.48, rely = 0.55, width = 55)



root.mainloop()