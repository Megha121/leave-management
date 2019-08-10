
from tkinter import *
from tkinter import messagebox as msg
from PIL import ImageTk,Image
import sqlite3
import scrolling_area
import ttkcalendar
import tkSimpleDialog


class CalendarDialog(tkSimpleDialog.Dialog):
    """Dialog box that displays a calendar and returns the selected date"""
    def body(self, master):
        self.calendar = ttkcalendar.Calendar(master)
        self.calendar.pack()

    def apply(self):
       self.result = self.calendar.selection


root= Tk()
root.title('LEAVE SUBMISSION ')
root.geometry('1366x768')
frame=Frame(root,width=1920,height=1080)
frame.place(x=0,y=0)
'''img=ImageTk.PhotoImage(Image.open("C:\\Users\\megha\\Desktop\\training project\\pppp.png"))
L=Label(frame,image=img)
L.place(x=0,y=0)'''




def main(root,frame):

    

    img898=ImageTk.PhotoImage(Image.open("C:\\Users\\megha\\Desktop\\training project\\pppp.png"))
    L=Label(frame,image=img898)
    L.place(x=0,y=0)
    B11=Button(frame,font=('Brittanic',20,'bold'),fg='orange',bg='black',width=25,borderwidth=8,text='REGISTER',command=lambda:emp(root,frame))
    B11.place(x=50,y=250)

    B22=Button(frame,font=('Brittanic',20,'bold'),fg='orange',bg='black',width=20,borderwidth=8,text='LOGIN AS ADMIN',command=lambda:login_page(root,frame))
    B22.place(x=50,y=460)

    B33=Button(frame,font=('Brittanic',20,'bold'),fg='orange',bg='black',width=15,borderwidth=8,text='HELP',command=lambda:HELP(root,frame))
    B33.place(x=1000,y=200)

    B44=Button(frame,font=('Brittanic',20,'bold'),fg='orange',bg='black',width=15,borderwidth=8,text='ABOUT',command=lambda:ABOUT(root,frame))
    B44.place(x=1000,y=300)

    B55=Button(frame,font=('Brittanic',20,'bold'),fg='orange',bg='black',width=15,borderwidth=8,text='CONTACT',command=lambda:CONTACT(root,frame))
    B55.place(x=1000,y=400)

    B66=Button(frame,font=('Brittanic',20,'bold'),fg='orange',bg='black',width=25,borderwidth=8,text='LOGIN AS EMPLOYEE',command=lambda:login_emp(root,frame))
    B66.place(x=50,y=360)
    frame.mainloop()
def ABOUT(root,frame):
    frame.destroy()
    frame=Frame(root,width=1800,height=1800)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open("C:\\Users\\megha\\Desktop\\training project\\pp.jpg"))
    L909=Label(frame,image=img)
    L909.place(x=0,y=0)

    #text = Text(frame)  
    #text.insert(INSERT, ("This project is designed under the rights of Megha Kaushik. This project is aimed at developing an online leave management system that is of importance to any organisation. This system can be used to automate the workflow of leave applications and their approvals. Leave Management application will reduce paper work and maintains record in more efficient way.") )
    #text.config(font=('times',17,'italic'))
    #text.insert(END, "For more information please contact on 869xxxxxxx or write an email to megha.kcse@gmail.com")   
    #text.pack()
    lab=Label(frame,text='''This project is designed under the rights of Megha Kaushik. This project
                            is aimed at developing an online leave management system that is of
                            importance to any organisation. This system can be used to automate the
                            workflow of leave applications and their approvals. Leave Management
                            application will reduce paper work and maintains record in more efficient way.''',font=('times',17,'italic'),bg='#2AA580')
    lab.place(x=55,y=5)
    b37=Button(frame,font=('courier',19,'bold'),bg='blue',fg='black',bd=7,text='BACK',command=lambda:BACK(root,frame))
    b37.place(x=500,y=550)
    frame.mainloop()

