from PyRoboteq import RoboteqHandler
from PyRoboteq import roboteq_commands as cmds
import time
 
controller = RoboteqHandler(debug_mode=True, exit_on_interrupt=False)
connected = controller.connect("/dev/ttyACM0") # Insert your COM port (for windows) or /dev/tty{your_port} (Commonly /dev/ttyACM0) for linux.



while true:
    int x = 500 #change to read in x value
    int y = 500 #change to read in y value


    if x<300 and x>-300 and y<300 and y>-300:
        controller.dual_motor_control(0, 0)
        print("Stop")
    if y>=300 and y<=1000 and x>-300 and x<300:
        controller.dual_motor_control(400, 400)
        print("forward/n")
    elif y<=-300 and y>=-1000 and x>-300 and x<300:
        controller.dual_motor_control(400, 400)
        print("reverse/n")
    elif x>=300 and x<=1000 and y>-300 and y<300
        controller.dual_motor_control(400, -400)
        print("right/n")
    elif x<=-300 and x>=-1000 and y>-300 and y<300:
        controller.dual_motor_control(-400, 400)
        print("left/n")
    else:
        controller.dual_motor_control(0, 0)
        print("Stop")


