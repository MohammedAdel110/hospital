from tkinter import *
from tkinter import messagebox 
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
import sqlite3
conn = sqlite3.connect('hospital.db')
cur = conn.cursor()
# Sample medicine data


# Function to update the treeview with filtered data

def update_treeview():
    
    # Clear the existing rows in the treeview
    for row in treeview.get_children():
        treeview.delete(row)

    # Fetch data from the database
    cur.execute('SELECT * FROM medicines')
    fetched_medicines = cur.fetchall()


    # Insert each medicine into the treeview
    for med in fetched_medicines:
        treeview.insert("", END, values=med)
    

# Function to add a new medicine
def add_medicine():
    
    new_name = name_var.get()
    new_category = category_var.get()
    new_quantity = quantity_var.get()
    new_price = price_var.get()
    new_cost = cost_var.get()

    try:
        
        new_quantity = int(new_quantity)
        new_price = float(new_price)
        new_cost = float(new_cost)

        # Insert the new medicine into the database
        cur.execute('''
            INSERT INTO medicines (name, category, quantity_in_stock, price, cost)
            VALUES (?, ?, ?, ?, ?)
        ''', (new_name, new_category, new_quantity, new_price, new_cost))
        conn.commit()
        

        messagebox.showinfo('Notification', 'The medicine was added successfully')

        update_treeview()
        clear_inputs()
        
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter valid values.")
      

   
# Function to delete a selected medicine
def delete_medicine():
    try:
        selected_item = treeview.selection()[0]
        selected_medicine_id = treeview.item(selected_item)['values'][0]

        cur.execute('DELETE FROM medicines WHERE id=?', (selected_medicine_id,))
        conn.commit()
        

        messagebox.showinfo('Notification', 'The medicine was deleted successfully')

        update_treeview()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a medicine to delete.")


# Function to edit a selected medicine
def edit_medicine():
    try:
        
        selected_item = treeview.selection()[0]
        selected_medicine_id = treeview.item(selected_item)['values'][0]

        updated_name = name_var.get()
        updated_category = category_var.get()
        updated_quantity = int(quantity_var.get())
        updated_price = float(price_var.get())
        updated_cost = float(cost_var.get())

        cur.execute('UPDATE medicines SET name=?, category=?, quantity_in_stock=?, price=?, cost=? WHERE id=?', (updated_name, updated_category, updated_quantity, updated_price, updated_cost, selected_medicine_id))

        conn.commit()
        

        messagebox.showinfo('Notification', 'The medicine was updated successfully')

        update_treeview()
        clear_inputs()
    except (IndexError, ValueError):
        messagebox.showwarning("Selection Error", "Please select a medicine to edit and enter valid data.")


# Function to clear the input fields
def clear_inputs():
    name_var.set("")
    category_var.set("All")
    quantity_var.set("")
    price_var.set("")
    cost_var.set("")
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
buy_med_window.resizable(FALSE,FALSE)
#image
imagee=Image.open('iamge/medicinnn.jpg')
imageTkk=ImageTk.PhotoImage(imagee)
lbl=Label(buy_med_window,image=imageTkk)
lbl.place(relx=0,rely=0)
#label
title_label = Label(buy_med_window, text="update Medicine", font=("Arial", 20, "bold"),background='#ade8f4' )
title_label.grid(row=0, column=0,columnspan=4)
 






#treeview
treeview_frame = Frame(buy_med_window)
treeview_frame.grid(row=1, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")

treeview = Treeview(treeview_frame, columns=("id", "name", "category","quanity", "price", "cost"), show="headings")

treeview.column('id', width=50, anchor="center")
treeview.column('name', width=50, anchor="center")
treeview.column('category', width=200, anchor="center")
treeview.column('quanity', width=100, anchor="center")
treeview.column('price', width=50, anchor="center")
treeview.column('cost', width=50, anchor="center")

treeview.heading("id", text="ID")
treeview.heading("name", text="Name")
treeview.heading("category", text="Category")
treeview.heading("quanity", text="quanity")
treeview.heading("price", text="Price")
treeview.heading("cost", text="cost")

treeview.grid(row=0, column=0, sticky="nsew")

scrollbar = Scrollbar(treeview_frame, orient=VERTICAL, command=treeview.yview)
treeview.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')
treeview_frame.grid_rowconfigure(0, weight=1)
treeview_frame.grid_columnconfigure(0, weight=1)

# Buy button
buy_button = Button(buy_med_window, text="Buy Medicine",bg='#48cae4')
buy_button.grid(row=3, column=0, columnspan=4, pady=10)

buy_med_window.grid_columnconfigure(0, weight=1)
buy_med_window.grid_columnconfigure(1, weight=1)
buy_med_window.grid_columnconfigure(2, weight=1)
buy_med_window.grid_rowconfigure(2, weight=1)
update_treeview()



# Input fields and buttons for add/edit/delete



input_frame = Frame(buy_med_window,bg="")
input_frame.grid(row=3, column=0, columnspan=4, pady=10)

name_var = StringVar()
name_label=Label(input_frame, text="Name:",bg='#ade8f4')
name_label.grid(row=0, column=0)
name_entry=Entry(input_frame, textvariable=name_var)
name_entry.grid(row=0, column=1)

category_var = StringVar()
category_label=Label(input_frame, text="Category:",bg='#ade8f4')
category_label.grid(row=1, column=0)
category_entry=Entry(input_frame, textvariable=category_var)
category_entry.grid(row=1, column=1)

Quantity_label=Label(input_frame, text="Quantity:",bg='#ade8f4')
Quantity_label.grid(row=2, column=0)
quantity_var = StringVar()
Quantity_entry=Entry(input_frame, textvariable=quantity_var)
Quantity_entry.grid(row=2, column=1)

Price_label=Label(input_frame, text="Price:",bg='#ade8f4')
Price_label.grid(row=3, column=0)
price_var = StringVar()
Price_entry=Entry(input_frame, textvariable=price_var)
Price_entry.grid(row=3, column=1)

Cost_label=Label(input_frame, text="Cost:",bg='#ade8f4')
Cost_label.grid(row=4, column=0)
cost_var = StringVar()
Cost_entry=Entry(input_frame, textvariable=cost_var)
Cost_entry.grid(row=4, column=1)

add_button = Button(input_frame, text="Add Medicine", command=add_medicine, bg='#48cae4')
add_button.grid(row=5, column=0, pady=5)

edit_button = Button(input_frame, text="Edit Medicine", command=edit_medicine, bg='#48cae4')
edit_button.grid(row=5, column=1, pady=5)

delete_button = Button(input_frame, text="Delete Medicine", command=delete_medicine, bg='#48cae4')
delete_button.grid(row=5, column=2, pady=5)

#back func
def backk():
    buy_med_window.destroy()
    import doctor_page
#back button
back=Button(buy_med_window,text='back',relief='groove',bg='#48cae4',command=backk)
back.place(relx=0.1,rely=0.92)



buy_med_window.mainloop()

conn.close()