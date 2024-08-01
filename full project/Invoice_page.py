from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import date
 
#Main page
Invoice=Tk()

window_width = 800
window_height = 900

w=Invoice.winfo_screenwidth()
h=Invoice.winfo_screenheight()
center_x = int(w/2 - window_width/2)
center_y = int(h/2 - window_height/2)

Invoice.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
Invoice.title("Invoice")
Invoice.iconbitmap('C:/Users/121mo/OneDrive/Desktop/hospital/iamge/hospital-building.ico')

Invoice.resizable(False, False)
#Main Image
MainImage_path=Image.open("C:/Users/121mo/OneDrive/Desktop/hospital/full project/iamge/doctor-office-logo-template_23-2149665617.jpg")
MainImageTk=ImageTk.PhotoImage(MainImage_path)
#Image lbl
Imagelbl=Label(Invoice,image=MainImageTk)
Imagelbl.place(relx=0.09,rely=0.05)
#Invoice lbl
Invoicelbl=Label(Invoice,text='INVOICE',font=('Arial',20),fg="#03045e")
Invoicelbl.place(relx=0.75,rely=0.01)
#Health Care Group
Health_carelbl=Label(Invoice,text='HealthCare Group',font=('Arial',10),fg="#495057")
Health_carelbl.place(relx=0.76,rely=0.043)
#New Cario
NewCariolbl=Label(Invoice,text='New Cario',font=('Arial',10),fg="#495057")
NewCariolbl.place(relx=0.768,rely=0.062)
#Street
Streetlbl=Label(Invoice,text='Al Ahram Street',font=('Arial',10),fg="#495057")
Streetlbl.place(relx=0.773,rely=0.084)
#Egypt 
Egyptlbl=Label(Invoice,text='Egypt',font=('Arial',10),fg="#495057")
Egyptlbl.place(relx=0.8,rely=0.0999)
#Date
today=date.today()
#Date lbl
Datelbl=Label(Invoice,text=today,font=('Arial',12,'bold'),fg='#03045e')
Datelbl.place(relx=0.8,rely=0.4)
#Date lbl txt
Datetxt_lbl=Label(Invoice,text="today date :",font=('Arial',12,'bold'),fg='#03045e')
Datetxt_lbl.place(relx=0.67,rely=0.4)


#Modern treatment
Modern_treatment_lbl=Label(Invoice,text='Modern treatment',font=('Arial',10),fg="#495057")
Modern_treatment_lbl.place(relx=0.09,rely=0.22)

#Best doctors
Best_doctors_lbl=Label(Invoice,text='Best doctors',font=('Arial',10),fg="#495057")
Best_doctors_lbl.place(relx=0.09,rely=0.24)
#Our goal is patient confidence
confidence_lbl=Label(Invoice,text='Our goal is patient confidence',font=('Arial',10),fg="#495057")
confidence_lbl.place(relx=0.09,rely=0.26)
#Visa lbl
Visa_lvl=Label(Invoice,fg="#495057",bg="#90e0ef",width=90,height=2)
Visa_lvl.place(relx=0.09,rely=0.5)
#Visa txt
Visa=Label(Invoice,text='Visa',font=('Arial',12,'bold'),fg="#495057",bg="#90e0ef",height=1)
Visa.place(relx=0.097,rely=0.505)
#Name lbl
Name=Label(Invoice,text="Name :",font=('Arial',12,'bold'),fg='#0077b6')
Name.place(relx=0.097,rely=0.55)
#Name Ent
NameVAr=StringVar()
Name_ent=Entry(Invoice,width=50,textvariable=NameVAr,bg="#48cae4",fg="white",relief="ridge")
Name_ent.place(relx=0.18,rely=0.555)
#Card Number lbl
Card_lbl=Label(Invoice,text="Card Number :",font=('Arial',12,'bold'),fg='#0077b6')
Card_lbl.place(relx=0.097,rely=0.59)
#Card Ent
CardVar=StringVar()
Card_Ent=Entry(Invoice,width=50,textvariable=CardVar,bg="#48cae4",fg="white",relief="ridge")
Card_Ent.place(relx=0.25,rely=0.594)
#Expiration date lbl
Expiration_datelbl=Label(Invoice,text="Expiration date :",font=('Arial',12,'bold'),fg='#48cae4')
Expiration_datelbl.place(relx=0.61,rely=0.59)
#Expiration date mont combobox
numberM = list(range(1, 13))
MonthVar = StringVar()
MonthVar.set(1)
monthbox = Combobox(Invoice, values=numberM, textvariable=MonthVar, width=2, state='readonly')
monthbox.place(relx=0.773, rely=0.595)
# Year combobox
numberY = list(range(2024, 2045))
YearVar = StringVar()
YearVar.set(2024)
yearbox = Combobox(Invoice, values=numberY, textvariable=YearVar, width=4, state='readonly')
yearbox.place(relx=0.82, rely=0.595)
#Security code lbl
Security_codelbl=Label(Invoice,text="Security code :",font=('Arial',12,'bold'),fg='#48cae4')
Security_codelbl.place(relx=0.57,rely=0.55)
#Security code Ent
SecurityVar=StringVar()
Security_codeEnt=Entry(Invoice,width=10,textvariable=SecurityVar,bg="#48cae4",fg="white",relief="ridge")
Security_codeEnt.place(relx=0.73,rely=0.555)
#Func Check
def Check():
   name=NameVAr.get()
   number=CardVar.get()
   code=SecurityVar.get()
   if name=="" and number=="" and code=="":
       messagebox.showerror('Data Error',"Please Enter Name,Card Number and Security code")
   elif name=="" and number!="" and code!="":
       messagebox.showerror('Data Error',"Please Enter Name")
   elif name!="" and number=="" and code!="":
       messagebox.showerror('Data Error',"Please Enter Card Number")
   elif name!="" and number!="" and code=="":
       messagebox.showerror('Data Error',"Please Enter Security code")
   elif name!="" and number=="" and code=="":
       messagebox.showerror('Data Error',"Please Enter Card Number and Security code")
   elif name=="" and number!="" and code=="":
       messagebox.showerror('Data Error',"Please Enter Name and Card  Security code")
   elif name=="" and number=="" and code!="":
       messagebox.showerror('Data Error',"Please Enter Name and Card Number")
   else:
       messagebox.showinfo("Confirm","Payment has been completed successfully.")
#Payment confirmation btn
Payment_confirmationbtn=Button(Invoice,text="Payment confirmation",font=('Arial',15,'bold'),bg="#0096c7",fg='white',width=20,relief="groove",command=Check)
Payment_confirmationbtn.place(relx=0.57,rely=0.65)

Invoice.mainloop()