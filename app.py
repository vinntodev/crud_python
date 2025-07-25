import streamlit as st
import pandas as pd
from database import create_table, insert_data, get_all_users, get_all_user_id, update_user, delete_user

create_table()
st.title("🧮 Aplikasi CRUD Sederhana")

menu = st.sidebar.selectbox("Menu", ["Create", "Read", "Update", "Delete"])

if menu == "Create":
  st.subheader("Add Data User")
  name = st.text_input("Enter Name")
  email = st.text_input("Enter Email")
  address = st.text_input("Enter Address")
  if st.button("Save"):
    insert_data(name, email, address)
    st.success("Data berhasil disimpan")

elif menu == "Read":
    st.subheader("Lihat Data")
    data = get_all_users()
    if data:
      df = pd.DataFrame(data, columns=["ID", "Name", "Email", "Address"])
    st.dataframe(df)

elif menu == "Update":
  st.subheader("Update Data")
  user_id = st.number_input("Masukkan ID yang ingin di update", min_value=1)
  user_data = get_all_user_id(user_id)
  if user_data:
    name = st.text_input(f"Name Baru", user_data[1])
    email = st.text_input(f"Email Baru", user_data[2])
    address = st.text_input(f"Address Baru", user_data[3])
    if st.button("Update"):
      update_user(user_id, name, email, address)
      st.success("Data berhasil diupdate")
  else:
    st.warning("Data dengan ID tersebut tidka ditemukan.")

elif menu == "Delete":
  st.subheader("Delete Data")
  user_id = st.number_input("ID", min_value=1)
  user_data = get_all_user_id(user_id)
  if user_data:
    name = st.text_input(f"Name Baru", user_data[1])
    email = st.text_input(f"Email Baru", user_data[2])
    address = st.text_input(f"Address Baru", user_data[3])
    if st.button("Delete"):
      delete_user(user_id)
      st.warning("Data dihapus")
  else:
    st.warning("Data dengan ID tersebut tidak ditemukan!")

