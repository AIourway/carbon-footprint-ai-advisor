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
# Run Tracker
if __name__ == "__main__":
    user_data = {
        "transport": input("Enter your mode of transport (car/bus): ").strip().lower(),
        "miles": float(input("Enter the number of miles traveled: ")),
        "diet": input("Enter your diet type (meat/vegetarian/vegan): ").strip().lower(),
        "electricity": float(input("Enter your electricity usage in kWh: "))
    }

    footprint = calculate_footprint(user_data)
    feedback = generate_feedback(footprint)

    print(f"Your carbon footprint for today is: {footprint} kg CO2")
    print(feedback)

