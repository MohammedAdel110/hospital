from tkinter import *
from tkinter import messagebox 
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview

# Sample medicine data
medicines = [
    {"id": 1, "name": "Paracetamol", "category": "Relief","quanity": 10, "price": 10, "cost": 5},
    {"id": 2, "name": "Paracetamol", "category": "Relief","quanity": 10, "price": 10, "cost": 5},
   {"id": 3, "name": "Paracetamol", "category": "Relief","quanity": 10, "price": 10, "cost": 5},
  {"id": 4, "name": "Paracetamol", "category": "Relief","quanity": 10, "price": 10, "cost": 5}
 
   
]

# Filtered medicine data
filtered_medicines = medicines.copy()

# Function to update the treeview with filtered data
def update_treeview():
    for row in treeview.get_children():
        treeview.delete(row)
    for med in filtered_medicines:
        treeview.insert("", END, values=(med['id'], med['name'], med['category'],med['quanity'], med['price'], med['cost']))

# Function to filter medicines
def filter_medicines():
    global filtered_medicines
    category = category_var.get()
    name = name_var.get().lower()

    # Initialize the filtered_medicines list
    filtered_medicines = []

    # Loop through the medicines list and apply the filter conditions
    for med in medicines:
        if (category == "All" or category == med["category"]) and name in med["name"].lower():
            filtered_medicines.append(med)

    update_treeview()


# Function to add a new medicine
def add_medicine():
    new_id = len(medicines) + 1
    new_name = name_var.get()
    new_category = category_var.get()
    new_quantity = int(quantity_var.get())
    new_price = float(price_var.get())
    new_cost = float(cost_var.get())

    new_medicine = {"id": new_id, "name": new_name, "category": new_category, "quanity": new_quantity, "price": new_price, "cost": new_cost}
    medicines.append(new_medicine)
    filtered_medicines.append(new_medicine)
    update_treeview()
    clear_inputs()
# Function to delete a selected medicine
def delete_medicine():
    selected_item = treeview.selection()[0]
    selected_medicine_id = treeview.item(selected_item)['values'][0]
    for med in medicines:
        if med["id"] == selected_medicine_id:
            medicines.remove(med)
            break
        for med in filtered_medicines:
            if med["id"] == selected_medicine_id:
                filtered_medicines.remove(med)
                break
    update_treeview()

# Function to edit a selected medicine
def edit_medicine():
    selected_item = treeview.selection()[0]
    selected_medicine_id = treeview.item(selected_item)['values'][0]
    for med in medicines:
        if med["id"] == selected_medicine_id:
            med["name"] = name_var.get()
            med["category"] = category_var.get()
            med["quanity"] = int(quantity_var.get())
            med["price"] = float(price_var.get())
            med["cost"] = float(cost_var.get())
            break
    for med in filtered_medicines:
        if med["id"] == selected_medicine_id:
            med["name"] = name_var.get()
            med["category"] = category_var.get()
            med["quanity"] = int(quantity_var.get())
            med["price"] = float(price_var.get())
            med["cost"] = float(cost_var.get())
            break
    update_treeview()
    clear_inputs()

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
imagee=Image.open('C:/Users/121mo/OneDrive/Desktop/hospital/full project/iamge/medicinnn.jpg')
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