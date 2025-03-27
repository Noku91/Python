def get_runway(angle):
    runway= (angle + 4) //10
    if runway == 36:
    return 0
        return 0
    return runway

runway_numbers = []
while true:
    angle_input = input("Enter your current angle: ")
    if angle_input.lower() == "final":
        break
    try:
        angle = int(angle_input)
        if 0 <= angle <= 359:
            









