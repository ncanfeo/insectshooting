import os, time, sys, threading
char = ""
width = 10
try:
    from msvcrt import getch
except ImportError:

    def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def keypress():
    global char
    while True:
        char = getch()
def clear_screen():
    try:
        os.system('clear')
    except:
        os.system('cls')
threading.Thread(target=keypress).start()
i = 0
while True:
	time.sleep(0.1)
	clear_screen()
	if char.lower() == "a":
		if i != 0:
			i -= 1
		char = ""
	elif char.lower() == "d":
		if i != width - 1:
			i += 1
		char = ""
	print("""
		$""")
	print(" " * i +"<=>"+" "*(i + 3))
