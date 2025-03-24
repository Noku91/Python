batteries = []

battery = float(input('Enter your input: '))
while battery>= 0:
    batteries.append(battery)
    battery = float(input('Enter your input: '))
for battery in batteries :
    if battery>= 1.2: 
        print('Beep')
    else:
        print('Boop')