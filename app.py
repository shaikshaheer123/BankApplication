import streamlit as st
from Bank import BankApplication

st.title("🏦 SBI Bank Application")

# Session storage
if "account" not in st.session_state:
    st.session_state.account = None

# Create Account
st.header("Create Account")

name = st.text_input("Enter Name")
acc_no = st.text_input("Account Number")
age = st.number_input("Age", min_value=18)
mobile = st.text_input("Mobile Number")
balance = st.number_input("Initial Balance", min_value=0)

if st.button("Create Account"):
    st.session_state.account = BankApplication(name, acc_no, age, mobile, balance)
    st.success("Account Created Successfully")

# Banking Operations
if st.session_state.account:

    st.header("Bank Operations")

    option = st.selectbox(
        "Select Operation",
        ["Deposit", "Withdraw", "Check Balance", "Update Mobile"]
    )

    if option == "Deposit":
        amount = st.number_input("Enter Amount")
        if st.button("Deposit"):
            msg = st.session_state.account.deposit(amount)
            st.success(msg)

    elif option == "Withdraw":
        amount = st.number_input("Enter Amount")
        if st.button("Withdraw"):
            msg = st.session_state.account.withdraw(amount)
            st.success(msg)

    elif option == "Check Balance":
        if st.button("Check"):
            msg = st.session_state.account.check_balance()
            st.info(msg)

    elif option == "Update Mobile":
        new_mobile = st.text_input("Enter New Mobile Number")
        if st.button("Update"):
            msg = st.session_state.account.update_mobile(new_mobile)
            st.success(msg)