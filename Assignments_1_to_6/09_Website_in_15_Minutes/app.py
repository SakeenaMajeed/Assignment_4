import streamlit as st

st.title("Simple Calculator")

st.write("Perform basic arithmetic operations.")

# Input fields
num1 = st.number_input("Enter the first number:", value=0.0, step=0.1)
num2 = st.number_input("Enter the second number:", value=0.0, step=0.1)

# Operation selection
operation = st.selectbox(
    "Select operation:", ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Calculation and display
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            st.error("Division by zero is not allowed!")
            result = None
        else:
            result = num1 / num2

    if result is not None:
        st.write(f"Result: {result}")
