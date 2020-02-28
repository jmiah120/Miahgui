import pygame as py

py.init()

class Keyboard:
    def __init__(self):
        self.pressed = []
        self.justpressed = []

py.display.set_mode((10,10))

while True:
    for event in py.event.get():
        print(event.type)
        if event.type == py.KEYDOWN:
            print(event)






    
