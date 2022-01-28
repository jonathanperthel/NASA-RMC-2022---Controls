# import curses
import curses

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)


try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                #print("up")
                controller.dual_motor_control(200, 200)
            elif char == curses.KEY_DOWN:
                #print("down")
                controller.dual_motor_control(-200, -200)
            elif char == curses.KEY_RIGHT:
                #print("right")
                controller.dual_motor_control(-200, 200)
            elif char == curses.KEY_LEFT:
                #print("left")
                controller.dual_motor_control(200, -200)
            elif char == 10:
                #print("stop")
                controller.dual_motor_control(0, 0)    
    if __name__ == "__main__":
        while connected:

             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()