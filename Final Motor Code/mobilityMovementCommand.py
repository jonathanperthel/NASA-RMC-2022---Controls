from PyRoboteq import RoboteqHandler
from PyRoboteq import roboteq_commands as cmds
import time
import os
from dynamixel_sdk import * # Uses Dynamixel SDK library

class moveRover:

    def init_Roboteq():
        #Link to Roboteq motor controller
        controller = RoboteqHandler(debug_mode=True, exit_on_interrupt=True)
        connected = controller.connect("/dev/ttyACM1") # Insert your COM port (for windows) or /dev/tty{your_port} (Commonly /dev/ttyACM0) for linux.
        return(controller)

    #Wheel motors are on Node 1 Channel 1
    def wheelMotors(controller, vel):
        #controller.dual_motor_control(x, x)
        #battery_amps = controller.read_value(cmds.READ_VOLTS, 1)
        controller_volts1 = controller.read_value("@01?T", 0)
        controller_volts2 = controller.read_value("@02?T", 0)
        strBase = "@01!G 1 "
        outputString = strBase + str(vel) + ''
        controller.send_raw_command(outputString)
        return(controller_volts2)

    #Digging Motor is on Node 1 Channel 2
    def digMotor(controller, vel):
        #controller_volts1 = controller.read_value("@01?T", 0)
        strBase = "@01!G 2 "
        outputString = strBase + str(vel) + ''
        controller.send_raw_command(outputString)
        return(1)

    #Digging Actuator is on Node 2 channel 1
    def digActuator(controller, vel):
        #controller_volts2 = controller.read_value("@02?T", 0)
        strBase = "@02!G 1 "
        outputString = strBase + str(vel) + ''
        controller.send_raw_command(outputString)
        return(1)
    

    #Dump Actuators are Node 2 channel 2
    def dumpActuator(controller, vel):
        #controller_volts2 = controller.read_value("@02?T", 0)
        strBase = "@02!G 2 "
        outputString = strBase + str(vel) + ''
        controller.send_raw_command(outputString)
        return(1)

    def servoSetup():
        if os.name == 'nt':
            import msvcrt
            def getch():
                return msvcrt.getch().decode()
        '''
        else:
            import sys, tty, termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            def getch():
                try:
                    tty.setraw(sys.stdin.fileno())
                    ch = sys.stdin.read(1)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                return ch
        '''


        #********* DYNAMIXEL Model definition *********
        #***** (Use only one definition at a time) *****
        MY_DXL = 'X_SERIES'       # X330 (5.0 V recommended), X430, X540, 2X430
        # Control table address
        ADDR_TORQUE_ENABLE          = 64
        ADDR_GOAL_POSITION          = 116
        ADDR_PRESENT_POSITION       = 132
        DXL_MINIMUM_POSITION_VALUE  = 0         # Refer to the Minimum Position Limit of product eManual
        DXL_MAXIMUM_POSITION_VALUE  = 4095      # Refer to the Maximum Position Limit of product eManual
        BAUDRATE                    = 57600


        # DYNAMIXEL Protocol Version (1.0 / 2.0)
        # https://emanual.robotis.com/docs/en/dxl/protocol2/
        PROTOCOL_VERSION            = 2.0

        # Factory default ID of all DYNAMIXEL is 1
        DXL_ID1                      = 1
        DXL_ID2                      = 2

        # Use the actual port assigned to the U2D2.
        # ex) Windows: "COM*", Linux: "/dev/ttyUSB*", Mac: "/dev/tty.usbserial-*"
        DEVICENAME                  = '/dev/ttyUSB0'

        TORQUE_ENABLE               = 1     # Value for enabling the torque
        TORQUE_DISABLE              = 0     # Value for disabling the torque
        DXL_MOVING_STATUS_THRESHOLD = 20    # Dynamixel moving status threshold

        index = 1
        angle = 2000
        dxl_goal_position = [1000, 2000]         # Goal position


        # Initialize PortHandler instance
        # Set the port path
        # Get methods and members of PortHandlerLinux or PortHandlerWindows
        portHandler = PortHandler(DEVICENAME)

        # Initialize PacketHandler instance
        # Set the protocol version
        # Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
        packetHandler = PacketHandler(PROTOCOL_VERSION)

        # Open port
        if portHandler.openPort():
            print("Succeeded to open the port")
        else:
            print("Failed to open the port")
            #print("Press any key to terminate...")
            #getch()
            quit()


        # Set port baudrate
        if portHandler.setBaudRate(BAUDRATE):
            print("Succeeded to change the baudrate")
        else:
            print("Failed to change the baudrate")
           # print("Press any key to terminate...")
            #getch()
            quit()
        #get started 
        #Set port baudrate
        if portHandler.setBaudRate(BAUDRATE):
            print("Succeeded to change the baudrate")
        else:
            print("Failed to change the baudrate")
            print("Press any key to terminate...")
            #getch()
            quit()

        # Enable Dynamixel Torque
        dxl_comm_result1, dxl_error1 = packetHandler.write1ByteTxRx(portHandler, DXL_ID1, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
        dxl_comm_result2, dxl_error2 = packetHandler.write1ByteTxRx(portHandler, DXL_ID2, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
        if dxl_comm_result1 != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result1))
        elif dxl_error1 != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error1))
        else:
            print("Dynamixel has been successfully connected")

        return(portHandler, packetHandler)



    def moveServos(portHandler, packetHandler, s1, s2, s3, s4):

        #control servo movement
        DXL_ID1 = 1
        DXL_ID2 = 2
        DXL_ID3 = 3
        DXL_ID4 = 4
        ADDR_GOAL_POSITION          = 116
        ADDR_TORQUE_ENABLE          = 64
        TORQUE_ENABLE               = 1     # Value for enabling the torque
        TORQUE_DISABLE              = 0     # Value for disabling the torque
       
        # Enable Dynamixel Torque
        dxl_comm_result1, dxl_error1 = packetHandler.write1ByteTxRx(portHandler, DXL_ID1, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
        dxl_comm_result2, dxl_error2 = packetHandler.write1ByteTxRx(portHandler, DXL_ID2, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
        dxl_comm_result1, dxl_error1 = packetHandler.write1ByteTxRx(portHandler, DXL_ID3, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
        dxl_comm_result2, dxl_error2 = packetHandler.write1ByteTxRx(portHandler, DXL_ID4, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)

        # Write goal position
        dxl_comm_result1, dxl_error1 = packetHandler.write4ByteTxRx(portHandler, DXL_ID1, ADDR_GOAL_POSITION, s1)
        dxl_comm_result2, dxl_error2 = packetHandler.write4ByteTxRx(portHandler, DXL_ID2, ADDR_GOAL_POSITION, s2)
        dxl_comm_result1, dxl_error1 = packetHandler.write4ByteTxRx(portHandler, DXL_ID3, ADDR_GOAL_POSITION, s3)
        dxl_comm_result2, dxl_error2 = packetHandler.write4ByteTxRx(portHandler, DXL_ID4, ADDR_GOAL_POSITION, s4)

        # Disable Dynamixel Torque
        dxl_comm_result1, dxl_error1 = packetHandler.write1ByteTxRx(portHandler, DXL_ID1, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
        dxl_comm_result2, dxl_error2 = packetHandler.write1ByteTxRx(portHandler, DXL_ID2, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
        dxl_comm_result1, dxl_error1 = packetHandler.write1ByteTxRx(portHandler, DXL_ID3, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
        dxl_comm_result2, dxl_error2 = packetHandler.write1ByteTxRx(portHandler, DXL_ID4, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)        


