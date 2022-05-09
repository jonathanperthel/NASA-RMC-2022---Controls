from mobilityMovementCommand import moveRover

port, pack = moveRover.servoSetup()
cont = moveRover.init_Roboteq()

#print(cont)
velocity = 0
angle = 1000

moveRover.moveServos(port, pack, angle, angle, angle, angle)
temp = moveRover.wheelMotors(cont, velocity)
print(temp)
'''
while True:
    #moveRover.wheelMotors(contr, velocity)
    #moveRover.moveServos(port, pack, angle, angle, angle, angle)

'''

