from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter.ttk import Combobox, Treeview
import sqlite3

conn = sqlite3.connect('hospital.db')
cur = conn.cursor()
# Sample medicine data


# Function to update the treeview with filtered data
def update_treeview():
    try:
        for row in treeview.get_children():
            treeview.delete(row)
        cur.execute('SELECT name,category,price FROM medicines')
        fetched_medicine = cur.fetchall()
    
        for med in fetched_medicine:
            treeview.insert("", END, values=med)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    

# Function to filter medicines
def filter_medicines():
    try:
        category = category_var.get()
        name = name_var.get().lower()
        cur.execute('''
            SELECT name, category, price
            FROM medicines
            WHERE (? = "All" OR category = ?) AND name LIKE ?
        ''',(category, category, f'%{name}%'))
        fetched_medicine = cur.fetchall()
        for row in treeview.get_children():
            treeview.delete(row)
        for med in fetched_medicine:
            treeview.insert("", END, values=med)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
total_cost=0
# handle selected medicines 
def handle_purchase():
    selected_items = treeview.selection()
    selected_medicines = [treeview.item(item, 'values') for item in selected_items]
    if not selected_medicines:
        messagebox.showwarning("Warning", "Please select at least one medicine to buy.")
    else:
        try:
            global total_cost 
            
            for med in selected_medicines:
                med_name = med[0]
                price = float(med[2])  # Assuming the price is in the third column (index 2)
                total_cost += price 
                cur.execute("UPDATE medicines SET quantity_in_stock = quantity_in_stock - 1 WHERE name = ?", (med_name,))
                conn.commit()
            messagebox.showinfo("Total Cost", f"The current total cost is ${total_cost:.2f}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
        

# Main window
buy_med_window = Tk()
buy_med_window.title("Medicine Purchase")
width = 700
height = 467
get_height = buy_med_window.winfo_screenheight()
get_width = buy_med_window.winfo_screenwidth()

Center_height = int((get_height - height) / 2)
Center_width = int((get_width - width) / 2)

buy_med_window.geometry(f'{width}x{height}+{Center_width}+{Center_height}')
buy_med_window.iconbitmap("iamge/hospital-building.ico")
buy_med_window.resizable(FALSE, FALSE)
# Image
imagee = Image.open('iamge/medicinnn.jpg')
imageTkk = ImageTk.PhotoImage(imagee)
lbl = Label(buy_med_window, image=imageTkk)
lbl.place(relx=0, rely=0)
# Label
title_label = Label(buy_med_window, text="Buy Medicine", font=("Arial", 20, "bold"), background='#ade8f4')
title_label.grid(row=0, column=0, columnspan=4)
# Filter
filter_frame = Frame(buy_med_window, bg='')
filter_frame.grid(row=1, column=0, columnspan=4, pady=10)

#category box
category_lbl = Label(filter_frame, text="Category:", bg='#ade8f4')
category_lbl.grid(row=0, column=0, padx=5)
category_var = StringVar(value="All")
category_combobox = Combobox(filter_frame, textvariable=category_var, state="readonly")

cur.execute('SELECT DISTINCT category FROM medicines')
categories = cur.fetchall()
category_combobox["values"] = ["All"] + [cat[0] for cat in categories]

category_combobox.grid(row=0, column=1, padx=5)
#med box
med_label = Label(filter_frame, text="Name:", bg='#ade8f4')
med_label.grid(row=1, column=0, padx=5)
name_var = StringVar()
name_entry = Entry(filter_frame, textvariable=name_var)
name_entry.grid(row=1, column=1, padx=5)

filter_button = Button(filter_frame, text="Filter", command=filter_medicines, bg='#48cae4')
filter_button.grid(row=2, column=0, columnspan=3, pady=5)

# Treeview
treeview_frame = Frame(buy_med_window)
treeview_frame.grid(row=2, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")

treeview = Treeview(treeview_frame, columns=("name", "category", "price"), show="headings", selectmode="extended")
treeview.column('name', width=150, anchor="center")
treeview.column('category', width=200, anchor="center")
treeview.column('price', width=100, anchor="center")
treeview.heading("name", text="Name")
treeview.heading("category", text="Category")
treeview.heading("price", text="Price")
treeview.grid(row=0, column=0, sticky="nsew")

scrollbar = Scrollbar(treeview_frame, orient=VERTICAL, command=treeview.yview)
treeview.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')
treeview_frame.grid_rowconfigure(0, weight=1)
treeview_frame.grid_columnconfigure(0, weight=1)

# Buy button
buy_button = Button(buy_med_window, text="Add Medicines", command=handle_purchase, bg='#48cae4')
buy_button.grid(row=3, column=0, columnspan=4, pady=10)

buy_med_window.grid_columnconfigure(0, weight=1)
buy_med_window.grid_columnconfigure(1, weight=1)
buy_med_window.grid_columnconfigure(2, weight=1)
buy_med_window.grid_rowconfigure(2, weight=1)
update_treeview()

# Back function
def backk():
    buy_med_window.destroy()
    import user_page1

# Back button
back = Button(buy_med_window, text='Back', relief='groove', bg='#48cae4', command=backk)
back.place(relx=0.1, rely=0.92)

# Go to checkout function
def checkout():
    buy_med_window.destroy()
    import Invoice_page

# Go to checkout button
Go_checkoutbtn = Button(buy_med_window, text="Go to checkout", relief='groove', bg='#48cae4', command=checkout)
Go_checkoutbtn.place(relx=0.79, rely=0.92)
conn.commit()

buy_med_window.mainloop()
conn.close()