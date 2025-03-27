def get_runway(angle):
    runway= (angle + 4) //10
    if runway == 36:
        
        return 0
    return runway

runway_numbers = []
while True:
    angle_input = input("Enter your current angle: ")
    if angle_input.lower() == "final":
        break
    try:
        angle = int(angle_input)
        if 0 <= angle <= 359:
            runway = get_runway(angle)
            runway_numbers.append(runway)
        else:
            print("ERROR: INVALID ERROR")
    except ValueError:
        print("ERROR: INVALID ERROR")

for runway in runway_numbers:
    print(runway)