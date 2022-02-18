from PyRoboteq import RoboteqHandler
from PyRoboteq import roboteq_commands as cmds
import time
 
controller = RoboteqHandler(debug_mode=True, exit_on_interrupt=False)
connected = controller.connect("/dev/ttyACM0") # Insert your COM port (for windows) or /dev/tty{your_port} (Commonly /dev/ttyACM0) for linux.

while connected:
    temp = controller.send_raw_command("@02?T 1 0") #raw string to get temperature reading of roboteq node 2
    voltage =  controller.send_raw_command("@02?V 1 0") #raw string to get temperature reading of roboteq node 2
    print(temp)
    print("/n")
    print(voltage)
    print("/n")