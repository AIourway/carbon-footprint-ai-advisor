import json

import streamlit as st

from emissions import calculate_footprint
from agent import generate_feedback


def main():
    st.title("🌍 Carbon Footprint Tracker AI")

    transport = st.selectbox("Transport", ["car", "bus", "bike"])
    miles = st.slider("Miles traveled", 0, 100)
    diet = st.selectbox("Diet", ["meat", "vegetarian", "vegan"])
    electricity = st.slider("Electricity (kWh)", 0, 50)

    if st.button("Calculate"):
        data = {
            "transport": transport,
            "miles": miles,
            "diet": diet,
            "electricity": electricity,
        }

        result = calculate_footprint(data)
        feedback = generate_feedback(result)

        st.write(f"### Your footprint: {result} kg CO2")
        st.write(feedback)

        with open("data/logs.json", "a") as f:
            f.write(json.dumps(data) + "\n")


if __name__ == "__main__":
    main()
