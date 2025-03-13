import datetime
from pymongo import MongoClient
import streamlit as st

client= MongoClient("mongodb://localhost:27017/")
db=client['atlasdemo']
collection=db['demo']

first_name=st.text_input("enter your first name")
last_name=st.text_input("enter your last name")
email=st.text_input("enter email")
password=st.text_input("set password",type="password")
confirm_password=st.text_input("retype password",type="password")
reg_time=datetime.datetime.now()

if st.button("Register"):
    if password==confirm_password:
        if first_name and last_name and email and password:
            user_info={
                "first_name":first_name,
                "last_name":last_name,
                "email":email,
                "password":password,    
                "reg time":reg_time
            }
            collection.insert_one(user_info)
            st.success("User registered successfully!")
        else:
            st.error("password not matching")
    else:
        st.error("Password no matching")