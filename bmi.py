import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Streamlit layout
st.title("🏋️‍♂️ BMI Calculator")

# Input section with styling
st.header("Enter Your Details")
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (kg):", min_value=0.0, step=0.1, format="%.1f")
    
with col2:
    height = st.number_input("Height (m):", min_value=0.0, step=0.01, format="%.2f")

# Calculate BMI button
if st.button("Calculate BMI"):
    if height > 0:  # Prevent division by zero
        bmi = calculate_bmi(weight, height)
        st.success(f"Your BMI is: **{bmi:.2f}**")

        # BMI categories
        if bmi < 18.5:
            st.write("Category: **Underweight**")
            st.write("👉 It's important to maintain a healthy weight. Consult a healthcare provider.")
        elif 18.5 <= bmi < 24.9:
            st.write("Category: **Normal weight**")
            st.write("✅ Keep up the good work!")
        elif 25 <= bmi < 29.9:
            st.write("Category: **Overweight**")
            st.write("⚠️ Consider a balanced diet and regular exercise.")
        else:
            st.write("Category: **Obesity**")
            st.write("🚨 Please consult a healthcare provider for guidance.")
    else:
        st.warning("Height must be greater than zero.")

# Add some additional information
st.markdown("---")
st.header("What is BMI?")
st.write("BMI (Body Mass Index) is a measure of body fat based on height and weight.")
st.write("It helps categorize individuals into different weight categories.")

st.markdown("---")
st.write("Developed with ❤️ by Your Name")




# import streamlit as st

# def calculate_bmi(weight, height):
#     return weight / (height ** 2)

# # Streamlit layout
# st.title("BMI Calculator")

# weight = st.number_input("Enter your weight (kg):", min_value=0.0)
# height = st.number_input("Enter your height (m):", min_value=0.0)

# if st.button("Calculate BMI"):
#     if height > 0:  # Prevent division by zero
#         bmi = calculate_bmi(weight, height)
#         st.write(f"Your BMI is: {bmi:.2f}")

#         # BMI categories
#         if bmi < 18.5:
#             st.write("Category: Underweight")
#         elif 18.5 <= bmi < 24.9:
#             st.write("Category: Normal weight")
#         elif 25 <= bmi < 29.9:
#             st.write("Category: Overweight")
#         else:
#             st.write("Category: Obesity")
#     else:
#         st.warning("Height must be greater than zero.")
