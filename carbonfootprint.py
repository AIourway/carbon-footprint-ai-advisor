import streamlit as st


def calculate_footprint(data):
    footprint = 0

    if data["transport"] == "car":
        footprint += data["miles"] * 0.411
    elif data["transport"] == "bus":
        footprint += data["miles"] * 0.105

    if data["diet"] == "meat":
        footprint += 7
    elif data["diet"] == "vegetarian":
        footprint += 3
    else:
        footprint += 2

    footprint += data["electricity"] * 0.233

    return round(footprint, 2)


def generate_feedback(footprint):
    if footprint < 8:
        return "Excellent! Your carbon footprint is low today 🌱"
    elif footprint < 15:
        return "Good, but there’s room to improve ⚖️"
    else:
        return "High footprint today. Let’s reduce it 🔥"


def main():
    st.set_page_config(page_title="Carbon Footprint AI", page_icon="🌍")
    st.title("🌍 Carbon Footprint Tracker")

    st.markdown("Use this app to estimate your daily carbon footprint based on travel, diet, and energy use.")

    transport = st.selectbox("Transport", ["car", "bus"])
    miles = st.number_input("Miles traveled", min_value=0.0, max_value=500.0, value=10.0, step=1.0)
    diet = st.selectbox("Diet", ["meat", "vegetarian", "vegan"])
    electricity = st.number_input("Electricity usage (kWh)", min_value=0.0, max_value=200.0, value=15.0, step=1.0)

    if st.button("Calculate footprint"):
        data = {
            "transport": transport,
            "miles": miles,
            "diet": diet,
            "electricity": electricity,
        }
        footprint = calculate_footprint(data)
        feedback = generate_feedback(footprint)

        st.success(f"Your carbon footprint for today is: {footprint} kg CO2")
        st.write(feedback)

        st.markdown(
            "---\n"
            "**Tip:** Try reducing car miles, choosing vegetarian meals, or lowering electricity use to cut emissions."
        )

    st.markdown("---")
    st.write("This file can be deployed directly on Streamlit Community Cloud using the GitHub repo URL:")
    st.write("https://github.com/AIourway/carbon-footprint-ai-advisor")


if __name__ == "__main__":
    main()

