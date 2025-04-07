import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="🧮",
    layout="centered"
)

# App title and description
st.markdown("## 🧮 BMI Calculator")
st.markdown("Enter your height and weight below to check your **Body Mass Index (BMI)** 💪")

# Create columns for input
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    height = st.number_input("📏 Height (in meters)", min_value=0.5, max_value=2.5, value=1.75)
with col2:
    weight = st.number_input("⚖️ Weight (in kg)", min_value=10, max_value=200, value=70)

# Add a button to calculate
st.markdown("---")
if st.button("🧠 Calculate My BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.markdown(f"### 📊 Your BMI is: **{bmi:.2f}**")

        # BMI Categories
        if bmi < 18.5:
            st.warning("🟡 You are **underweight**. Consider eating a balanced diet.")
        elif bmi < 24.9:
            st.success("🟢 You have a **normal weight**. Keep it up!")
        elif bmi < 29.9:
            st.warning("🟠 You are **overweight**. Consider some exercise.")
        else:
            st.error("🔴 You are **obese**. It might be good to talk to a doctor.")
    else:
        st.error("❌ Please enter valid height and weight values.")
