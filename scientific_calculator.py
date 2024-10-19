import streamlit as st
import numpy as np

# Function to perform calculations
def calculate(operation, num1, num2=None):
    if operation == 'Addition':
        return num1 + num2
    elif operation == 'Subtraction':
        return num1 - num2
    elif operation == 'Multiplication':
        return num1 * num2
    elif operation == 'Division':
        return num1 / num2 if num2 != 0 else "Error: Division by zero."
    elif operation == 'Sine':
        return np.sin(np.radians(num1))
    elif operation == 'Cosine':
        return np.cos(np.radians(num1))
    elif operation == 'Tangent':
        return np.tan(np.radians(num1))
    elif operation == 'Exponentiation':
        return num1 ** num2
    elif operation == 'Logarithm':
        return np.log(num1) if num1 > 0 else "Error: Logarithm of non-positive number."

# Streamlit layout
st.title("Scientific Calculator")

# Operation selection
operation = st.selectbox("Select operation:", [
    "Addition", "Subtraction", "Multiplication", "Division", 
    "Sine", "Cosine", "Tangent", "Exponentiation", "Logarithm"
])

# Input fields
num1 = st.number_input("Enter first number:", value=0.0)

if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation"]:
    num2 = st.number_input("Enter second number:", value=0.0)
else:
    num2 = None

# Calculate button
if st.button("Calculate"):
    if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation"]:
        result = calculate(operation, num1, num2)
    else:
        result = calculate(operation, num1)

    st.write(f"Result: {result}")

