from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Main page
Bookpage = Tk()
Bookpage.title('Bookpage')
Bookpage.iconbitmap('C:/Users/121mo/OneDrive/Desktop/hospital/full project/iamge/hospital-building.ico')

Width = 1300
Hight = 800

GetWidth = Bookpage.winfo_screenwidth()
GetHight = Bookpage.winfo_screenheight()

centerWidth = int((GetWidth - Width) / 2)
centerHight = int((GetHight - Hight) / 2)
Bookpage.geometry(f'{Width}x{Hight}+{centerWidth}+{centerHight}')
Bookpage.resizable(FALSE, FALSE)

# Top Frame
TopFrame = Frame(Bookpage, width=400, bg='#ade8f4', relief=RAISED, highlightbackground="blue", highlightcolor="black", height=110)
TopFrame.pack(side="top", fill="x")

# Go home page
def goHome():
    Bookpage.destroy()
    import user_page1

# Home btn
Homebtn = Button(Bookpage, text='Home page', font=('Arial', 12, 'bold'), bg='#ade8f4', relief='flat', fg='#013a63', command=goHome)
Homebtn.place(relx=0.8, rely=0.02)

# Go medicin page
def medicin():
    Bookpage.destroy()
    import Buy_medic

# Buy medic btn
Buy_medic_btn = Button(Bookpage, text='Buy Medicin', font=('Arial', 12, 'bold'), bg='#ade8f4', relief='flat', fg='#013a63', command=medicin)
Buy_medic_btn.place(relx=0.9, rely=0.02)

# Book Now Label
Book_now_lbl = Label(Bookpage, text='BOOK NOW ', font=('Arial', 50, 'bold'), relief='solid', fg='#013a63', bg='#ade8f4')
Book_now_lbl.place(relx=0.38, rely=0.17)

# Book icon
book_icon_path = Image.open('C:/Users/121mo/OneDrive/Desktop/hospital/full project/iamge/medical-appointment (1).png')
book_iconTk = ImageTk.PhotoImage(book_icon_path)

# Book icon label
Book_icon_label = Label(Bookpage, image=book_iconTk, bg='#ade8f4')
Book_icon_label.place(relx=0.05, rely=0.03)

# Book Icon Text label
Booklabel = Label(Bookpage, text="Doctor's Appointment\n Booking", font=('Arial', 13, 'bold'), bg='#ade8f4', relief='flat', fg='#013a63')
Booklabel.place(relx=0.098, rely=0.04)

# Info label
infolbl = Label(Bookpage, height=30, width=80, bg='#91e5f6', relief='solid')
infolbl.place(relx=0.55, rely=0.4)

# Name lbl bar
namebar = Label(Bookpage, height=3, width=72, bg='white', relief='solid')
namebar.place(relx=0.57, rely=0.56)

# Book Appointment
Book_appointmentlbl = Label(Bookpage, text='Book Appointment', font=('Batang', 30, 'bold'), bg='#91e5f6', relief='flat', fg='#013a63')
Book_appointmentlbl.place(relx=0.63, rely=0.45)

# Name lbl
namelbl = Label(Bookpage, text="your full name:", font=('Batang', 10, 'bold'), fg="#9999a1", bg='white')
namelbl.place(relx=0.574, rely=0.572)

# Name Entry
nameVar = StringVar()
nameEnt = Entry(Bookpage, width=60, relief='solid', bg="white", textvariable=nameVar)
nameEnt.place(relx=0.652, rely=0.576)

# Phone lbl bar
phone_bar = Label(Bookpage, height=3, width=72, bg='white', relief='solid')
phone_bar.place(relx=0.57, rely=0.66)

# Phone lbl
phonelbl = Label(Bookpage, text='your number:', font=('Batang', 10, 'bold'), fg="#9999a1", bg='white')
phonelbl.place(relx=0.574, rely=0.676)

# Phone Entry
phoneVar = StringVar()
phoneEnt = Entry(Bookpage, width=60, relief='solid', bg="white", textvariable=phoneVar)
phoneEnt.place(relx=0.645, rely=0.679)

# Email bar
email_bar = Label(Bookpage, height=3, width=72, bg='white', relief='solid')
email_bar.place(relx=0.57, rely=0.76)

