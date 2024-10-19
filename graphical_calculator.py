import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to plot
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

# Streamlit layout
st.title("Scientific Graphical Calculator")

# Function selection
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

# Ensure x_min is less than x_max
if x_min >= x_max:
    st.warning("Minimum x value should be less than maximum x value.")
else:
    if st.button("Plot"):
        plot_function(func_options[function_name], (x_min, x_max))
