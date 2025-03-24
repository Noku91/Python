angles = []

current_angle = int(input('Enter your current angle: '))
while current_angle <= 359:
    angles.append(current_angle)

    current_angle = int(input('Enter your current angle: '))

for angle in current_angles:
    if angle <= 359:
        print('final')
    else:
        print('ERROR: INVALID ANGLE')   


