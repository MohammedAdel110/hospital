from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import date


#Main page
doctor_page=Tk()
doctor_page.title('Doctor Page')
doctor_page.iconbitmap('iamge/hospital-building.ico')

Width=doctor_page.winfo_screenwidth()
Hight=doctor_page.winfo_screenheight()



doctor_page.geometry(f'{Width}x{Hight}+{0}+{0}')
doctor_page.resizable(FALSE,FALSE)
#Left Frame

sidebar = tk.Frame(doctor_page, width=400, bg='#ade8f4',relief=RAISED,highlightbackground="blue", highlightcolor="black")
sidebar.pack(side="left", fill="y")
#User Image
userimage_path=Image.open('iamge/id-card.png')
userImageTk=ImageTk.PhotoImage(userimage_path)

UsereImagelbl=Label(doctor_page,image=userImageTk,bg="#ade8f4")
UsereImagelbl.place(relx=0.02,rely=0.06)
#User name label
userNamelbl=Label(doctor_page,text='User name',font=('Arial',15,'bold'),bg='#ade8f4',fg='#0077b6')
userNamelbl.place(relx=0.06,rely=0.077)
#UserEmail label
UserEmail=Label(doctor_page,text='User@gmail.com',font=('Arial',8,'bold'),bg='#ade8f4',fg='#6c757d')
UserEmail.place(relx=0.06,rely=0.1)
#log out func
def logout():
    doctor_page.destroy()
    import login
    
#logoutbtn
logoutbtn=Button(doctor_page,text='Log out',font=('Arial',10,'bold'),width=30,fg='#0077b6',bg='#48cae4',relief='groove',command=logout)
logoutbtn.place(relx=0.023,rely=0.15)
#Date
today=date.today()
#Date lbl
Datelbl=Label(doctor_page,text=today,font=('Arial',13,'bold'),fg='#03045e')
Datelbl.place(relx=0.9,rely=0.03)
#Date image
DateImage_path=Image.open('iamge/calendar.png')
DateImageTk=ImageTk.PhotoImage(DateImage_path)
Datashow=Label(doctor_page,image=DateImageTk)
Datashow.place(relx=0.95,rely=0.01)
#Today Date lbl
Today_Date_lbl=Label(doctor_page,text="Today's Date",font=('Arial',10,'bold'),fg="#6c757d")
Today_Date_lbl.place(relx=0.9,rely=0.01)
#Patients Booking image
bookImage=Image.open('iamge/doc appointment (1).jpg')
bookImage.resize((400,600))
bookTk=ImageTk.PhotoImage(bookImage)

#Patients Booking lbl
book_lbl=Label(doctor_page,image=bookTk)
book_lbl.place(relx=0.23,rely=0.15)
#Patients Booking text
bookText=Label(doctor_page,text="Patients Booking  ",font=('Arial',18,'bold'),fg="#0077b6")
bookText.place(relx=0.23,rely=0.12)
#Patients Booking btn func
def Patients_Booking_btn():
    doctor_page.destroy()
    import doctor_appointments
    
    
#Patients Booking btn
book_btn=Button(doctor_page,text='Review Patients Appointment',font=('Arial',13,'bold'),width=39,bg='#48cae4',fg='white',command=Patients_Booking_btn)
book_btn.place(relx=0.23,rely=0.72)
#Buy medicine
medicineImage_path=Image.open('iamge/doc update (1).jpg')
medicineImageTk=ImageTk.PhotoImage(medicineImage_path)
#medicin lbl
medicinlbl=Label(doctor_page,image=medicineImageTk)
medicinlbl.place(relx=0.6,rely=0.15)
#medicin text lbl
medicinTextlbl=Label(doctor_page,text='Medicine List',font=('Arial',18,'bold'),fg="#0077b6")
medicinTextlbl.place(relx=0.6,rely=0.119)

#medic func
def medic_list():
    doctor_page.destroy()
    import update_med
#medicin btn
medicin_btn=Button(doctor_page,text='Update Medicin',font=('Arial',13,'bold'),width=39,bg='#48cae4',fg='white',command=medic_list)
medicin_btn.place(relx=0.6,rely=0.72)










doctor_page.mainloop()