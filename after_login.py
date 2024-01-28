from tkinter import *
from tkinter.messagebox import *
import tkinter
import sqlite3
import os
from PIL import ImageTk,Image
class Client_login:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        request_connect=sqlite3.connect('signup.db')
        request_cursor=request_connect.cursor()
        request_cursor.execute("SELECT * FROM signup_users WHERE username=?;",(username,))
        profile_datas=request_cursor.fetchall()

        if(len(profile_datas)<=0):
            showwarning('warning','please signup after login')

        else:
            app=tkinter.Toplevel()
            app.title('Welcome Users')
            app.config(bg='white')
            app.geometry('1200x600')

            users_info_frame=Frame(master=app,bg='#E5C6E4')
            users_info_frame.config(height=300,width=150,highlightbackground='white',highlightthickness=2)
            users_info_frame.pack_propagate(0)
        
            product_info_frame=Frame(master=app)
            product_info_frame.config(height=600,width=600)

            users_info_frame.pack(side='left',fill=BOTH,expand=True)




            image_name=profile_datas[0][7]+'.'+profile_datas[0][11]


            image_list=os.listdir()

            for x in range(len(image_list)-1):
                if(image_list[x]==image_name):
                    image_name= image_list[x]
                    break
                if(len(image_list)-2 == x):
                    with open(image_name,'wb') as write_photo:
                        write_photo.write(profile_datas[0][10])
                        write_photo.close()
                        image_name=image_name

            photo=Image.open(image_name)
            rz=photo.resize((200,200))
            final_photo=ImageTk.PhotoImage(rz)

            image_lbl=Label(users_info_frame,image=final_photo)
            image_lbl.pack(side='top')



            information_frame=Frame(users_info_frame)
            information_frame.config(bg='#E5C6E4',height=250,width=250)
            information_frame.pack(expand=True,fill=BOTH)

            name_lbl=Label(information_frame,text=profile_datas[0][1])
            name_lbl.config(font=('times',15),bg='lightblue',fg='black')
            name_lbl.pack(ipadx=3,ipady=3,padx=3,pady=3)

            phone_lbl=Label(information_frame,text='Register No :+91'+profile_datas[0][6])
            phone_lbl.config(font=('times',15),bg='lightblue',fg='black')
            phone_lbl.pack()


            home_image=Image.open('home.png')
            home_rz=home_image.resize((60,60))
            home_final=ImageTk.PhotoImage(home_rz)

            home_btn=Button(information_frame,text='HOME',image=home_final)
            home_btn.config(bg='lightgreen',fg='green')
            home_btn.pack()


            add_lbl=Label(information_frame)
            add_lbl.config(fg='blue',bg='#E5C6E4',font=('times',23))
            add_lbl.pack()

            confirm_btn=Button(information_frame,text='Continue')

            def hide():
                add_lbl['text']=''
                confirm_btn.pack_forget()

            confirm_btn.config(fg='black',bg='green',font=('times',13),width=10,height=3,command=hide)


            db_connect=sqlite3.connect('product_upload.db')
            db_cursor=db_connect.cursor()
            query='''
            SELECT * FROM product_upload;
            '''
            db_execute=db_cursor.execute(query)
            datas=db_execute.fetchall()

            scrl_bar=Scrollbar(product_info_frame)
            canvas_container=Canvas(product_info_frame,height=300,width=800,yscrollcommand=scrl_bar.set,bg='white')
            scrl_bar.pack(side='right',expand=1,fill='y',anchor='e')
            canvas_container.pack(expand=1,fill=BOTH,anchor='w',side='left')
            scrl_bar.config(command=canvas_container.yview)

            inside_canvas_frame=Frame(canvas_container)

            canvas_container.create_window(0,0,window=inside_canvas_frame)

            for x in range(0,len(datas)-1):
                elements_x_frame=Frame(master=inside_canvas_frame,height=250,width=900,bg='skyblue')
                elements_x_frame.pack_propagate(0)
                elements_x_frame.pack(pady=20,expand=1,fill='x')

                lbl_x=Label(elements_x_frame,text=datas[x][1].upper())
                lbl_x.config(font=('times 13 bold'),bg='skyblue',fg='black')
                lbl_x.pack(side='top')

                with open(datas[x][1]+"."+datas[x][10],'wb') as get_product_image:
                    get_product_image.write(datas[x][9])
                    get_product_image.close()

                product_image_name=Image.open(datas[x][1]+"."+datas[x][10])
                product_image_name_rz=product_image_name.resize((100,100))
                final_product_image_name=ImageTk.PhotoImage(product_image_name_rz)

                lbl_product_image_x=Label(elements_x_frame,image=final_product_image_name)
                lbl_product_image_x.image=final_product_image_name
                lbl_product_image_x.pack(side='top')

                price_lbl_x=Label(elements_x_frame,text='\u20B9 '+datas[x][4])
                price_lbl_x.config(font=('times 20 bold'),bg='skyblue',fg='black')
                price_lbl_x.pack(pady=10,side='top')

                def shipping_address():
                    add_lbl['text']='Shipping Address\n+--------------------+\n'+profile_datas[0][9]+"\n+--------------------+\nNote : Cash On Delivery"
                    confirm_btn.pack()


                buy_btn_x=Button(elements_x_frame,text='Buy',bg='green',fg='black',height=10,width=10,command=shipping_address)
                buy_btn_x.pack_propagate(0)
                buy_btn_x.pack(pady=10)







            product_info_frame.update()
            canvas_container.config(scrollregion=canvas_container.bbox('all'))




            product_info_frame.pack(side='right',fill=BOTH,expand=True)


            # request_connect=sqlite3.connect(os.path.realpath(r'../signup.db'))
        



            app.mainloop()


#Client_login('silambu','djska')