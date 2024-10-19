import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Streamlit layout
st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg):", min_value=0.0)
height = st.number_input("Enter your height (m):", min_value=0.0)

if st.button("Calculate BMI"):
    if height > 0:  # Prevent division by zero
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is: {bmi:.2f}")

        # BMI categories
        if bmi < 18.5:
            st.write("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            st.write("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            st.write("Category: Overweight")
        else:
            st.write("Category: Obesity")
    else:
        st.warning("Height must be greater than zero.")
