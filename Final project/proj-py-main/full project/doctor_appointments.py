from tkinter import *
from tkinter import messagebox 
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
import sqlite3
conn = sqlite3.connect('hospital.db')
cur = conn.cursor()
# Sample appointments data




# Function to update the treeview with filtered data
def update_treeview():
    
    for row in treeview.get_children():
        treeview.delete(row)
    cur.execute('SELECT patent_name,patent_number,patent_mail ,day || "-" || month || "-" || hour FROM appointments order by month')
    fetched_appoin = cur.fetchall()
    for med in fetched_appoin:
        treeview.insert("", END, values=med)
    
        
# Function to filter appointments
def filter_appointments():
    day = int(DayVar.get()) 
    month = int(MonthVar.get())

    if day and month:
        for row in treeview.get_children():
            treeview.delete(row)
        cur.execute('SELECT patent_name, patent_number, patent_mail, day || "-" || month || "-" || hour FROM appointments WHERE day=? AND month=? ORDER BY month',(day,month))
        fetched_appoin = cur.fetchall()
        for med in fetched_appoin:
            treeview.insert("", END, values=med)

    

    

# Function to reset the filter and show all appointments
def unfilter_appointments():
    for row in treeview.get_children():
        treeview.delete(row)
    cur.execute('SELECT patent_name,patent_number,patent_mail ,day || "-" || month || "-" || hour FROM appointments order by month')
    fetched_appoin = cur.fetchall()
    for med in fetched_appoin:
        treeview.insert("", END, values=med)

# Main window
buy_med_window = Tk()
buy_med_window.title("Doctor Appointments")
width = 700
height = 467
get_height = buy_med_window.winfo_screenheight()
get_width = buy_med_window.winfo_screenwidth()

Center_height = int((get_height - height) / 2)
Center_width = int((get_width - width) / 2)

buy_med_window.geometry(f'{width}x{height}+{Center_width}+{Center_height}')
buy_med_window.iconbitmap("iamge/hospital-building.ico")
buy_med_window.resizable(FALSE, FALSE)

# Background image
imagee = Image.open('iamge/medicinnn.jpg')
imageTkk = ImageTk.PhotoImage(imagee)
lbl = Label(buy_med_window, image=imageTkk)
lbl.place(relx=0, rely=0)

# Title label
title_label = Label(buy_med_window, text="Appointments", font=("Arial", 20, "bold"), background='#ade8f4')
title_label.grid(row=0, column=0, columnspan=4)

# Filter frame
filter_frame = Frame(buy_med_window, bg='')
filter_frame.grid(row=1, column=0, columnspan=4, pady=10)

# Day-Month label
Day_Month_Year = Label(filter_frame, text="Day-Month", font=('Batang', 10, 'bold'), bg='#84d2f6', relief='solid')
Day_Month_Year.grid(row=0, column=0, columnspan=3)

# Day combobox
DayVar = StringVar()
daybox = Combobox(filter_frame, textvariable=DayVar, width=2, state='readonly')
daybox.grid(row=1, column=0, columnspan=2)

# Month combobox
numberM = list(range(1, 13))
MonthVar = StringVar()
MonthVar.set(1)
monthbox = Combobox(filter_frame, values=numberM, textvariable=MonthVar, width=2, state='readonly')
monthbox.grid(row=1, column=2)

# Update days in the day combobox based on selected month
def update_days(*args):
    month = int(MonthVar.get())
    if month == 2:
        daybox['values'] = list(range(1, 29))
    elif month in [4, 6, 9, 11]:
        daybox['values'] = list(range(1, 31))
    else:
        daybox['values'] = list(range(1, 32))
    DayVar.set('')

MonthVar.trace('w', update_days)
update_days()

# Filter button
filter_button = Button(filter_frame, text="Filter", bg='#48cae4', command=filter_appointments)
filter_button.grid(row=2, column=0, columnspan=3, pady=5)

# Unfilter button
unfilter_button = Button(filter_frame, text="Unfilter", bg='#48cae4', command=unfilter_appointments)
unfilter_button.grid(row=3, column=0,columnspan=3)

# Treeview frame
treeview_frame = Frame(buy_med_window)
treeview_frame.grid(row=2, column=0, columnspan=4, pady=5, padx=10, sticky="nsew")

# Treeview 
treeview = Treeview(treeview_frame, columns=("name", "number", "mail", "date"), show="headings")
treeview.column('name', width=150, anchor="center")
treeview.column('number', width=200, anchor="center")
treeview.column('mail', width=200, anchor="center")
treeview.column('date', width=100, anchor="center")

treeview.heading("name", text="Name")
treeview.heading("number", text="Number")
treeview.heading("mail", text="Email")
treeview.heading("date", text="Date")

treeview.grid(row=0, column=0, sticky="nsew")

scrollbar = Scrollbar(treeview_frame, orient=VERTICAL, command=treeview.yview)
treeview.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')
treeview_frame.grid_rowconfigure(0, weight=1)
treeview_frame.grid_columnconfigure(0, weight=1)

# Back button function
def backk():
    buy_med_window.destroy()
    import doctor_page

# Back button
back = Button(buy_med_window, text="Back", relief='groove', bg='#48cae4', command=backk)
back.place(relx=0.1, rely=0.92)

# Initialize the treeview with all appointments
update_treeview()
buy_med_window.mainloop()
conn.close()

