from PyRoboteq import RoboteqHandler
from PyRoboteq import roboteq_commands as cmds
import time
 
controller = RoboteqHandler(debug_mode=False, exit_on_interrupt=False)
connected = controller.connect("/dev/ttyACM0") # Insert your COM port (for windows) or /dev/tty{your_port} (Commonly /dev/ttyACM0) for linux.
count = 0

while connected:
    temp = controller_volts = controller.read_value("?ICL", 2)
    controller_volts1 = controller.read_value("@01?T", 0)
    controller_volts2 = controller.read_value("@02?T", 0)     
    if count%100 == 0:
        #print(temp)
        print(controller_volts1)
        print(controller_volts2)
        #print("/n")
    count += 1