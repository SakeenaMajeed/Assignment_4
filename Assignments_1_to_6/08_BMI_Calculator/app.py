import streamlit as st

st.title("BMI Calculator")

st.write("Enter your height and weight to calculate your BMI.")

height = st.number_input(
    "Height (in meters)", min_value=0.5, max_value=3.0, value=1.75, step=0.01
)
weight = st.number_input(
    "Weight (in kilograms)", min_value=20.0, max_value=200.0, value=70.0, step=0.1
)

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height**2)
        st.write(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            st.write("You are underweight.")
        elif bmi < 25:
            st.write("You have a normal weight.")
        elif bmi < 30:
            st.write("You are overweight.")
        else:
            st.write("You are obese.")
    else:
        st.error("Please enter valid height and weight.")
