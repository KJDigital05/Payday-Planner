import streamlit as st
from datetime import timedelta

st.title("Bills")

bill_name = st.text_input("Bill Name")
amount = st.number_input("Amount (£)")
bill_due = st.date_input("Due Date:")
bill_frequency = st.selectbox(
    "Bill Frequency",
    ["Weekly", "Fortnightly", "Monthly", "Yearly"]
)
def get_next_due_date(start_date, frequency, count=10):
    due_day = []
    bill_due = start_date

    for _ in range(count):  
        due_day.append(current)
    return due_day

    if frequency == "Weekly":
        current += timedelta(days=7)
    elif frequency == "Fortnightly":
        current += timedelta(days=14)
    elif frequency == "Monthly":
        current += timedelta(days=30)
    elif frequency == "Yearly":
        current += timdelta(days=365)

if st.button("Add Bill"):
    st.success("Bill added")
