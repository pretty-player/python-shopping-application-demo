from tkinter import *
from tkcalendar import DateEntry
from tkinter import filedialog
from admin_window import Admin_window
from tkinter.messagebox import showinfo,showwarning
import tkinter
from after_login import *
import admin_window
import sqlite3
from catch_signup import *

app=tkinter.Tk()
app.title("Welcome Users")
app.config(bg='skyblue')
app.geometry('400x400')
app.resizable(False,False)

parent_frame=Frame(app,height=400,width=400)

parent_frame.pack(expand=1,fill=BOTH)
        
title_lbl=Label(parent_frame,text="Welcome 2 Shoping")
title_lbl.config(font=('times',23),fg='black')
title_lbl.pack(side='top')

def Admin():
    parent_frame.forget()

    admin_frame=Frame(app,height=400,width=400)
    admin_frame.config(bg='purple')
    admin_frame.pack(expand=True,fill=BOTH)

    admin_username=Entry(admin_frame)
    admin_username.config(font=('Times',15))
    admin_username.pack(side='top',ipadx=10,ipady=10,padx=20,pady=10)

    admin_password=Entry(admin_frame,show='*')
    admin_password.config(font=('Times',15))
    admin_password.pack(side='top',ipadx=10,ipady=10,padx=20,pady=10)

    def admin_login(admin_username,admin_password):
        if( admin_username=='admin' and admin_password=='admin'):
            Admin_window()
        else:
            showinfo('information','Not access for you')

    admin_btn=Button(admin_frame,text="Login",command=lambda : admin_login(admin_username.get(),admin_password.get()))
    admin_btn.config(bg='lightgreen',fg='white',font=('times bold',18))
    admin_btn.pack(side='top',ipadx=10,ipady=6,padx=20,pady=10)
    

    def back():
        parent_frame.pack(expand=True,fill=BOTH)
        admin_frame.forget()

    back_btn=Button(admin_frame,text="Back",command=back)
    back_btn.config(bg='lightgreen',fg='white',font=('times bold',10))
    back_btn.pack(side='bottom',ipadx=10,ipady=6,padx=20,pady=10)


def Login():
    parent_frame.forget()
    login_frame=Frame(app,height=400,width=400)
    login_frame.config(bg='purple')
    login_frame.pack(expand=True,fill=BOTH)

    title_lbl=Label(login_frame,text="Login")
    title_lbl.config(bg='purple',fg='black',font=('times',23))
    title_lbl.grid(row=0,columnspan=6,ipadx=3,ipady=3,padx=180,pady=6,sticky='w')


    username_lbl=Label(login_frame,text="Username")
    username_lbl.config(bg='purple',fg='black',font=('times',16))
    username_lbl.grid(row=1,column=0,ipadx=3,ipady=3,padx=6,pady=6,sticky='w')
    username_entry=Entry(login_frame)
    username_entry.config(font=('times',16))
    username_entry.grid(row=1,column=1,ipadx=3,ipady=3,sticky='w')
        
    passwd_lbl=Label(login_frame,text="Password")
    passwd_lbl.config(bg='purple',fg='black',font=('times',16))
    passwd_lbl.grid(row=2,column=0,ipadx=3,ipady=3,padx=6,pady=6,sticky='w')
    passwd_entry=Entry(login_frame,show='*')
    passwd_entry.config(font=('times',16))
    passwd_entry.grid(row=2,column=1,ipadx=3,ipady=3,sticky='w')    


    def post(username,password):
        if(username=='' or password==''):
            showwarning('warning','please fillout\nRequired fields')
        else:
            Client_login(username,password)
        

    login_btn=Button(login_frame,text='Login',command=lambda : post(username_entry.get(),passwd_entry.get()))
    login_btn.config(bg='green',fg='black',font=("Times",17))
    login_btn.grid(ipadx=4,ipady=4,row=3,column=1,pady=5)

    def forget_password(event):
        showinfo("information",'wait for implement')
        
    forget_lbl=Label(login_frame,text="Forget Password?",cursor='hand2')
    forget_lbl.config(fg='blue',bg='purple',font=('times',13,'underline'))
    forget_lbl.bind('<Button-1>',lambda event:forget_password(event))
    forget_lbl.grid(row=5,column=1,pady=10)


    def back():
        login_frame.forget()
        parent_frame.pack(expand=True,fill=BOTH)
        #admin_frame.forget()
        #login_frame.forget()

    back_btn=Button(login_frame,text="Back",command=back)
    back_btn.config(bg='lightgreen',fg='white',font=('times bold',10))
    back_btn.grid(row=6,column=1)