def HELP(root,frame):
        frame.destroy()
        frame=Frame(root,width=1800,height=1800)
        frame.place(x=0,y=0)
        img=ImageTk.PhotoImage(Image.open("C:\\Users\\megha\\Desktop\\training project\\helppicture.jpg"))
        L904=Label(frame,image=img)
        L904.place(x=0,y=0)
        b38=Button(frame,font=('courier',19,'bold'),fg='blue',bg='black',bd=7,text='BACK',command=lambda:BACK(root,frame))
        b38.place(x=500,y=550)
    
        frame.mainloop()
def data(E1,E2,E3,E4,E5,E6):
    a=E1.get()
    b=E2.get()
    c=E3.get()
    d=E4.get()
    e=E5.get()
    f=E6.get()

    if(a=='' or b=='' or c=='' or d=='' or e=='' or f==''):
        msg.showinfo('Warning','Incomplete Information')
    else:
        conn=sqlite3.connect('employee1.db')
        conn.execute('''create table if not exists dataentry
                (NAME TEXT NOT NULL,
                 EMPLOYEE_ID NOT NULL,
                 PASSWORD TEXT NOT NULL,
                 EMPLOYEE_DESIGNATION TEXT NOT NULL,
                 EMPLOYEE_CONTACT_NO int,
                 RESPONSE TEXT,
                 REASON TEXT NOT NULL);''')
        msg.showinfo('TITLE','Sucessfully Completed...')
        conn.commit()

        

def CONTACT(root,frame):
        frame.destroy()
        frame=Frame(root,width=1800,height=1800)
        frame.place(x=0,y=0)
        img=ImageTk.PhotoImage(Image.open("C:\\Users\\megha\\Desktop\\training project\\pp.jpg"))
        L909=Label(frame,image=img)
        L909.place(x=0,y=0)
        #B46=Button(frame,font=('courier',19,'bold'),bd=7,text='SELECT A DATE FOR LEAVE',command=lambda:ABOUT(frame))
        #B46.place(x=50,y=400)


        lab1=Label(frame,text='''You can contact on the Phone No. : 86969861xx.
                      or write an Email to : megha.kcse@gmail.com.''',font=('times',17,'italic'))
       
        lab1.place(x=55,y=5)
        b38=Button(frame,font=('courier',19,'bold'),bd=7,text='BACK',command=lambda:BACK(root,frame))
        b38.place(x=400,y=400)
        frame.mainloop()

