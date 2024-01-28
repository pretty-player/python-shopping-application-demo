import sqlite3
from tkinter.messagebox import *
import time
#import sys
import os
#sys.path.append('../../app')
# sqlite database connection
db_connect=sqlite3.connect('signup.db')
db_cursor=db_connect.cursor()

class Signup_Datas:

    def imageTObinary(photopath):
        with open(str(photopath),'rb') as photo:
            read_bytes=photo.read()
            photo.close()
        return read_bytes

    def insert_into(first_name,last_name,dob,email,phone,username,password,bio,photopath):
        insert_into_query="""
        INSERT INTO signup_users(first_name,last_name,dob,email,phone,username,password,bio,photo,extention)
        VALUES(?,?,?,?,?,?,?,?,?,?);
        """
        values_tuple=(first_name,last_name,dob,email,phone,username,password,bio,Signup_Datas.imageTObinary(photopath),photopath.split('.')[-1])
        try:
            db_cursor.execute(insert_into_query,values_tuple)
            db_connect.commit()
            showinfo("Success","Successfully Registered\nback to login")
        except(Exception):
            showwarning('warning','Number (or) Email (or) Username\nAlready registered')
            print(Exception)






