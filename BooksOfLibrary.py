from tkinter import *
import os
from tkinter import messagebox
import mysql.connector as m
import random
from datetime import date,datetime
today=str(date.today())
mydb =m.connect(host='localhost',user ='root',password='1234',database='library')
mycursor = mydb.cursor(buffered=True)
tn=""
for i in range(6):
    tn+=str(random.randint(0,9))
mycursor.execute('select * from books')
for y in mycursor:
    while tn in y:
        tn=""
        for i in range(6):
            tn+=str(random.randint(0,9))
def library():
    def issuebook():
        w.destroy()
        w1=Tk()
        def submit():
            mycursor.execute("insert into books values(%s,%s,%s,%s,%s,%s,%s)",(a.get(),int(b.get()),c.get(),d.get(),e.get(),today,int(tn)))
            mydb.commit()
            messagebox.showinfo("Success","Successfully Added Into The Database!")
            w1.destroy()
            library()
        def confirm():
            t.configure(state='normal')
            t.insert(END,"The Name of the borrower is "+str(a.get()))
            t.insert(END,"\n\nThe Phone Number of the borrower is "+b.get())
            t.insert(END,"\n\nThe ID of the borrower is "+c.get())
            t.insert(END,"\n\nThe ID Number on ID "+c.get()+" of the borrower is "+d.get())
            t.insert(END,"\n\nThe Book issued is "+e.get())
            t.insert(END,"\n\nThe Date of issue is "+today)
            t.insert(END,"\n\nToken Number is {}".format(tn))
            t.configure(state='disabled')
            b3=Button(w1,text="Submit",command=lambda:submit(),bd=5).place(x=150,y=300)
        t=Text(w1,height=15,width=60)
        t.configure(state='disabled')
        t.place(x=300,y=50)
        l1=Label(w1,text="Enter Name").place(x=20,y=50)
        l2=Label(w1,text="Enter Phone number").place(x=20,y=100)
        l3=Label(w1,text="Enter ID Name").place(x=20,y=150)
        l4=Label(w1,text="Enter ID Number").place(x=20,y=200)
        l5=Label(w1,text="Enter Book").place(x=20,y=250)
        a=StringVar()
        b=StringVar()
        c=StringVar()
        d=StringVar()
        e=StringVar()
        f=StringVar()
        ae=Entry(w1,textvariable=a).place(x=150,y=50)
        be=Entry(w1,textvariable=b).place(x=150,y=100)
        ce=Entry(w1,textvariable=c).place(x=150,y=150)
        de=Entry(w1,textvariable=d).place(x=150,y=200)
        ee=Entry(w1,textvariable=e).place(x=150,y=250)
        b2=Button(w1,text="Confirm",command=lambda:confirm()).place(x=150,y=300)    
        w1.geometry('800x350')
        w1.resizable(False,False)
    def returnbook():
        w.destroy()
        w1=Tk()
        def returned():
            x=a.get()
            sql="select date from books where token_number=(%s)"
            val=(x,)
            mycursor.execute(sql,val)
            y=str(mycursor.fetchall())
            y=y[3:len(y)-4]
            mycursor.execute('select * from books')
            for z in mycursor:
                if int(x) in z:
                    d1 = datetime.strptime(str(today), "%Y-%m-%d")
                    d2 = datetime.strptime(str(y), "%Y-%m-%d")
                    delta = d2 - d1
                    if (int(delta.days) > 7):
                        messagebox.showwarning("Warning!","The submission is late by {} days".format(delta.days - 7))
            sql1="delete from books where token_number={}".format(int(x))
            mycursor.execute(sql1)
            mydb.commit()
            w1.destroy()
            messagebox.showinfo("Success","Done")
            library()  
        l=Label(w1,text="Enter the token number").place(x=0,y=20)
        a=StringVar()
        ae=Entry(w1,textvariable=a).place(x=150,y=20)
        b=Button(w1,text="Return Book",command=lambda:returned()).place(x=150,y=80)
        w1.geometry('300x300')
        w1.resizable(False,False)
    def finddate():
        w.destroy()
        w1=Tk()
        def showdate():
            mycursor.execute('select * from books')
            for z in mycursor:
                if a.get() in z:
                    mycursor.execute("select date from books where token_number = %s",(a.get(),))
                    y=mycursor.fetchall()
                    mycursor.execute("select book from books where token_number = %s",(a.get(),))
                    m=mycursor.fetchall()
                    y=str(y)
                    y=y[3:len(y)-4]
                    m=str(m)
                    m=m[3:len(m)-4]
                    d1 = datetime.strptime(str(today), "%Y-%m-%d")
                    d2 = datetime.strptime(str(y), "%Y-%m-%d")
                    delta = d2 - d1
                    messagebox.showinfo("Result","Remaining dates for returning book ({}) is: {} days".format(m,7 - delta.days))
                    w1.destroy()
                    library()
        a=IntVar()
        l1=Label(w1,text='Enter Token Number').place(x=20,y=20)
        ae=Entry(w1,textvariable=a).place(x=150,y=20)
        b1=Button(w1,text="Submit",command=lambda:showdate()).place(x=150,y=50)
        w1.geometry('290x80')
        w1.resizable(False,False)
    w=Tk()
    b1=Button(w,text="Issue Book",command=lambda:issuebook()).place(x=25,y=30)
    b2=Button(w,text="Return Book",command=lambda:returnbook()).place(x=25,y=80)
    b3=Button(w,text="Date Remaining",command=lambda:finddate()).place(x=25,y=130)
    w.geometry('150x170')
    w.resizable(False,False)
    w.mainloop()
library()