def login_emp(root,frame):
    def getdate(frame):
         cd = CalendarDialog(frame)
         result = cd.result
         selected_date.set(result.strftime("%d-%m-%Y"))
         print(e1.get())
    
    
    frame.destroy()
    frame=Frame(root,width=1800,height=1800)

    
    frame.place(x=0,y=0)
    img=PhotoImage(file="projj.gif")
    L202=Label(frame,image=img)
    L202.image=img
    L202.place(x=0,y=0)
         
    selected_date= StringVar()
    date=StringVar()
    e1=Entry(frame,textvariable=selected_date,font=('courier',20,'bold'))
    e1.place(x=650,y=400)
    b1=Button(frame,font=('courier',19,'bold'),bd=7,text='SELECT A DATE FOR LEAVE',command=lambda:getdate(frame))
    b1.place(x=50,y=400)

    
    #txt=E21.get()
    #txt2=E2222.get()

    
    #print(txt)
    #print(txt2)
    
    L0=Label(frame,text='NAME',relief='raised',width= 23,height=2)
    L0.place(x=50,y=200)
    
    L2222=Label(frame,text='PASSWORD',relief='raised',width=23,height=2)
    L2222.place(x=50,y=300)
    
    E21=Entry(frame,font=('courier',19,'bold'),bd=7)
    E21.place(x=250,y=200)
    
    E2222=Entry(frame,show='*',font=('courier',19,'bold'),bd=7)
    E2222.place(x=250,y=300)

    B77=Button(frame,font=('Brittanic',20,'bold'),fg='red',bg='white',width=20,borderwidth=8,
               text='LOGIN',command=lambda:login_success(root,frame))
    B77.place(x=150,y=500)




    B38=Button(frame,font=('Brittanic',20,'bold'),fg='red' ,bg='white',width=20,borderwidth=8,
              text='BACK',command=lambda:BACK(root,frame))
    B38.place(x=150,y=600)


    def login_success(root,frame):
            txt=E21.get()
            txt2=E2222.get()
            conn=sqlite3.connect('employee.db')
            cursor=conn.execute('Select NAME,PASSWORD from dataentry')
            c=cursor.fetchall()
            print(c)
            if( c[0][0]==txt and c[0][1]==txt2):
                msg.showinfo('Title','Login Success...')
                frame.destroy()
                frame=Frame(root,width=1800,height=1800)
                frame.place(x=0,y=0)

                img=ImageTk.PhotoImage(Image.open("C:\\Users\\megha\\Desktop\\training project\\proooo.png"))
                L121=Label(frame,image=img)
                L121.place(x=0,y=0)                      

                B89=Button(frame,font=('courier',20,'bold'),fg='lightgreen' ,bg='blue',width=20,borderwidth=20,
                      text='CHECK YOUR LEAVE',command=lambda:login_success(root,frame))
                B89.place(x=500,y=150)
                B90=Button(frame,font=('courier',20,'bold'),fg='lightgreen' ,bg='blue',width=20,borderwidth=20,
                      text='REQUEST',command=lambda:REQUEST(root,frame))

                B90.place(x=500,y=350)
                B91=Button(font=('courier',20,'bold'),fg='lightgreen' ,bg='blue',width=20,borderwidth=20,
                      text='LOGOUT',command=lambda:LOGOUT(root,frame))
                B91.place(x=500,y=550)



                
            else: 
                conn.commit()

            frame.mainloop()
    
def login_page(root,frame):
        frame.destroy()
        frame=Frame(root,width=1800,height=1800)
        frame.place(x=0,y=0)
        img=ImageTk.PhotoImage(Image.open("C:\\Users\\megha\\Desktop\\training project\\pp.jpg"))
        L910=Label(frame,image=img)
        L910.place(x=0,y=0)

        conn=sqlite3.connect('employee1.db')
        cursor=conn.execute('select NAME,EMPLOYEE_ID,EMPLOYEE_DESIGNATION,EMPLOYEE_CONTACT_NO,REASON  from dataentry ')
        
        scl=scrolling_area.Scrolling_Area(frame,height=300,width=1500)
        scl.place(x=0,y=0)
        table=scrolling_area.Table(scl.innerframe,
                                     ['NAME','EMPLOYEE_ID','EMPLOYEE_DESGNATION','EMPLOYEE_CONTACT_NO','REASON'],
                                     column_minwidths=[322,322,322,322,322] 
                                   )
        table.pack(expand=True,fill=X)
        table.on_change_data(scl.update_viewport)
        data=[]
        for row in cursor:
            column=[]
            data.append(column)
            for r in row:
                print(r)
                column.append(r)
        table.set_data(data)    
                        
        B45=Button(frame,font=('Brittanic',20,'bold'),fg='red',bg='white',width=20,borderwidth=8,
               text='ACCEPT',command=lambda:ACCEPT(root,frame,E14,E15))
        B45.place(x=20,y=550)
        B46=Button(frame,font=('Brittanic',20,'bold'),fg='red',bg='white',width=20,borderwidth=8,
                   text='REJECT',command=lambda:REJECT(root,frame,E14,E15))
        B46.place(x=800,y=550)

        L14=Label(frame,text='EMPLOYEE_ID',relief='raised',width=23,height=2)
        L14.place(x=50,y=400)

        L15=Label(frame,text='NAME',relief='raised',width=23,height=2)
        L15.place(x=50,y=450)

        
        E14=Entry(frame,font=('courier',19,'bold'),bd=7)
        E14.place(x=250,y=400)
        txt1=E14.get()
        print(txt1)
        E15=Entry(frame,font=('courier',19,'bold'),bd=7)
        E15.place(x=250,y=450)
        txt2=E15.get()
        print(txt2)


        B1000=Button(frame,font=('courier',19,'bold'),fg='red', bg='white',width=20,text='BACK',bd=7,command=lambda:BACK(root,frame))
        B1000.place(x=450,y=600)
        frame.mainloop()

        '''def ACCEPT(root,frame):
            frame.destroy()
            frame=Frame(root,width=1800,height=1800)
            frame.place(x=0,y=0)'''
        
            
        
    
