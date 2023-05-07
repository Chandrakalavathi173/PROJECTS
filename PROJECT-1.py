# CONNECTION.PY

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Chandu(173)")
print(mydb.connection_id)
cur=mydb.cursor()
----------------------------------------------------------------------------------------------------------------------------------------------

# CREATE_DB.PY

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Chandu(173)")
cur=mydb.cursor()
cur.execute("create database Inventory_Management")
mydb.commit()
----------------------------------------------------------------------------------------------------------------------------------------------------

# CREATE_TABLE.PY

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Chandu(173)",database="inventory_management")
cur=mydb.cursor()
a='create table manufacture (manuf_id integer(5),product varchar(20),color varchar(20),defective integer(2),manuf_date date,no_of_items integer(5))'
b='create table goods (goods_id integer(5),product varchar(20),color varchar(20),manuf_date date,company varchar(20))'
c='create table purchase (purch_id integer(5),product varchar(20),color varchar(20),purch_amount integer(5),purch_date date,store varchar(20))'
d='create table sales (sales_id integer(5),product varchar(20),color varchar(20),profit_margin integer(5),sales_date date,store varchar(20))'
cur.execute(a)
cur.execute(b)
cur.execute(c)
cur.execute(d)
mydb.commit()
print("Created")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

# INSERT_DATA.PY

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Chandu(173)",database="inventory_management")
cur=mydb.cursor()
a='insert into manufacture (manuf_id,product,color,defective,manuf_date,no_of_items) values(%s,%s,%s,%s,%s,%s)'
b=[(1,"toy","red",2,"2023-05-01",120),(2,"shirt","black",1,"2023-04-02",190),(3,"wooden tables","brown",0,"2023-06-12",100),(4,"wooden chairs","brown",8,"2023-04-22",90),(5,"sandles","white",5,"2023-04-08",100)]
c='insert into goods (goods_id,product,color,manuf_date,company) values(%s,%s,%s,%s,%s)'
d=[(1,"toy","red","2023-05-01","defExport"),(2,"shirt","black","2023-04-02","abcExport"),(3,"wooden tables","brown","2023-06-12","ssExport"),(4,"wooden chairs","brown","2023-04-22","xExport"),(5,"sandles","white","2023-04-08","yExport")]
e='insert into purchase (purch_id,product,color,purch_amount,purch_date,store) values(%s,%s,%s,%s,%s,%s)'
f=[(1,"toy","red",1500,"2023-05-13","MyKids"),(2,"shirt","black",5000,"2023-04-29","ORay"),(3,"wooden tables","brown",15000,"2023-06-28","MyCare"),(4,"wooden chairs","brown",2000,"2023-05-22","MyCare"),(5,"sandles","white",1000,"2023-05-05","Bata")]
g='insert into sales (sales_id,product,color,profit_margin,sales_date,store) values(%s,%s,%s,%s,%s,%s)'
h=[(1,"toy","red",200,"2023-05-13","MyKids"),(2,"shirt","black",500,"2023-04-29","ORay"),(3,"wooden tables","brown",2000,"2023-06-28","MyCare"),(4,"wooden chairs","brown",600,"2023-05-22","MyCare"),(5,"sandles","white",300,"2023-05-05","Bata")]
cur.executemany(a,b)
cur.executemany(c,d)
cur.executemany(e,f)
cur.executemany(g,h)
mydb.commit()
print("Inserted")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# QUERY.PY

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Chandu(173)",database="inventory_management")
cur=mydb.cursor()

# Delete the defective item, e.g., the shirt which was accidentally purchased by the “ORay” store, manufactured on the date ‘02-04-23’.
a='delete manufacture from manufacture inner join purchase on manufacture.manuf_id=purchase.purch_id where manufacture.manuf_date="2023-04-02" and manufacture.product="shirt" and purchase.store="ORay"'
cur.execute(a)

# Update the manufacture details of all the red-colored toys which are purchased by the “MyKids” store.
b='update manufacture inner join purchase on manufacture.manuf_id=purchase.purch_id set manufacture.manuf_id=109,manufacture.color="black",manufacture.defective=5,manufacture.manuf_date="2023-05-22",manufacture.no_of_items=110 where manufacture.color="red" and manufacture.product="toy" and purchase.store="MyKids"'
cur.execute(b)
mydb.commit()
print("Executed")

# Display all the “wooden chair” items that were manufactured before the 1st May 2023. 
c='select * from manufacture where manuf_date<"2023-05-01" and product="wooden chairs"' 
cur.execute(c)
display=cur.fetchall()
for x in display:
    print(x)

#  Display the profit margin amount of the “wooden table” that was sold by the “MyCare” store, manufactured by the “SS Export” company.
d='select sales.profit_margin from sales inner join goods on sales.sales_id=goods.goods_id where sales.product="wooden tables" and sales.store="MyCare" and goods.company="ssExport"'
cur.execute(d)
display=cur.fetchall()
for x in display:
    print(x)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
