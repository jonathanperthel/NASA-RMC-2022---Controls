from curses.ascii import RS
from PyRoboteq import RoboteqHandler
from PyRoboteq import roboteq_commands as cmds
import time
 
controller = RoboteqHandler(debug_mode=True, exit_on_interrupt=False)
connected = controller.connect("/dev/ttyACM0") # Insert your COM port (for windows) or /dev/tty{your_port} (Commonly /dev/ttyACM0) for linux.
count = 0

if __name__ == "__main__":
    while connected:
        while True:
            controller.dual_motor_control(0, 0)
            #READ_MOTOR_AMPS, MOTOR #2
            battery_amps = controller.read_value(cmds.READ_VOLTS, 1)
            if(count%200 == 0):
                print(battery_amps)
            #controller.dual_motor_control(0, 0)
            #time.sleep(1)
            count = count + 1
#            time.sleep(2)
#            controller.dual_motor_control(-400, -400)
#            time.sleep(2)
