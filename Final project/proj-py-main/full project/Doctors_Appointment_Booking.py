from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime, timedelta
import sqlite3
conn = sqlite3.connect('hospital.db')
cur = conn.cursor()
# Main page
Bookpage = Tk()
Bookpage.title('Bookpage')
Bookpage.iconbitmap('iamge/hospital-building.ico')

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
book_icon_path = Image.open('iamge/medical-appointment (1).png')
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
Day_Month_Year = Label(Bookpage, text="Day-Month", font=('Batang', 10, 'bold'), bg='#84d2f6', relief='solid')
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

#booking func
def book():
    name=nameVar.get()
    number=phoneVar.get()
    email=emailVar.get()
    day=DayVar.get()
    month=MonthVar.get()
    hour=timeVar.get()
    doc_name=DoctorsVar.get()
    medical_field=medical_fieldsVar.get()
    if name =='' or number=='' or email=='':
        messagebox.showerror("Error","Please fill all data")
    
    else:
        try:
            cur.execute('INSERT INTO appointments (patent_name,patent_number,patent_mail ,day,month ,hour,doctor_name,medical_field) VALUES (?, ?, ?,?,?,?,?,?)', (name,number,email,day,month,hour,doc_name,medical_field))
            conn.commit()
            
            messagebox.showinfo('notification','You booked the doctor sucessfully')
        except:
            messagebox.showwarning("Selection Error", "Please select a diffrent time.")
        
        
    
    

# Book now btn
bookNow = Button(Bookpage, text='Book Now', font=('Batang', 10, 'bold'), bg='#013a63', fg='white', relief='groove', width=15,command=book)
bookNow.place(relx=0.85, rely=0.9)

# Book image
bookImage = Image.open('iamge/360_F_244582094_BTflxzaxlNDHk250JiOaPwAeC4487ns8.jpg')
bookImageTk = ImageTk.PhotoImage(bookImage)

# Image lbl
Imagelbl = Label(Bookpage, image=bookImageTk)
Imagelbl.place(relx=0.1, rely=0.45)

# Medical field combobox
cur.execute("SELECT DISTINCT medical_field FROM doctors_accounts")
medical_fields=cur.fetchall()

medical_fieldsVar = StringVar()
medical_fieldsVar.set("select")

medical_fieldcombobox = Combobox(Bookpage, values=medical_fields, textvariable=medical_fieldsVar, width=11, state='readonly')
medical_fieldcombobox.place(relx=0.69, rely=0.88)

# Medical field lbl
medical_fieldlbbl = Label(Bookpage, text='medical field', font=('Batang', 10, 'bold'), bg='#84d2f6', relief='solid')
medical_fieldlbbl.place(relx=0.69, rely=0.85)

# Update medical field based on doctor selection
def update_doctors(*args):
    selected_field = medical_fieldsVar.get()
    if selected_field:  # Handle case where no field is selected
        cur.execute("SELECT first_name  FROM doctors_accounts WHERE medical_field=?", (selected_field,))
        doctors = cur.fetchall()
        doctors = [doctor[0] for doctor in doctors]
        Doctor_combobox['values'] = doctors
        Doctor_combobox.set("select")




# Doctor name combobox

doctors=[]
DoctorsVar = StringVar()
medical_fieldsVar.trace('w', update_doctors)
DoctorsVar.set("select")

Doctor_combobox = Combobox(Bookpage, values=doctors, textvariable=DoctorsVar, width=13, state='readonly')
Doctor_combobox.place(relx=0.76, rely=0.88)

# Doctor name lbl
Doctor_lbl = Label(Bookpage, text="Doctor name", font=('Batang', 10, 'bold'), bg='#84d2f6', relief='solid')
Doctor_lbl.place(relx=0.76, rely=0.85)


#Determine the time lbl
Determine_time=Label(Bookpage, text="Determine the time :", font=('Batang', 10, 'bold'), bg='#84d2f6', relief='solid')
Determine_time.place(relx=0.58,rely=0.91)
#generate timee
timeVar=StringVar()
timeVar.set("12:00")

def generate_schedule(start_time, end_time, interval_minutes):
    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")
    schedule = []
    current_time = start
    while current_time <= end:
        schedule.append(current_time.strftime("%H:%M"))
        current_time += timedelta(minutes=interval_minutes)
    return schedule
start_time = "12:00"
end_time = "22:00"
interval_minutes = 30

schedule = generate_schedule(start_time, end_time, interval_minutes)
#Determine the time combobox
Timecombox=Combobox(Bookpage,values=schedule,textvariable=timeVar,width=8,state='readonly')
Timecombox.place(relx=0.69,rely=0.91)
#PM label
pm=Label(Bookpage,text="PM",font=('arial',8,'bold'),bg='white',relief='solid')
pm.place(relx=0.747,rely=0.91)



Bookpage.mainloop()
conn.close()