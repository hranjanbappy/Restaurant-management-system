# -*- coding: utf-8 -*-
"""Restaurant management system.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ezps4A1lrW0CSpF9VOOnACQlPDZtLdhK
"""

#This software is written in python & anyone can run this. 
#Run this code is written using IDE: "Google Colab" 
#Follow this tutorial video to run this code properly : 
'''
A restaurant management system that generates bill (with discount) per order. 
The rules for the discount are given below: 
(1) If a customer is younger than 25 years, he/she gets a 15% discount on all products on his/her birthday. 
(2) If a customer is older than 60 years, he/she gets a 30% discount on all products on his/her birthday. 
(3) For the rest of the customers, they get a 5% discount on their birthday. 
(4) There is a 20% discount on pasta regardless of the customer’s date of birth. 
(6) Only the largest discount can be applied to any item if there are multiple discounts.

'''
from google.colab import files
uploded= files.upload()
 
import pandas as pd
 
Customer_Order= pd.read_excel('Customer Order.xlsx').fillna(0)
Restaurant_menu= pd.read_excel('Restaurant menu.xlsx').fillna(0)


# Different types of discount offers
dis_1 = 15/100
dis_2 = 30/100
dis_3 = 5/100
dis_4 = 20/100

#loop for bill preparation 
i = 0
while i < len(Customer_Order):
  discount = 0
  by = Customer_Order["date_of_birth"].dt.year
  bm = Customer_Order["date_of_birth"].dt.month
  bd = Customer_Order["date_of_birth"].dt.day
  py = Customer_Order["pruchase_date"].dt.year
  pm = Customer_Order["pruchase_date"].dt.month
  pd = Customer_Order["pruchase_date"].dt.day


  #Checking the age & birthday for proper discount
  if bm[i] == pm[i] and bd[i] == pd[i] :
    age = py[i] - by[i]
    if age < 25 :
      discount = dis_1
    elif age > 60 :
      discount = dis_2
    else :
      discount = dis_3
  #taking care of the special pasta discount 
  if Customer_Order ["item"][i] == 'pasta' :
    if discount < dis_4 :
      discount = dis_4

  #Fining the item orderd by the customer in our menu
  item = Restaurant_menu.loc[Restaurant_menu['item'] == Customer_Order['item'][i]]

  #Single Product Price without any discount
  price = item['price'].values
  
  #quantity orderd by the customer
  quantity = Customer_Order['quantity'][i]
  
  #Tatal Bill after discount
  Customer_Order.loc[i, "total_bill"] = (price - price*discount)*quantity

  i += 1

#Creating the output for total bill
customer_bill = Customer_Order[['Customer_id', 'total_bill']]

#Creating output in xlsx format & downloading the output
customer_bill.to_excel("customer_bill.xlsx",
             sheet_name='Bill')
 
files.download('customer_bill.xlsx')