import streamlit as st
import pandas as pd
from datetime import datetime

st.title("💸 Smart Expense Tracker")

# Load existing data
try:
    df = pd.read_csv("expenses.csv")
except:
    df = pd.DataFrame(columns=["date", "category", "amount", "payment_method", "notes"])

# Input section
st.subheader("Add New Expense")
date = st.date_input("Date", datetime.today())
category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Other"])
amount = st.number_input("Amount", min_value=0.0)
payment_method = st.selectbox("Payment Method", ["Cash", "UPI", "Card"])
notes = st.text_input("Notes")

# Save entry
if st.button("Add Expense"):
    new_entry = {
        "date": date,
        "category": category,
        "amount": amount,
        "payment_method": payment_method,
        "notes": notes
    }
    new_df = pd.DataFrame([new_entry])  # ✅ wrap in list
    df = pd.concat([df, new_df], ignore_index=True)  # ✅ use concat
    df.to_csv("expenses.csv", index=False)
    st.success("Expense added successfully!")