def REQUEST(root,frame):
    frame.destroy()
    frame=Frame(root,width=1800,height=1800)
    frame.place(x=0,y=0)
    
    img=ImageTk.PhotoImage(Image.open("C:\\Users\\megha\\Desktop\\training project\\pp.jpg"))
    L131=Label(frame,image=img)
    L131.place(x=0,y=0)

    def SUBMIT_HERE(root,frame):
        txt34=E.get()
        if txt34=='':
            msg.showwarning('Title','details required')
        else:
            msg.showinfo('Title','SUBMITTED SUCCESSFULLY')
            main(root,frame)

        
            
    
    
    L01=Label(frame,font=('courier',19,'bold'),text='PLEASE ENTER YOUR REASON HERE',relief='raised',bd=7)
    L01.place(x=50,y=200)
    
    E=Entry(frame,font=('courier',19,'bold'))
    E.place(x=50,y=500)
    
    B100=Button(frame,font=('courier',19,'bold'),fg='blue', bg='brown',width=20,text='SUBMIT HERE',bd=7,command=lambda:SUBMIT_HERE(root,frame))
    B100.place(x=550,y=600)

    
    frame.mainloop()
    
def emp(root,frame):
    
    frame.destroy()
    frame=Frame(root,width=1800,height=1800)
    frame.place(x=0,y=0)

    img=ImageTk.PhotoImage(Image.open("C:\\Users\\megha\\Desktop\\training project\\i1.jpg"))
    L111=Label(frame,image=img)
    L111.place(x=0,y=0)
    
    conn=sqlite3.connect('employee1.db')
    conn.execute('''create table if not exists dataentry
                (NAME TEXT NOT NULL,
                 EMPLOYEE_ID NOT NULL,
                 PASSWORD TEXT NOT NULL,
                 EMPLOYEE_DESIGNATION TEXT NOT NULL,
                 EMPLOYEE_CONTACT_NO int,
                 RESPONSE int,
                 REASON TEXT NOT NULL);''')
    def write(root,frame):
        
        txt=E.get()
        txt1=E1.get()
        txt2=E2.get()
        txt3=E3.get()
        txt4=E4.get()
        #txt5=E5.get()
        
        print(txt)
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        #print(txt5)
        conn=sqlite3.connect('employee1.db')
        conn.execute("INSERT INTO dataentry(NAME,EMPLOYEE_ID,PASSWORD,EMPLOYEE_DESIGNATION,EMPLOYEE_CONTACT_NO,RESPONSE,REASON)VALUES('%s','%s','%s','%s',%d,'%d','%s')"%(txt,txt1,txt2,txt3,int(txt4),txt5))
        cursor=conn.execute('select * from dataentry')
        for row in cursor:
             print('NAME=',row[0])
             print('EMPLOYEE_ID=',row[1])
             print('PASSWORD=',row[2])
             print('EMPLOYEE_DESIGNATION=',row[3])
             print('EMPLOYEE_CONTACT_NO=',row[4])
             print('RESPONSE',row[5])
             #print('REASON=',row[6])
         
        conn.commit()
        conn.close()
        submit(root,frame)

    L=Label(frame,text='NAME',relief='raised',width= 23,height=2)
    L.place(x=50,y=200)


    L1=Label(frame,text='EMPLOYEE_ID',relief='raised',width=23,height=2)
    L1.place(x=50,y=250)

    L2=Label(frame,text='PASSWORD',relief='raised',width=23,height=2)
    L2.place(x=50,y=300)

    
    L3=Label(frame,text='EMPLOYEE_DESIGNATION',relief='raised',width=23,height=2)
    L3.place(x=50,y=350)

    L4=Label(frame,text='EMPLOYEE_CONTACT_NO',relief='raised',width=23,height=2)
    L4.place(x=50,y=400)

    #L5=Label(frame,text='REASON',relief='raised',width=23,height=2)
    #L5.place(x=50,y=450)

    
    #B7=Button(frame,font=('courier',19,'bold'),fg='red' ,bg='white',width=20,
              #text='NEXT',command=lambda:NEXT(root,frame))
    #B7.place(x=150,y=500)

    B8=Button(frame,font=('courier',19,'bold'),fg='red' ,bg='white',width=20,
              text='BACK',command=lambda:BACK(root,frame))
    B8.place(x=150,y=600)

    E=Entry(frame,font=('courier',19,'bold'),bd=7)
    E.place(x=250,y=200)

    E1=Entry(frame,font=('courier',19,'bold'),bd=7)
    E1.place(x=250,y=250)

    E2=Entry(frame,show='*',font=('courier',19,'bold'),bd=7)
    E2.place(x=250,y=300)

    E3=Entry(frame,font=('courier',19,'bold'),bd=7)
    E3.place(x=250,y=350)
    
    E4=Entry(frame,font=('courier',19,'bold'),bd=7)
    E4.place(x=250,y=400)
    
    #E5=Entry(frame,font=('courier',19,'bold'),bd=7)
    #E5.place(x=250,y=450)

    
    frame.mainloop()
    


