import streamlit as st

st.title ("Payday Planner")

pay = st.number_input("Pay recieved (£)", min_value=0.0)

food = st.number_input("Food Budget", value=120.0)
petrol = st.number_input("Petrol Budget", value=120.0)
car_payment = st.number_input("Car Payment", value=150.0)
savings = st.number_input("Savings", value=30.0)

allocated = food + petrol + car_payment + savings
reamining = pay - allocated

if st.button("Calculate"):
    st.subheader("Allocation")
    
    st.write(f"Food: £{food}")
    st.write(f"Petrol: £{petrol}")
    st.write(f"Car Payment: £{car_payment}")
    st.write(f"Savings: £{savings}")

    st.metric("Reamining", f"£{reamining:.2f}")