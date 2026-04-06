import streamlit as st
import backend

import pandas as pd
import json
import requests  ### Py file dr tsegtstei bailgah uudnees importuudiig deed taldn ehleed oruulna


st.header("Hello")

st.subheader("Sub-header shu")
st.write("Ene heseg deer paragraph text garch irne")

st.divider()

st.write("---")



name = st.text_input("Нэр")
st.write("Таны нэр:", name)

age = st.number_input("Таны нас")
st.write("Таны нас:", age)

pwd = st.text_input("Password", type="password")

color = st.selectbox("Өнгө сонгох", ["Хар", "Цагаан", "Ягаан","Улаан"])
colors = st.multiselect("Өнгө сонгох",["Хар", "Цагаан", "Ягаан","Улаан"])


st.divider()
st.subheader("Cargo price calculotar")

weight = st.number_input("Жин")

height = st.number_input("Урт")
depth = st.number_input("Өргөн")
lenght = st.number_input("Өндөр")

if st.button("Тооцоолох"):
    st.write("Функц дуудаж ажиллах")

    price = backend.cargo_price_calculator(height, depth, lenght, weight, kg_price=3500, m3_price=3000)
    st.success(f"Таны карго үнэ: {price}")
    st.info(f"Таны карго үнэ: {price}")
    st.warning(f"Таны карго үнэ: {price}")
    st.error(f"Таны карго үнэ: {price}")


st.divider()
st.subheader("Alt mungunii une")

col1, col2, col3 = st.columns([2,2,1])
start_date = col1.date_input("Ehleh hugatsaa")
end_date = col2.date_input("Duusah hugatsaa")

if col3.button("Haih"):
    if start_date > end_date:
        st.error("Ognoonii songolt buruu bn.")
    else:
        df = backend.alt_mungunii_une(
            start_date.strftime("%Y-%m-%d"),
            end_date.strftime("%Y-%m-%d")
        )
        st.dataframe(df)

        
st.divider()
st.subheader("Эксэл файл цэвэрлэгээ")

## files = st.file_uploader("Файлаа оруулна уу", type=["xlsx", 'xls'], accept_multiple_files = True)

files = st.file_uploader("Файлаа оруулна уу", type=["xlsx", 'xls'], accept_multiple_files = True)

for file in files:
    st.dataframe(backend.excel_sheet_append(file))
    
        

    

    
    
    



    


