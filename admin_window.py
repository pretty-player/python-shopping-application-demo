# pretty_player

import os
from tkinter import *
import tkinter
from tkinter import filedialog
from tkinter.messagebox import *
from PIL import ImageTk,Image
from tkcalendar import DateEntry
import sqlite3
from PIL import ImageTk,Image
from admin_product_insert import Product_insert
class Admin_window:
    def __init__(self):
        self.app=tkinter.Toplevel()
        self.app.title('admin portal')
        self.app.geometry('1200x600')

        # Database connect 
        self.db_connect=sqlite3.connect('signup.db')
        self.db_cursor=self.db_connect.cursor()
        # End database connect

        # Icon configuration

        self.profile_close_icon=Image.open('left_arrow_icon.jpeg')
        self.profile_close_icon_rz=self.profile_close_icon.resize((20,20))
        self.final_profile_close_icon=ImageTk.PhotoImage(self.profile_close_icon_rz)
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        self.profile_open_icon=Image.open('profile_icon.jpeg')
        self.profile_open_icon_rz=self.profile_open_icon.resize((20,20))
        self.final_profile_open_icon=ImageTk.PhotoImage(self.profile_open_icon_rz)
        # End icon configuration


        # Parent Frame
        self.parent_frame=Frame(self.app,height=600,width=1200,bg='red')


        # Left side window configuration
        self.left_side_frame=Frame(self.parent_frame,bg='#E0CACA',width=400,height=600)

        def profile_open_callback():
            self.left_side_frame.pack(side='left',expand=True,fill='y',anchor='w')
            self.left_side_frame.pack_propagate(0)


        def profile_close_callback():
            self.left_side_frame.forget() 
        # close btn
        self.close_profile_btn=Button(master=self.left_side_frame,image=self.final_profile_close_icon,command=profile_close_callback)
        self.close_profile_btn.pack(side='top',anchor='e')
        # End close btn

        # Left Details frame
        self.details_frame=Frame(self.left_side_frame,bg='#E0CACA',width=400,height=300)

        self.categorized_products_lbl=Label(self.details_frame,text="Categorized Products")
        self.categorized_products_lbl.config(fg='green',bg='#E0CACA',font=('times',18))
        self.categorized_products_lbl.pack(side='top')


        self.total_categorized_products_lbl=Label(self.details_frame,text="5")
        self.total_categorized_products_lbl.config(fg='green',bg='#E0CACA',font=('times',18))
        self.total_categorized_products_lbl.pack(side='top')


        self.uncategorized_products_lbl=Label(self.details_frame,text="UnCategorized Products")
        self.uncategorized_products_lbl.config(fg='green',bg='#E0CACA',font=('times',18))
        self.uncategorized_products_lbl.pack(side='top')

        self.total_uncategorized_products_lbl=Label(self.details_frame,text="0")
        self.total_uncategorized_products_lbl.config(fg='green',bg='#E0CACA',font=('times',18))
        self.total_uncategorized_products_lbl.pack(side='top')

        self.whole_products_lbl=Label(self.details_frame,text="Total Products")
        self.whole_products_lbl.config(fg='green',bg='#E0CACA',font=('times',18))
        self.whole_products_lbl.pack(side='top')

        self.total_whole_products_lbl=Label(self.details_frame,text="5")
        self.total_whole_products_lbl.config(fg='green',bg='#E0CACA',font=('times',18))
        self.total_whole_products_lbl.pack(side='top')

        self.details_frame.pack_propagate(0)
        #self.details_frame.pack(expand=1,fill=BOTH,side='top',anchor='w')  
        # End Left details frame


        # users frame left side window
        self.users_details_frame=Frame(self.left_side_frame,bg='#E0CACA',width=400,height=300)

        self.male_lbl=Label(self.users_details_frame,text="Total Male")
        self.male_lbl.config(fg='green',bg='#E0CACA',font=('times',18))
        self.male_lbl.pack(side='top')


        self.total_male_lbl=Label(self.users_details_frame,text="1")
        self.total_male_lbl.config(fg='green',bg='#E0CACA',font=('times',18))
        self.total_male_lbl.pack(side='top')


        self.female_lbl=Label(self.users_details_frame,text="Total Female")
        self.female_lbl.config(fg='green',bg='#E0CACA',font=('times',18))
        self.female_lbl.pack(side='top')

        self.total_female_lbl=Label(self.users_details_frame,text="0")
        self.total_female_lbl.config(fg='green',bg='#E0CACA',font=('times',18))
        self.total_female_lbl.pack(side='top')

        self.whole_members_lbl=Label(self.users_details_frame,text="Total Registered Members")
        self.whole_members_lbl.config(fg='green',bg='#E0CACA',font=('times',18))
        self.whole_members_lbl.pack(side='top')

        self.total_whole_members_lbl=Label(self.users_details_frame,text="1")
        self.total_whole_members_lbl.config(fg='green',bg='#E0CACA',font=('times',18))
        self.total_whole_members_lbl.pack(side='top')

        self.users_details_frame.pack_propagate(0)
        self.users_details_frame.pack(expand=1,fill=BOTH,side='top',anchor='w')

        # End Users left side Frame
        self.left_side_frame.pack(side='left',expand=True,fill='y',anchor='w')
        self.left_side_frame.pack_propagate(0)
        # End Left side window configuration




        # Right side window configuration product usermanagement
        self.usermanagement_frame=Frame(self.parent_frame,bg='skyblue',width=1000,height=600)
        self.usermanagement_frame.pack(side='right',expand=True,fill=BOTH)
        #self.usermanagement_frame.pack_propagate(0)
        # profile open btn

        self.open_profile_btn_user=Button(master=self.usermanagement_frame,image=self.final_profile_open_icon,command=profile_open_callback)
        self.open_profile_btn_user.pack(side='top',anchor='w')
        # End profile open btn

        # Users details for admin view
        #++++++++++++++++++++++++++++++++#


        self.db_query='''
        SELECT * FROM signup_users;
        '''
        self.db_query_execute=self.db_cursor.execute(self.db_query)
        self.db_fetch_rows=self.db_query_execute.fetchall()


        # Loop for users details


        self.scrl_bar=Scrollbar(self.usermanagement_frame)
        #self.scrl_bar.pack_propagate(0)
        self.canvas_container=Canvas(self.usermanagement_frame,width=1000,height=600,yscrollcommand=self.scrl_bar.set,bg='skyblue')
        self.scrl_bar.pack(side='right',expand=1,fill='y',anchor='e')
        self.canvas_container.pack(expand=1,fill=BOTH,anchor='w',side='left')
        self.scrl_bar.config(command=self.canvas_container.yview)
        #self.scrl_bar.pack(side='right',expand=1,fill='y',anchor='e')
        
        self.inside_canvas_frame=Frame(self.canvas_container)
        
        self.canvas_container.create_window(0,0,window=self.inside_canvas_frame)
        
        # waiting for looping
        #print(self.db_fetch_rows[0][6]+","+self.db_fetch_rows[0][10])

        for image in range(0,len(self.db_fetch_rows)):
            with open(self.db_fetch_rows[image][7]+"."+self.db_fetch_rows[image][11],'wb') as self.write_photo:
                self.write_photo.write(self.db_fetch_rows[image][10])
                self.write_photo.close()

        for x in range(0,len(self.db_fetch_rows)):
            self.elements_x=Frame(master=self.inside_canvas_frame,height=300,width=1200,bg='skyblue')
            self.elements_x.pack_propagate(0)

            self.profile_name_x=Label(self.elements_x,text="Name :"+self.db_fetch_rows[x][1],bg='skyblue',fg='black')
            self.profile_name_x.config(font=('times 13 bold'))
            self.profile_name_x.pack(expand=1,fill=BOTH)
            #-------------------------------------------------------------------#
            self.open_image_x=Image.open(self.db_fetch_rows[x][7]+"."+self.db_fetch_rows[x][11])
            self.open_image_x_rz=self.open_image_x.resize((100,100))
            self.photo=ImageTk.PhotoImage(self.open_image_x_rz)
            self.lbl_x=Label(master=self.elements_x,image=self.photo)
            self.lbl_x.image=self.photo
            self.lbl_x.pack()


            self.username_x=Label(self.elements_x,text="Username :@"+self.db_fetch_rows[x][7],bg='skyblue',fg='black')
            self.username_x.config(font=('times 13 bold'))
            self.username_x.pack(expand=1,fill=BOTH)

            self.elements_x.pack(pady=20,expand=1,fill='x')
        # End for looping

        self.usermanagement_frame.update()
        self.canvas_container.config(scrollregion=self.canvas_container.bbox('all'))
        #self.canvas_container.pack(expand=1,fill=BOTH)
        #self.inside_canvas_frame.pack(expand=1,fill=BOTH)

        



        # End loop for users details

        #print(self.db_fetch_rows[1])
        self.db_connect.close()

        #++++++++++++++++++++++++++++++++#
        # End Users details for admin view


        # End Right side window configuration usermanagement

        # Right side window configuration product explore
        self.product_explore_frame=Frame(self.parent_frame,bg='skyblue',width=1000,height=600)
        # profile open btn
        self.open_profile_btn_explore=Button(master=self.product_explore_frame,image=self.final_profile_open_icon,command=profile_open_callback)
        self.open_profile_btn_explore.pack(side='top',anchor='w')
        # End profile open btn
        self.product_explore_frame.pack_propagate(0)

        def product_explore_update():
            explore_db_connect=sqlite3.connect('product_upload.db')
            explore_db_cursor=explore_db_connect.cursor()
            explore_query='''
            SELECT * FROM product_upload;
            '''
            explore_db_execute=explore_db_cursor.execute(explore_query)
            explore_datas=explore_db_execute.fetchall()

            # print(explore_datas[0][9])


            explore_scrl_bar=Scrollbar(self.product_explore_frame)

            explore_canvas_container=Canvas(self.product_explore_frame,width=1000,height=600,yscrollcommand=explore_scrl_bar.set,bg='skyblue')
            explore_scrl_bar.pack(side='right',expand=1,fill='y',anchor='e')
            explore_canvas_container.pack(expand=1,fill=BOTH,anchor='w',side='left')
            explore_scrl_bar.config(command=explore_canvas_container.yview)
            # .scrl_bar.pack(side='right',expand=1,fill='y',anchor='e')
        
            explore_inside_canvas_frame=Frame(explore_canvas_container)
        
            explore_canvas_container.create_window(0,0,window=explore_inside_canvas_frame)

            # Looping for all products
            for x in range(0,len(explore_datas)-1):
                elements_x_frame=Frame(master=explore_inside_canvas_frame,height=300,width=1200,bg='skyblue')
                elements_x_frame.pack_propagate(0)
                elements_x_frame.pack(pady=20,expand=1,fill='x')


                '''


                details_txt=explore_datas[x][3]+" Quality\n\n"+explore_datas[x][6]+"% Discount\n\n"+explore_datas[x][7].upper()+" Color\n\n"+explore_datas[x][5]+" uploaded\n\n"+"NOTE : "+explore_datas[x][8]
            

                explore_quality=Label(elements_x_frame,text=details_txt)
                explore_quality.config(font=('times 10'))
                explore_quality.pack(side='right',expand=1,fill='y',anchor='e')


                '''
                lbl_x=Label(elements_x_frame,text=explore_datas[x][1].upper())
                lbl_x.config(font=('times 13 bold'),bg='skyblue',fg='black')
                lbl_x.pack(side='top')

                with open(explore_datas[x][1]+"."+explore_datas[x][10],'wb') as get_product_image:
                    get_product_image.write(explore_datas[x][9])
                    get_product_image.close()

                product_image_name=Image.open(explore_datas[x][1]+"."+explore_datas[x][10])
                product_image_name_rz=product_image_name.resize((100,100))
                final_product_image_name=ImageTk.PhotoImage(product_image_name_rz)

                lbl_product_image_x=Label(elements_x_frame,image=final_product_image_name)
                lbl_product_image_x.image=final_product_image_name
                lbl_product_image_x.pack(side='top')

                price_lbl_x=Label(elements_x_frame,text='\u20B9 '+explore_datas[x][4])
                price_lbl_x.config(font=('times 20 bold'),bg='skyblue',fg='black')
                price_lbl_x.pack(pady=10,side='top')

                def product_details_function():
                    pass

                view_btn=Button(elements_x_frame,text="View",bg='green',fg='black',command=product_details_function)
                view_btn.pack(pady=10,ipadx=20,ipady=3)

             

            # End looping for all products



            self.product_explore_frame.update()
            explore_canvas_container.config(scrollregion=explore_canvas_container.bbox('all'))


            # End Right side window configuration explore



        # Right side window configuration product insert
        self.product_insert_frame=Frame(self.parent_frame,bg='skyblue',width=1000,height=600)




        # profile open btn
        self.open_profile_btn_insert=Button(master=self.product_insert_frame,image=self.final_profile_open_icon,command=profile_open_callback)
        self.open_profile_btn_insert.pack(side='top',anchor='w')
        # End profile open btn


        self.product_insert_signup_frame=Frame(self.product_insert_frame,bg='skyblue',width=700,height=700)
        self.product_insert_signup_frame.pack_propagate(0)

        self.product_name_lbl=Label(self.product_insert_signup_frame,text='Product Name')
        self.product_name_lbl.config(font=('times bold',14),bg='skyblue',fg='black')
        self.product_name_lbl.grid(row=0,column=0,ipadx=3,ipady=3,padx=4,pady=4,sticky='w')

        self.product_name_entry=Entry(self.product_insert_signup_frame)
        self.product_name_entry.config(font=('times bold',14))
        self.product_name_entry.grid(row=0,column=1,sticky='e')


        self.product_category_lbl=Label(self.product_insert_signup_frame,text='Product Category')
        self.product_category_lbl.config(font=('times bold',14),bg='skyblue',fg='black')
        self.product_category_lbl.grid(row=1,column=0,ipadx=3,ipady=3,padx=4,pady=4,sticky='w')

        self.product_category_entry=Entry(self.product_insert_signup_frame)
        self.product_category_entry.config(font=('times bold',14))
        self.product_category_entry.grid(row=1,column=1,sticky='e')

        self.product_quality_lbl=Label(self.product_insert_signup_frame,text='Product Quality')
        self.product_quality_lbl.config(font=('times bold',14),bg='skyblue',fg='black')
        self.product_quality_lbl.grid(row=2,column=0,ipadx=3,ipady=3,padx=4,pady=4,sticky='w')

        self.product_quality_entry=Entry(self.product_insert_signup_frame)
        self.product_quality_entry.config(font=('times bold',14))
        self.product_quality_entry.grid(row=2,column=1,sticky='e')

        self.product_price_lbl=Label(self.product_insert_signup_frame,text='Product Price')
        self.product_price_lbl.config(font=('times bold',14),bg='skyblue',fg='black')
        self.product_price_lbl.grid(row=3,column=0,ipadx=3,ipady=3,padx=4,pady=4,sticky='w')


        self.product_price_entry=Entry(self.product_insert_signup_frame)
        self.product_price_entry.config(font=('times bold',14))
        self.product_price_entry.grid(row=3,column=1,sticky='e')

        self.product_upload_date_lbl=Label(self.product_insert_signup_frame,text='Upload Date')
        self.product_upload_date_lbl.config(font=('times bold',14),bg='skyblue',fg='black')
        self.product_upload_date_lbl.grid(row=4,column=0,ipadx=3,ipady=3,padx=4,pady=4,sticky='w')

        self.product_upload_date_entry=Entry(self.product_insert_signup_frame)
        self.product_upload_date_entry.config(font=('times bold',14))
        self.product_upload_date_entry.grid(row=4,column=1,sticky='e')


        self.product_discount_lbl=Label(self.product_insert_signup_frame,text='Discount')
        self.product_discount_lbl.config(font=('times bold',14),bg='skyblue',fg='black')
        self.product_discount_lbl.grid(row=6,column=0,ipadx=3,ipady=3,padx=4,pady=4,sticky='w')

        self.product_discount_entry=Entry(self.product_insert_signup_frame)
        self.product_discount_entry.config(font=('times bold',14))
        self.product_discount_entry.grid(row=6,column=1,sticky='e')

        self.product_color_lbl=Label(self.product_insert_signup_frame,text='Product Color')
        self.product_color_lbl.config(font=('times bold',14),bg='skyblue',fg='black')
        self.product_color_lbl.grid(row=7,column=0,ipadx=3,ipady=3,padx=4,pady=4,sticky='w')

        self.product_color_entry=Entry(self.product_insert_signup_frame)
        self.product_color_entry.config(font=('times bold',14))
        self.product_color_entry.grid(row=7,column=1,sticky='e')


        self.product_description_lbl=Label(self.product_insert_signup_frame,text='Product Description')
        self.product_description_lbl.config(font=('times bold',14),bg='skyblue',fg='black')
        self.product_description_lbl.grid(row=8,column=0,ipadx=3,ipady=3,padx=4,pady=4,sticky='w')

        self.product_description_entry=Text(self.product_insert_signup_frame,height=3,width=20)
        self.product_description_entry.config(font=('times bold',14))
        self.product_description_entry.grid(row=8,column=1,sticky='e')


        self.product_image_lbl=Label(self.product_insert_signup_frame,text='Nothing selected')
        self.product_image_lbl.config(font=('times bold',14),bg='skyblue',fg='black')
        self.product_image_lbl.grid(row=9,column=1,ipadx=3,ipady=3,padx=4,pady=4,sticky='e')

        self.photo_path={}

        def browse_image():
            #showinfo('browse','image browse')
            filename=filedialog.askopenfilename(initialdir="~/")
            self.photo_path['image_path']=filename
            self.product_image_lbl.config(text=filename.split('/')[-1])
        
        #print(self.photo_path.keys())

        self.product_image_btn=Button(self.product_insert_signup_frame,text="Browse Image",command=browse_image)
        self.product_image_btn.grid(row=9,column=0,ipadx=3,ipady=3,pady=4,padx=4,sticky='w')

        def upload_function():
            Product_insert()
            Product_insert.upload(self.product_name_entry.get(),self.product_category_entry.get(),self.product_quality_entry.get(),self.product_price_entry.get(),self.product_upload_date_entry.get(),self.product_discount_entry.get(),self.product_color_entry.get(),self.product_description_entry.get("1.0",'end-1c'),self.photo_path['image_path'],self.photo_path['image_path'].split('.')[-1])
            #showinfo('whole informationn',self.product_name_entry.get()+"\n"+self.product_category_entry.get()+"\n"+self.product_quality_entry.get()+"\n"+self.product_price_entry.get()+"\n"+self.product_upload_date_entry.get()+"\n"+self.product_discount_entry.get()+"\n"+self.product_color_entry.get()+"\n"+self.product_description_entry.get("1.0",'end-1c')+"\n"+self.photo_path['image_path']+"\n"+self.photo_path['image_path'].split('.')[-1])



    
        self.signup_btn=Button(self.product_insert_signup_frame,text='Upload',command=upload_function)
        self.signup_btn.config(font=('times',14),bg='green',fg='black')
        self.signup_btn.grid(row=10,columnspan=3,ipadx=10,ipady=10,pady=30)




        self.product_insert_signup_frame.pack(expand=1,fill='y',anchor='center')

        #self.product_insert_frame.pack(side='right',expand=True,fill=BOTH,anchor='e')
        self.product_insert_frame.pack_propagate(0)

        # End Right side window configuration insert





        

        # Product Explore and Product Insert button configuration
        def product_insert():
            self.users_details_frame.forget()
            self.product_explore_frame.forget()
            self.usermanagement_frame.forget()            
            self.details_frame.pack_propagate(0)
            self.details_frame.pack(expand=1,fill=BOTH,side='top',anchor='w')
            self.product_insert_frame.pack(side='right',expand=True,fill=BOTH,anchor='e')
            self.product_insert_frame.pack_propagate(0)


        def product_explore():
            self.users_details_frame.forget()
            self.usermanagement_frame.forget()
            self.product_insert_frame.forget()
            self.details_frame.pack_propagate(0)
            self.details_frame.pack(expand=1,fill=BOTH,side='top',anchor='w')
            self.product_explore_frame.pack(side='right',expand=True,fill=BOTH,anchor='e')
            product_explore_update()
            self.product_explore_frame.pack_propagate(0)

        self.product_insert_btn=Button(self.left_side_frame,text='Product Insert',command=product_insert)
        self.product_insert_btn.pack(side='bottom',ipadx=3,ipady=3,pady=10,padx=10)

        self.product_explore_btn=Button(self.left_side_frame,text='Product Explore',command=product_explore)
        self.product_explore_btn.pack(side='bottom',ipadx=3,ipady=3,pady=10,padx=10)

        # End Product Explore and Product Insert

        # Users management button
        def usermanagement_btn():
            self.details_frame.forget()
            self.product_explore_frame.forget()
            self.product_insert_frame.forget()
            self.users_details_frame.pack(expand=1,fill=BOTH,side='top',anchor='w')
            self.users_details_frame.pack_propagate(0)
            self.usermanagement_frame.pack(side='right',expand=True,fill=BOTH,anchor='e')
            self.usermanagement_frame.pack_propagate(0)
            

        self.user_management_btn=Button(self.left_side_frame,text='User Management',command=usermanagement_btn)
        self.user_management_btn.pack(side='bottom',ipadx=3,ipady=3,pady=10,padx=10)
        # End Users management button


        self.parent_frame.pack(expand=1,fill=BOTH)
        self.parent_frame.pack_propagate(0)
        # Parent Frame

        self.app.mainloop()

#Admin_window()