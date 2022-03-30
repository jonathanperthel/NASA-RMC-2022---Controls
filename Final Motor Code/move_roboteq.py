from PyRoboteq import RoboteqHandler
from PyRoboteq import roboteq_commands as cmds
import time


class roboteqMovement:

    def __init__(self):
        #Link to Roboteq motor controller
        self.controller = RoboteqHandler(debug_mode=True, exit_on_interrupt=False)
        self.connected = self.controller.connect("/dev/ttyACM0") # Insert your COM port (for windows) or /dev/tty{your_port} (Commonly /dev/ttyACM0) for linux.

    def wheelMotors(self, x):
        self.controller.dual_motor_control(x, x)


