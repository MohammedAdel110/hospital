from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import sqlite3
# Create login window
login = Tk()

width = 700
height = 467
get_height = login.winfo_screenheight()
get_width = login.winfo_screenwidth()

Center_height = int((get_height - height) / 2)
Center_width = int((get_width - width) / 2)

login.title('Log-in')
login.geometry(f'{width}x{height}+{Center_width}+{Center_height}')
login.resizable(FALSE, FALSE)
login.iconbitmap("iamge/hospital-building.ico")

# Image
img = Image.open('iamge/4.jpg')
img.resize((350,467))
imgTK = ImageTk.PhotoImage(img)


lbl = Label(login, image=imgTK)
lbl.place(relwidth=0.5, relheight=1)

# Frame
frame = Frame(login)
frame.place(anchor='center', relx=0.75, rely=0.1) 

# Main label
Welcome_label = Label(frame, text="Welcome Back!",font=('Arial',20,'bold'),fg='#00b4d8')
Welcome_label.grid(row=2, column=0, columnspan=4)
#sign label
sign_label=Label(login,text='Sign into your account',font=('Arial',8,'bold'),fg='#48cae4')
sign_label.place(relx=0.6,rely=0.15)
#icons
icon_path=Image.open('iamge/email.png')                          
iconTk=ImageTk.PhotoImage(icon_path)   
iconlbl=Label(login,image=iconTk)
iconlbl.place(relx=0.6,rely=0.3)
#Ent Email
EmailVar=StringVar()
EmailVar.set('EmailName@Gmail.com')
Ent_Email=Entry(login,width=35,borderwidth=2,textvariable=EmailVar)
Ent_Email.place(relx=0.6,rely=0.38)
#Email label
Email=Label(login,text='Email:',font=('Arial',10,'bold'),fg='#00b4d8')
Email.place(relx=0.65,rely=0.31)
#password icon
password_icon=Image.open('iamge/12.png')
passwordTk=ImageTk.PhotoImage(password_icon)
passwordlbl=Label(login,image=passwordTk)
passwordlbl.place(relx=0.6,rely=0.45)
#password Entry
PasswordVar=StringVar()
passwordEnt=Entry(login,width=35,borderwidth=2,textvariable=PasswordVar,show='*')
passwordEnt.place(relx=0.6,rely=0.55)
#passwoerd label
passwordlbl=Label(login,text='password:',font=('Arial',10,'bold'),fg='#00b4d8')
passwordlbl.place(relx=0.65,rely=0.46)
#login button
def login_check():
    email = EmailVar.get()
    password = PasswordVar.get()
    try:
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        
        query = "SELECT * FROM patient_accounts WHERE mail = ? AND pass = ?"
        cursor.execute(query, (email, password))
        result = cursor.fetchone()
        query_doc = "SELECT * FROM doctors_accounts WHERE account = ? AND password = ?"
        cursor.execute(query_doc, (email, password))
        result_doc = cursor.fetchone()
        conn.close()

        if result:
            login.destroy()
            import user_page1
            
        elif result_doc:
            login.destroy()
            import doctor_page
        else:
            messagebox.showwarning("Login Failed", "Invalid email or password.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    
logintbtn=Button(login,text="Login",fg='White',bg='#48cae4',relief='groove',width=30,font=('Arial',10,'bold'),command=login_check)
logintbtn.place(relx=0.569,rely=0.7)
#create acc label
Createlbl=Label(login,text="Don't have an account? ",font=('Arial',10,'bold'),fg="#48cae4")
Createlbl.place(relx=0.569,rely=0.79)
####
def create():
    login.destroy()
    import create_acc


#Create nowbtn
Createnowbtn=Button(login,text='Create now',font=('Arial',8,'bold'),fg='White',relief='ridge',bg='#48cae4',command=create)
Createnowbtn.place(relx=0.8,rely=0.79)

login.mainloop()