def Signup():
    parent_frame.forget()
    app.geometry('600x600')
    app.title('sign up')
    signup_frame=Frame(app,bg='skyblue',width=600,height=600)
    signup_frame.pack_propagate(0)

    photo_path={}
    fname_lbl=Label(signup_frame,text="First Name ")
    fname_lbl.config(bg='skyblue',fg='black',font=('times',16))
    fname_lbl.grid(row=0,column=0,ipadx=3,ipady=3,padx=6,pady=6,sticky='w')
    fname_entry=Entry(signup_frame)
    fname_entry.config(font=('times',16))
    fname_entry.grid(row=0,column=1,ipadx=3,ipady=3,sticky='w')
        
    #frame.pack(expand=True)
    lname_lbl=Label(signup_frame,text="Last Name ")
    lname_lbl.config(font=('times',16),bg='skyblue',fg='black')
    lname_lbl.grid(row=1,column=0,ipadx=3,ipady=3,padx=6,pady=6,sticky='w')
    lname_entry=Entry(signup_frame)
    lname_entry.config(font=('times',16))
    lname_entry.grid(row=1,column=1,ipadx=3,ipady=3,sticky='w')
        
        
    dob_lbl=Label(signup_frame,text="DOB ")
    dob_lbl.config(bg='skyblue',fg='black',font=('times',16))
    dob_lbl.grid(row=2,column=0,ipadx=3,ipady=3,padx=6,pady=6,sticky='w')
    dob_entry=DateEntry(signup_frame,selectmode='day')
    dob_entry.grid(row=2,column=1,ipadx=10,ipady=6,sticky='w')

    gender_lbl=Label(signup_frame,text="Gender ")
    gender_lbl.config(font=('times',16),bg='skyblue',fg='black')
    gender_lbl.grid(row=3,column=0,ipadx=3,ipady=3,padx=6,pady=6,sticky='w')
    gender_entry=Entry(signup_frame)
    gender_entry.config(font=('times',16))
    gender_entry.grid(row=3,column=1,ipadx=3,ipady=3,sticky='w')

        
    email_lbl=Label(signup_frame,text="Email address ")
    email_lbl.config(bg='skyblue',fg='black',font=('times',16))
    email_lbl.grid(row=4,column=0,ipadx=3,ipady=3,padx=6,pady=6,sticky='w')
    email_entry=Entry(signup_frame)
    email_entry.config(font=('times',16))
    email_entry.grid(row=4,column=1,ipadx=3,ipady=3,sticky='w')
        
        
    phone_lbl=Label(signup_frame,text="Phone No ")
    phone_lbl.config(bg='skyblue',fg='black',font=('times',16))
    phone_lbl.grid(row=5,column=0,ipadx=3,ipady=3,padx=6,pady=6,sticky='w')
    phone_entry=Entry(signup_frame)
    phone_entry.config(font=('times',16))
    phone_entry.grid(row=5,column=1,ipadx=3,ipady=3,sticky='w')
     
     
    username_lbl=Label(signup_frame,text="New Username ")
    username_lbl.config(bg='skyblue',fg='black',font=('times',16))
    username_lbl.grid(row=6,column=0,ipadx=3,ipady=3,padx=6,pady=6,sticky='w')
    username_entry=Entry(signup_frame)
    username_entry.config(font=('times',16))
    username_entry.grid(row=6,column=1,ipadx=3,ipady=3,sticky='w')
    
    passwd_lbl=Label(signup_frame,text="New Password ")
    passwd_lbl.config(bg='skyblue',fg='black',font=('times',16))
    passwd_lbl.grid(row=7,column=0,ipadx=3,ipady=3,padx=6,pady=6,sticky='w')
    passwd_entry=Entry(signup_frame)
    passwd_entry.config(font=('times',16))
    passwd_entry.grid(row=7,column=1,ipadx=3,ipady=3,sticky='w')
    
    cnfrm_passwd_lbl=Label(signup_frame,text="Confirm Password ")
    cnfrm_passwd_lbl.config(bg='skyblue',fg='black',font=('times',16))
    cnfrm_passwd_lbl.grid(row=8,column=0,ipadx=3,ipady=3,padx=6,pady=6,sticky='w')
    cnfrm_passwd_entry=Entry(signup_frame,show='*')
    cnfrm_passwd_entry.config(font=('times',16))
    cnfrm_passwd_entry.grid(row=8,column=1,ipadx=3,ipady=3,sticky='w')
    
    
    bio_lbl=Label(signup_frame,text="Address ")
    bio_lbl.config(bg='skyblue',fg='black',font=('times',16))
    bio_lbl.grid(row=9,column=0,ipadx=3,ipady=3,padx=6,pady=6,sticky='w')
    bio_entry=Text(signup_frame,height=3,width=20)
    bio_entry.config(font=('times',16))
    bio_entry.grid(row=9,column=1,ipadx=3,ipady=3,sticky='w')
       
        

    def browse_image():
        filename=filedialog.askopenfilename(initialdir="~/")
        img_lbl.config(text=filename.split('/')[-1])
        photo_path['filename']=filename

    browse_btn=Button(signup_frame,text="Browse Image",command=browse_image)
    browse_btn.grid(row=10,column=0,ipadx=3,ipady=3,pady=5,sticky='w')
        
        
        
    img_lbl=Label(signup_frame,text="slect image")
    img_lbl.config(bg='skyblue',fg='black',font=('times italic',13))
    img_lbl.grid(row=10,column=1,ipadx=3,ipady=3,padx=6,pady=6,sticky='w')

    def register():
        Signup_Datas()
        Signup_Datas.insert_into(fname_entry.get(),lname_entry.get(),dob_entry.get(),email_entry.get(),phone_entry.get(),username_entry.get(),passwd_entry.get(),bio_entry.get('1.0','end-1c'),photo_path['filename'])
    
    register_btn=Button(signup_frame,text='Register',command=register)
    register_btn.config(bg='green',fg='black',font=("Times",17))
    register_btn.grid(ipadx=6,ipady=6,row=11,column=1,pady=5)


    def back():
        #login_frame.forget()
        signup_frame.forget()
        app.geometry('400x400')
        parent_frame.config(height=400,width=400)
        parent_frame.pack(expand=1,fill=BOTH)
        #admin_frame.forget()
        #login_frame.forget()

    back_btn=Button(signup_frame,text="Back",command=back)
    back_btn.config(bg='lightgreen',fg='white',font=('times bold',10))
    back_btn.grid(row=11,column=2)
    signup_frame.pack()


