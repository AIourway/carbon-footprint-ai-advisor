def generate_tips(profile, lifestyle):
    """Generate a short set of carbon reduction tips."""
    tips = [
        "Use public transport or carpool when possible.",
        "Reduce food waste by planning meals ahead.",
    ]

    if lifestyle == "busy":
        tips.append("Choose quick eco-friendly actions like reusable bottles and energy-saving bulbs.")
    elif lifestyle == "average":
        tips.append("Try swapping one meat meal per week for a plant-based option.")
    else:
        tips.append("Use more sustainable transport options and track your energy use closely.")

    if profile.get("location") and profile["location"] != "Unknown":
        tips.append(f"Explore local sustainability programs in {profile['location']}.")

    return tips
