def get_profile(location):
    """Return a simple profile based on user location."""
    normalized_location = location.strip().title() if location else "Unknown"
    return {
        "location": normalized_location,
        "description": f"A user in {normalized_location}",
        "climate_zone": "temperate",
    }
