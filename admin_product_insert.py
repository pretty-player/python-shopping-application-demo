import sqlite3
from tkinter.messagebox import showinfo


product_db_connect=sqlite3.connect('product_upload.db')
product_db_cursor=product_db_connect.cursor()
product_db_initial_query='''
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


class Product_insert:
    def ImageToBinary(image_path):
        with open(image_path,'rb') as bytes_values:
            image_bytes=bytes_values.read()
            bytes_values.close()
            return image_bytes

    def upload(product_name,product_category,product_quality,product_price,product_upload_date,product_discount,product_color,product_description,photo_path,photo_extention):
        showinfo('check',photo_path)
        values_tuple=(product_name,product_category,product_quality,product_price,product_upload_date,product_discount,product_color,product_description,Product_insert.ImageToBinary(photo_path),photo_extention)
        insert_into_query="""
            INSERT INTO product_upload(product_name,product_category,product_quality,product_price,product_upload_date,product_discount,product_color,product_description,product_image,product_image_extention)
            VALUES(?,?,?,?,?,?,?,?,?,?);
            """
        try:
            check_query='''
                SELECT * FROM product_upload;
                '''
            product_db_cursor.execute(check_query)
            product_db_cursor.execute(insert_into_query,values_tuple)
            product_db_connect.commit()
            showinfo('success','Data inserted successfully')
        except:
            product_db_cursor.execute(product_db_initial_query)
            product_db_cursor.execute(insert_into_query,values_tuple)
            product_db_connect.commit()
            showinfo('success','Data inserted successfully')

        # End Product insert database