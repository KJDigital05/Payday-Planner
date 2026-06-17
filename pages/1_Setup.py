import streamlit as st
from datetime import timedelta
from database import load_settings, save_settings

settings = load_settings()

st.title("Current Finances")

pay_frequency = st.selectbox(
    "Pay Frequency",
    ["Weekly", "Fortnightly", "Monthly"]
)

next_payday = st.date_input("Next Payday")
def get_next_paydays(start_date, frequency, count=10):
    paydays = []
    current = start_date
    
    for _ in range(count):  
        paydays.append(current)
    return paydays

    if frequency == "Weekly":
        current += timedelta(days=7)
    elif frequency == "Fortnightly":
        current += timedelta(days=14)
    elif frequency == "Monthly":
        current += timedelta(days=30)

balance = st.number_input(
    "Current Balance (£)", 
    value=float(settings.get("balance", 0))
)

if st.button("Save"):
    
    save_settings = ({
        "pay_frequency": pay_frequency,
        "next_payday": str(next_payday),
        "current_balance": balance
    })
    st.success("Settings Saved.")

