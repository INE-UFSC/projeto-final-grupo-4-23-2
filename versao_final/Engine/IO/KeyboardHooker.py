from pynput import keyboard
from enum import Enum

class KeyEventEnum(Enum):
    PRESS = 1,
    DOWN = 2,
    UP = 4,
    ALL = 8

class KeyboardHooker:
    def __init__(self):
        self.__hooks = {}
        self.__keys_status = {}
        # listener = keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
        # listener.start()
    
    def on_press(self, key): 
        self.call_hook(key, KeyEventEnum.PRESS)
    def on_release(self, key): self.call_hook(key, KeyEventEnum.UP)
    
    def call_hook(self, key, event:KeyEventEnum):
        try:
            # key = key.replace('\'','')
            # new_event = event
            if not key in self.__keys_status: self.__keys_status[key] = False
            
            # if self.__keys_status[key] == False and event == KeyEventEnum.PRESS: new_event = KeyEventEnum.DOWN
            # elif self.__keys_status[key] == True and event == KeyEventEnum.UP: new_event = KeyEventEnum.UP
            # elif event == KeyEventEnum.PRESS: new_event = KeyEventEnum.PRESS
            
            self.__keys_status[key] = event == KeyEventEnum.PRESS
            
            if not key in self.__hooks: return
            
            if KeyEventEnum.ALL in self.__hooks[key]:
                for f in self.__hooks[key][KeyEventEnum.ALL]: f(key, event)
                
            if not event in self.__hooks[key]: return
            for f in self.__hooks[key][event]: f(key, event)
        except:
            raise
            print("KeyHooker ERROR")
        
    
    def hook_keyboard(self, keys, on_event, function):
        for key in keys:
            if not key in self.__hooks: self.__hooks[key] = {}
            if not on_event in self.__hooks[key]: self.__hooks[key][on_event] = []
            self.__hooks[key][on_event].append(function)