from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import date
import sqlite3
conn = sqlite3.connect('hospital.db')
cur = conn.cursor()
#Main page
Invoice=Tk()

window_width = 800
window_height = 800

w=Invoice.winfo_screenwidth()
h=Invoice.winfo_screenheight()
center_x = int(w/2 - window_width/2)
center_y = int(h/2 - window_height/2)

Invoice.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
Invoice.title("Invoice")
Invoice.iconbitmap('iamge/hospital-building.ico')

Invoice.resizable(False, False)
#Back ground Image
Back_ground=Image.open('iamge/2149103942 (1).jpg')
BackGroundTk=ImageTk.PhotoImage(Back_ground)

BackGroundlbl=Label(Invoice,image=BackGroundTk)
BackGroundlbl.place(relx=0,rely=0)
#Main Image
MainImage_path=Image.open("iamge/doctor-office-logo-template_23-2149665617.jpg")
MainImageTk=ImageTk.PhotoImage(MainImage_path)
#Image lbl
Imagelbl=Label(Invoice,image=MainImageTk)
Imagelbl.place(relx=0.09,rely=0.05)
#Invoice lbl
Invoicelbl=Label(Invoice,text='INVOICE',font=('Arial',20),fg="#f8f9fa",relief='solid',bg="#4cc9f0")
Invoicelbl.place(relx=0.75,rely=0.013)
#Health Care Group
Health_carelbl=Label(Invoice,text='HealthCare Group',font=('Arial',10),fg="#f8f9fa",bg="#4cc9f0",relief='groove')
Health_carelbl.place(relx=0.76,rely=0.06)
#New Cario
NewCariolbl=Label(Invoice,text='New Cario',font=('Arial',10),fg="#f8f9fa",bg="#4cc9f0",relief='groove')
NewCariolbl.place(relx=0.773,rely=0.088)
#Street
Streetlbl=Label(Invoice,text='Al Ahram Street',font=('Arial',10),fg="#f8f9fa",bg="#4cc9f0",relief='groove')
Streetlbl.place(relx=0.773,rely=0.115)
#Egypt 
Egyptlbl=Label(Invoice,text='Egypt',font=('Arial',10),fg="#f8f9fa",bg="#4cc9f0",relief='groove')
Egyptlbl.place(relx=0.8,rely=0.14)
#Date
today=date.today()
#Date lbl
Datelbl=Label(Invoice,text=today,font=('Arial',12,'bold'),fg='#f8f9fa',bg="#0466c8",relief='groove')
Datelbl.place(relx=0.8,rely=0.45)
#Date lbl txt
Datetxt_lbl=Label(Invoice,text="today date :",font=('Arial',12,'bold'),fg='#f8f9fa',bg="#0466c8",relief='groove')
Datetxt_lbl.place(relx=0.67,rely=0.45)


#Modern treatment
Modern_treatment_lbl=Label(Invoice,text='Modern treatment',font=('Arial',10),fg='#f8f9fa',bg="#72ddf7")
Modern_treatment_lbl.place(relx=0.09,rely=0.243)

#Best doctors
Best_doctors_lbl=Label(Invoice,text='Best doctors',font=('Arial',10),fg='#f8f9fa',bg="#72ddf7")
Best_doctors_lbl.place(relx=0.09,rely=0.268)
#Our goal is patient confidence
confidence_lbl=Label(Invoice,text='Our goal is patient confidence',fg='#f8f9fa',bg="#72ddf7")
confidence_lbl.place(relx=0.09,rely=0.295)
#Visa lbl
Visa_lvl=Label(Invoice,fg="#495057",bg="#0466c8",width=90,height=2,relief='groove')
Visa_lvl.place(relx=0.09,rely=0.5)
#Visa txt
Visa=Label(Invoice,text='Visa',font=('Arial',12,'bold'),fg="#f8f9fa",bg="#0466c8",height=1,relief='groove')
Visa.place(relx=0.097,rely=0.505)
#Name lbl
Name=Label(Invoice,text="Name :",font=('Arial',12,'bold'),fg='#f8f9fa',bg='#0466c8',relief='groove')
Name.place(relx=0.097,rely=0.55)
#Name Ent
NameVAr=StringVar()
Name_ent=Entry(Invoice,width=50,textvariable=NameVAr,bg="#0466c8",fg="white",relief="ridge")
Name_ent.place(relx=0.18,rely=0.555)
#Card Number lbl
Card_lbl=Label(Invoice,text="Card Number :",font=('Arial',12,'bold'),fg='#f8f9fa',bg='#0466c8',relief='groove')
Card_lbl.place(relx=0.097,rely=0.59)
#Card Ent
CardVar=StringVar()
Card_Ent=Entry(Invoice,width=50,textvariable=CardVar,bg="#0466c8",fg="white",relief="ridge")
Card_Ent.place(relx=0.25,rely=0.594)
#Expiration date lbl
Expiration_datelbl=Label(Invoice,text="Expiration date :",font=('Arial',12,'bold'),fg='#f8f9fa',bg='#0466c8',relief="groove")
Expiration_datelbl.place(relx=0.64,rely=0.59)
#Expiration date mont combobox
numberM = list(range(1, 13))
MonthVar = StringVar()
MonthVar.set(1)
monthbox = Combobox(Invoice, values=numberM, textvariable=MonthVar, width=2, state='readonly')
monthbox.place(relx=0.81, rely=0.595)
# Year combobox
numberY = list(range(2024, 2045))
YearVar = StringVar()
YearVar.set(2024)
yearbox = Combobox(Invoice, values=numberY, textvariable=YearVar, width=4, state='readonly')
yearbox.place(relx=0.86, rely=0.595)
#Security code lbl
Security_codelbl=Label(Invoice,text="Security code :",font=('Arial',12,'bold'),fg='#f8f9fa',bg='#0466c8',relief="ridge")
Security_codelbl.place(relx=0.57,rely=0.55)
#Security code Ent
SecurityVar=StringVar()
Security_codeEnt=Entry(Invoice,width=10,textvariable=SecurityVar,bg="#0466c8",fg="white",relief="groove")
Security_codeEnt.place(relx=0.73,rely=0.555)
#Func Check
def Check():
   name=NameVAr.get()
   number=CardVar.get()
   code=SecurityVar.get()
   month=MonthVar.get()
   year=YearVar.get()
   if name=="" or number=="" or code=="":
       messagebox.showerror('Data Error',"Please Enter Name,Card Number and Security code")
   elif len(number)!=16 or len(code)!=3:
       messagebox.showerror('Data Error',"Please Enter valid data!")
   else:
       try:
           number=int(number)
           code=int(code)
           ex_date=month+"/"+year
           cur.execute('''
               INSERT INTO visa (name, card_number, sec_code, ex_date)
               VALUES (?, ?, ?, ?)
           ''', (name, number, code, ex_date))
           conn.commit()
       except ValueError:
           messagebox.showwarning("Invalid Input", "Please enter valid values.")    
    
       
       
       messagebox.showinfo("Confirm","Payment has been completed successfully.")
#Payment confirmation btn
Payment_confirmationbtn=Button(Invoice,text="Payment confirmation",font=('Arial',15,'bold'),bg="#0466c8",fg='white',width=20,relief="groove",command=Check)
Payment_confirmationbtn.place(relx=0.57,rely=0.65)

Invoice.mainloop()
conn.close()