admin_btn=Button(parent_frame,text="Admin",command=Admin)
admin_btn.config(font=('times',16),bg='green',fg='black')
admin_btn.pack(side='top',pady=13)

login_btn=Button(parent_frame,text="Login",command=Login)
login_btn.config(font=('times',16),bg='green',fg='black')
login_btn.pack(side='top',pady=5)


signup_btn=Button(parent_frame,text="Signup",command=Signup)
signup_btn.config(font=('times',16),bg='green',fg='black')
signup_btn.pack(side='top',pady=5)

product_db_initial_query= '''
        CREATE TABLE product_upload(
                             id INTEGER PRIMARY KEY,
                             product_name TEXT NOT NULL,
                             product_category TEXT NOT NULL,
                             product_quality TEXT NOT NULL,
                             product_price TEXT NOT NULL,
                             product_upload_date DATETIME,
                             product_discount TEXT,
                             product_color TEXT,
                             product_description TEXT,
                             product_image BLOB,
                             product_image_extention TEXT
                             );
        '''
        
users_db_query = '''
        CREATE TABLE signup_users (
                             id INTEGER PRIMARY KEY,
                             first_name TEXT NOT NULL,
                             last_name TEXT NOT NULL,
                             dob DATETIME,
                             gender TEXT,
                             email TEXT NOT NULL UNIQUE,
                             phone TEXT NOT NULL UNIQUE,
                             username TEXT NOT NULL UNIQUE,
                             password TEXT NOT NULL,
                             bio TEXT,
                             photo BLOB,
                             extention TEXT
                             );
                '''
    

def db_configuration():
    db_connect_users=sqlite3.connect('signup.db')
    db_cursor_users=db_connect_users.cursor()
    db_cursor_users.execute(users_db_query)
    
    
    db_connect_product=sqlite3.connect('product_upload.db')
    db_cursor_product=db_connect_product.cursor()
    db_cursor_product.execute(product_db_initial_query)
#db_configuration()
app.mainloop()








