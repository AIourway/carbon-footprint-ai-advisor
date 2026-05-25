import streamlit as st

from advisor import generate_tips
from location import get_profile


def main():
    st.title("🌱 Carbon Reduction Advisor AI")

    location = st.text_input("Enter your location")
    lifestyle = st.selectbox("Lifestyle", ["busy", "average", "eco-conscious"])

    if st.button("Get Advice"):
        profile = get_profile(location)
        tips = generate_tips(profile, lifestyle)

        st.write("### Your Tips:")
        for tip in tips:
            st.write("- " + tip)


if __name__ == "__main__":
    main()
