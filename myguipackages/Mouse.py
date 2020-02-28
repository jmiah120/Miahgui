Mouse = '''
class Mouse:
    """STOP!!! DON'T USE THIS UNLESS YOU'RE REALLY SURE YOU KNOW HOW TO USE IT!!
    Nothing bad will happen, but it just won't really help you much. Peace. 
    """
    def __init__(self):
        """Mouse.__init__()"""
        ## button press things
        self.justpressed = (0,0,0)

        ## visible 
        self.visible = True

    @property
    def pos(self): return py.mouse.get_pos()

    @property
    def x(self):   return self.pos[0]
    
    @property
    def y(self):   return self.pos[1]
    
    @property
    def arepressed(self):  return py.mouse.get_pressed()
    
    @property
    def leftbutton(self):  return self.arepressed[0]
    
    @property
    def scrollwheel(self): return self.arepressed[1]
    
    @property
    def rightbutton(self): return self.arepressed[2]
    
    @property
    def leftbuttonpressed(self):  return self.justpressed[0]
    
    @property
    def scrollwheelpressed(self): return self.justpressed[1]
    
    @property
    def rightbuttonpressed(self): return self.justpressed[2]
    
    def __setattr__(self, name, value) -> None:
        "set self.name to value"
        ## These actually aren't pointless!
        ## These are the mouse things we can change in pygame
        if name == 'justpressed':
            self.__dict__['justpressed'] = value
        elif name == 'visible':
            py.mouse.set_visible(value)
        elif name == 'pos':
            py.mouse.set_pos(value)
        elif name == 'x':
            py.mouse.set_pos([value,self.y])
        elif name == 'y':
            py.mouse.set_pos([self.x,value])
        else:
            if name in self.__dict__:
                raise AttributeError(f"You can't change Mouse attribute '{name}'")
            else:
                raise AttributeError(f"Mouse has no attribute '{name}'")

'''
