from PyRoboteq import RoboteqHandler
from PyRoboteq import roboteq_commands as cmds

controller = RoboteqHandler(debug_mode=True, exit_on_interrupt=False) 
connected = controller.connect("/dev/ttyS0") # Insert your COM port (for windows) or /dev/tty{your_port} (Commonly /dev/ttyACM0) for linux.

battery_amps = controller.read_value(cmds.READ_VOLTS, 1)
print(battery_amps)

