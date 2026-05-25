def generate_feedback(footprint):
    if footprint < 8:
        return "Excellent! Your carbon footprint is low today 🌱"
    elif footprint < 15:
        return "Good, but there’s room to improve ⚖️"
    else:
        return "High footprint today. Let’s reduce it 🔥"