def ACCEPT(root,frame,E14,E15):
    val1='1'
    Id= E14.get()
    Name=E15.get()
    conn=sqlite3.connect('employee1.db')
    conn.execute('''UPDATE dataentry SET RESPONSE='%s' WHERE EMPLOYEE_ID='%s' and NAME='%s' '''%(val1,Id,Name))
    conn.commit()

def REJECT(root,frame,E14,E15):
    val0='0'
    Id= E14.get()
    Name=E15.get()
        
    conn=sqlite3.connect('employee1.db')
    conn.execute('''UPDATE dataentry SET RESPONSE='%s' WHERE EMPLOYEE_ID='%s' and NAME='%s' '''%(val0,Id,Name))
    conn.commit()


def BACK(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=786)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open("C:\\Users\\megha\\Desktop\\training project\\pppp.png"))
    
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    main(root,frame)  
    frame.mainloop()

def LOGOUT(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=786)
    frame.place(x=0,y=0)
    print(root)
    root.destroy()
    root.quit()
    


'''def NEXT(root,frame):
     def getdate(frame):
         cd = CalendarDialog(frame)
         result = cd.result
         selected_date.set(result.strftime("%d-%m-%Y"))
         print(e1.get())
    
     frame.destroy()
     frame=Frame(width=1366,height=768)
     frame.place(x=0,y=0)
     img1=ImageTk.PhotoImage(Image.open("C:\\Users\\megha\\Desktop\\training project\\proooo.png"))
     L34=Label(frame,image=img1)
     L34.place(x=0,y=0)



     
     selected_date= StringVar()
     date=StringVar()
     e1=Entry(frame,textvariable=selected_date,font=('courier',32,'bold'))
     e1.place(x=650,y=400)
     b1=Button(frame,font=('courier',29,'bold'),fg='blue',bg='yellow',width=20,text='Choose a date',command=lambda:getdate(frame))
     b1.place(x=50,y=400)
     b22=Button(frame,font=('courier',19,'bold'),fg='pink' ,bg='blue',width=20,
              text='BACK',command=lambda:BACK(root,frame))
     b22.place(x=450,y=600)
     b33=Button(frame,font=('courier',19,'bold'),fg='blue', bg='yellow',width=20,text='NEXT')
     b33.place(x=450,y=550)
     
     frame.mainloop()'''


    
main(root,frame)
