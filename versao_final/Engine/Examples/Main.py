import sys
from time import sleep
sys.path.append("../")
from Engine.Graphics import *

hooker = KeyboardHooker()
hooker.hook_keyboard("a", lambda x: print("Shazamm"))

while True: sleep(1)