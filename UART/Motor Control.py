from PyRoboteq import RoboteqHandler
from PyRoboteq import roboteq_commands as cmds
import time
 
controller = RoboteqHandler(debug_mode=True, exit_on_interrupt=False)
connected = controller.connect("/dev/ttyACM0") # Insert your COM port (for windows) or /dev/tty{your_port} (Commonly /dev/ttyACM0) for linux.
count = 0

if __name__ == "__main__":
    while connected:
        while count < 10:
            controller.dual_motor_control(200, 200)
            time.sleep(2)
            controller.dual_motor_control(-200, -200)
            time.sleep(2)
            controller.dual_motor_control(0, 0)
            time.sleep(1)
            count = count + 1

        

        
        
