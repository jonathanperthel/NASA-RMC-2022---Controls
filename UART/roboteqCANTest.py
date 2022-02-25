from PyRoboteq import RoboteqHandler
from PyRoboteq import roboteq_commands as cmds
import time
 
controller = RoboteqHandler(debug_mode=False, exit_on_interrupt=False)
connected = controller.connect("/dev/ttyS0") # Insert your COM port (for windows) or /dev/tty{your_port} (Commonly /dev/ttyACM0) for linux.
count = 0

while connected:
    temp = controller_volts = controller.read_value("?ICL", 2)
    #voltage =  controller.send_raw_command("@02?V 1 0") #raw string to get temperature reading of roboteq node 2
    if count%1000 == 0:
        print(temp)
        #print(voltage)
        #print("/n")
    count += 1