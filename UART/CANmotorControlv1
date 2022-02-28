from PyRoboteq import RoboteqHandler
from PyRoboteq import roboteq_commands as cmds

controller = RoboteqHandler(debug_mode=True, exit_on_interrupt=False) 
connected = controller.connect("/dev/ttyACM0") # Insert your COM port (for windows) or /dev/tty{your_port} (Commonly /dev/ttyACM0) for linux.

ch1 = 0
ch2 = 0
count = 0
while True:
    ch1 = 100
    if (count % 10000) == 0:
        controller.send_raw_command("@02!G 1 200 ")
    count += 1
 
#ch1 = 0
#controller.send_raw_command("@02!G 1", ch1)
