from time import sleep
from Engine.IO.KeyboardHooker import *

hooker = KeyboardHooker()
hooker.hook_keyboard("a", KeyEventEnum.ALL, lambda key, event: print(f"Shazamm ({key}, {event})"))
while True: sleep(1)