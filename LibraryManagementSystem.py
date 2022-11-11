from tkinter import *
from tkinter import messagebox
import os
import mysql.connector as m
mydb =m.connect(host='localhost',user ='root',password='1234',database='library')
mycursor = mydb.cursor(buffered=True)
w=Tk()
def signup():
    w.destroy()
    w1=Tk()
    def enter(a,b,c,d):
        if(len(d)!=10):
            messagebox.showerror("Error","Length of Phone number can't be less than or greater than 10")
            return None
        if(b.isdigit() is False):
            messagebox.showerror("Error","UID can't have alphabets")
            return None
        if(d.isdigit() is False):
            messagebox.showerror("Error","Phone Number can't have alphabets")
            return None
        mycursor.execute("insert into login values(%s,%s,%s,%s)",(a,b,c,d))
        mydb.commit()
        messagebox.showinfo("Success","Congratulations, You have successfully registered in our database")
        w1.destroy()
    w1.geometry('300x300')
    w1.resizable(False,False)
    n=StringVar()
    u=StringVar()
    p=StringVar()
    pn=StringVar()
    ln=Label(w1,text='Enter Name:').place(x=20,y=50)
    lu=Label(w1,text='Enter UID:').place(x=20,y=100)
    lp=Label(w1,text='Enter Password:').place(x=20,y=150)
    lpn=Label(w1,text='Enter Phone Number:').place(x=20,y=200)
    ne=Entry(w1,textvariable=n).place(x=150,y=50)
    ue=Entry(w1,textvariable=u).place(x=150,y=100)
    pe=Entry(w1,textvariable=p).place(x=150,y=150)
    pne=Entry(w1,textvariable=pn).place(x=150,y=200)
    b=Button(w1,text="Submit",command=lambda:enter(n.get(),u.get(),p.get(),pn.get())).place(x=150,y=250)
def show(w2,a,b):
    mycursor.execute("select * from login")
    for y in mycursor:
        if((a in y) and (b in y)):
            mycursor.execute("select password from login where uid={} and ph_no={}".format(a,b))
            c=str(mycursor.fetchall())
            messagebox.showinfo("Password","Your password is '{}'".format(c[3:len(c)-4]))
            w2.destroy()
def forgot():
    w.destroy()
    w2=Tk()
    w2.geometry('300x200')
    lu=Label(w2,text="Enter UID: ").place(x=10,y=50)
    lp=Label(w2,text="Enter Phone Number: ").place(x=10,y=100)
    u=StringVar()
    p=StringVar()
    un=Entry(w2,textvariable=u).place(x=160,y=50)
    pn=Entry(w2,textvariable=p).place(x=160,y=100)
    b=Button(w2,text="Submit",command=lambda:show(w2,int(u.get()),int(p.get()))).place(x=150,y=150)
    w2.resizable(False,False)
def validate():
    mycursor.execute("select * from login")
    for y in mycursor:
        if ((uid.get() in y) and (password.get() in y)):
            m=messagebox.showinfo("Success","Redirecting to home page")
            w.destroy()
            os.startfile(r'BooksOfLibrary.py')
            return None
        else:            
            m=messagebox.showerror("Failed","Enter correct details")
l1=Label(text="Enter UID: ").place(x=0,y=50)
l2=Label(text="Enter Password:").place(x=0,y=100)
uid=IntVar()
password=StringVar()
uide=Entry(w,textvariable=uid).place(x=100,y=50)
passworde=Entry(w,textvariable=password).place(x=100,y=100)
b1=Button(w,text="Sign up?",command=lambda:signup()).place(x=170,y=150)
b2=Button(w,text="Submit",command=lambda:validate()).place(x=100,y=150)
b3=Button(w,text="Forgot password",command=lambda:forgot()).place(x=110,y=190)
w.geometry('300x300')
w.resizable(False,False)
w.mainloop()