# Email labl
emaillbl = Label(Bookpage, text='your email:', font=('Batang', 10, 'bold'), fg="#9999a1", bg='white')
emaillbl.place(relx=0.58, rely=0.776)

# Email Entry
emailVar = StringVar()
emailEnt = Entry(Bookpage, width=60, relief='solid', bg="white", textvariable=emailVar)
emailEnt.place(relx=0.642, rely=0.778)

# Day-Month-Year lbl
Day_Month_Year = Label(Bookpage, text="Day-Month-Year", font=('Batang', 10, 'bold'), bg='#84d2f6', relief='solid')
Day_Month_Year.place(relx=0.58, rely=0.85)

# Day combobox
DayVar = StringVar()
daybox = Combobox(Bookpage, textvariable=DayVar, width=2, state='readonly')
daybox.place(relx=0.58, rely=0.88)

# Month combobox
numberM = list(range(1, 13))
MonthVar = StringVar()
MonthVar.set(1)
monthbox = Combobox(Bookpage, values=numberM, textvariable=MonthVar, width=2, state='readonly')
monthbox.place(relx=0.608, rely=0.88)

# Year combobox
numberY = list(range(2024, 2031))
YearVar = StringVar()
YearVar.set(2024)
yearbox = Combobox(Bookpage, values=numberY, textvariable=YearVar, width=4, state='readonly')
yearbox.place(relx=0.635, rely=0.88)

# Update_days
def update_days(*args):
    month = int(MonthVar.get())
    if month == 2:
        daybox['values'] = list(range(1, 29))
    elif month in [4, 6, 9, 11]:
        daybox['values'] = list(range(1, 31))
    else:
        daybox['values'] = list(range(1, 32))
    DayVar.set(1)

MonthVar.trace('w', update_days)
update_days()

# Book now btn
bookNow = Button(Bookpage, text='Book Now', font=('Batang', 10, 'bold'), bg='#013a63', fg='white', relief='groove', width=15)
bookNow.place(relx=0.85, rely=0.9)

# Book image
bookImage = Image.open('C:/Users/121mo/OneDrive/Desktop/hospital/full project/iamge/360_F_244582094_BTflxzaxlNDHk250JiOaPwAeC4487ns8.jpg')
bookImageTk = ImageTk.PhotoImage(bookImage)

# Image lbl
Imagelbl = Label(Bookpage, image=bookImageTk)
Imagelbl.place(relx=0.1, rely=0.45)

# Medical fields dictionary
medical_fields = {
    "Dentistry": "Ramy Khaled",
    "Orthopedics": "Ziad Kamal",
    "Pulmonology": "Ahmed Mohamed",
    "Cardiology": "Yusesef Hassan",
    "Ophthalmology": "Hossam Wael"
}

# Medical field label
medical_fieldlbbl = Label(Bookpage, text='Medical Field', font=('Batang', 10, 'bold'), bg='#84d2f6', relief='solid')
medical_fieldlbbl.place(relx=0.68, rely=0.85)

# Medical field combobox
medical_fieldsVar = StringVar()
medical_fieldsVar.set("Dentistry")
medical_field_combobox = Combobox(Bookpage, values=list(medical_fields.keys()), textvariable=medical_fieldsVar, width=13, state='readonly')
medical_field_combobox.place(relx=0.68, rely=0.88)

# Doctor name label
Doctor_lbl = Label(Bookpage, text="Doctor Name", font=('Batang', 10, 'bold'), bg='#84d2f6', relief='solid')
Doctor_lbl.place(relx=0.758, rely=0.85)

# Doctor name entry
DoctorsVar = StringVar()
doctor_name_entry = Entry(Bookpage, textvariable=DoctorsVar, width=16, state='readonly')
doctor_name_entry.place(relx=0.762, rely=0.88)

# Update doctor name based on medical field selection
def update_doctor_name(*args):
    selected_field = medical_fieldsVar.get()
    doctor_name = medical_fields.get(selected_field, "")
    DoctorsVar.set(doctor_name)

medical_fieldsVar.trace('w', update_doctor_name)
update_doctor_name()

Bookpage.mainloop()
