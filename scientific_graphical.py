import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function for basic arithmetic operations
def simple_calculator():
    st.subheader("Simple Calculator")
    num1 = st.number_input("Enter first number:", value=0.0)
    operation = st.selectbox("Select operation:", ["+", "-", "*", "/"])
    num2 = st.number_input("Enter second number:", value=0.0)

    if st.button("Calculate"):
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero."
        else:
            result = "Invalid operation."
        
        st.write(f"Result: {result}")

# Function for scientific calculations
def scientific_calculator():
    st.subheader("Scientific Calculator")
    operation = st.selectbox("Select operation:", ["sin", "cos", "tan", "exp", "log"])
    num = st.number_input("Enter number:", value=0.0)

    if st.button("Calculate"):
        if operation == 'sin':
            result = np.sin(np.radians(num))
        elif operation == 'cos':
            result = np.cos(np.radians(num))
        elif operation == 'tan':
            result = np.tan(np.radians(num))
        elif operation == 'exp':
            result = np.exp(num)
        elif operation == 'log':
            if num > 0:
                result = np.log(num)
            else:
                result = "Error: Logarithm of non-positive number."
        else:
            result = "Invalid operation."

        st.write(f"Result: {result}")

# Function to plot mathematical functions
def plot_function(func, x_range):
    x = np.linspace(x_range[0], x_range[1], 1000)
    y = func(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=str(func.__name__))
    plt.title(f"Graph of {func.__name__}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()
    st.pyplot(plt)

def graphical_calculator():
    st.subheader("Graphical Calculator")
    func_options = {
        "Sine": np.sin,
        "Cosine": np.cos,
        "Tangent": np.tan,
        "Exponential": np.exp,
        "Logarithm": np.log,
    }

    function_name = st.selectbox("Select function to plot:", list(func_options.keys()))
    x_min = st.number_input("Enter minimum x value:", value=-10.0)
    x_max = st.number_input("Enter maximum x value:", value=10.0)

    if x_min < x_max:
        if st.button("Plot"):
            plot_function(func_options[function_name], (x_min, x_max))
    else:
        st.warning("Minimum x value should be less than maximum x value.")

# Streamlit layout
st.title("Combined Calculator")

calculator_type = st.selectbox("Select calculator type:", ["Simple Calculator", "Scientific Calculator", "Graphical Calculator"])

if calculator_type == "Simple Calculator":
    simple_calculator()
elif calculator_type == "Scientific Calculator":
    scientific_calculator()
elif calculator_type == "Graphical Calculator":
    graphical_calculator()
