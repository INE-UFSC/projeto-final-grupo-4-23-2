import keyboard
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
    
    def call_hook(self, key, event:KeyEventEnum):
        new_event = event
        
        if not key in self.__keys_status: self.__keys_status[key] = False
        
        if not self.__keys_status[key] and event == KeyEventEnum.PRESS: new_event = KeyEventEnum.DOWN
        if event == KeyEventEnum.UP: self.__keys_status[key]=False
        if event == KeyEventEnum.PRESS: self.__keys_status[key]=True
        
        if KeyEventEnum.ALL in self.__hooks[key]: 
            for f in self.__hooks[key][KeyEventEnum.ALL]: f(key, new_event)
        
        if not new_event in self.__hooks[key]: return
        for f in self.__hooks[key][new_event]: f(key, new_event)
        
    
    def hook_keyboard(self, keys, on_event, function):
        for key in keys:
            if not key in self.__hooks: 
                self.__hooks[key] = {}
                keyboard.on_press_key(key, lambda _: self.call_hook(key, KeyEventEnum.PRESS))
                keyboard.on_release_key(key, lambda _: self.call_hook(key, KeyEventEnum.UP))

            if not on_event in self.__hooks[key]:
                self.__hooks[key][on_event] = []
            
            self.__hooks[key][on_event].append(function)