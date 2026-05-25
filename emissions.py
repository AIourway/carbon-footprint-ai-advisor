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
