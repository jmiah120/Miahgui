Button = '''
class Button:
    """ Makes a button that does a thing when clicked.
    methods : show, call
    attributes : surface, rect, func, args, passivecolor, activecolor, rounded,
    passiveform, activeform

    func: the function you want to execute when button is pressed
    args: the arguments you want the function to execute on
    kwargs: the key word arguments you want the function to execute on
    rect: size and position you want the button to have
    surface: the surface you want the button on
    text: the text you want the button to have
    passivecolor: the color of the button when the mouse is not on it
    activecolor: the color of the button when the mouse is on it
    passiveform: Message displayed when the mouse is not on it
    activeform: Message displayed when the mouse is on it
    rounded: How rounded you want the corners to be, should be between 0 & 1
    """
    def __init__(self, func, args:tuple = None, kwargs:dict = None,
                 text:str = None, rect:tuple = None, surface = None,
                 passivecolor:py.Color = grey68, activecolor:py.Color = grey60,
                 passiveform:Message = None, activeform:Message = None,
                 rounded:float = 0.25):
        """Button.__init__()"""
        ## the basics
        self.func         = func 
        self.args         = _ifelse(args, ())
        self.kwargs       = _ifelse(kwargs, {})
        self.text         = _ifelse(text, 'BUTTON')
        self.surface      = _ifelse(surface, _screen_)
        self.passivecolor = _ifelse(passivecolor, grey68)
        self.activecolor  = _ifelse(activecolor, grey60)

        ## rectangle business
        self.rounded     = min(max(0, rounded), 1)
        if rect is None:
            self.rect = py.Rect(0,0,int(1.1*self.text.width+2*self.borderwidth),
                             int(1.1*self.text.height+2*self.borderwidth))
        elif type(rect) is tuple:
            if len(rect) == 2:
                self.rect = py.Rect(*rect,
                                 int(1.1*self.text.width+2*self.borderwidth),
                                 int(1.1*self.text.height+2*self.borderwidth))
            elif len(rect) == 4:
                self.rect = py.Rect(*rect)
            else:
                raise TypeError(f'rect argument must be of length 2 or 4 not {rect}')
        elif type(rect) is py.Rect:
            self.rect = rect
        else:
            raise TypeError(f'rect argument must be Rect or tuple not {rect}')

        ## ---- forms ---- ##
        ## passive
        p = _ifelse(passiveform, Message(text, passivecolor, rect, surface))
        self.passiveform = p
        self.passivecolor = self.passiveform.color
        ## active
        a = _ifelse(activeform, Message(text, activecolor, rect, surface))
        self.activeform = a
        self.activecolor = self.activeform.color
                        
    def show(self, clicked:bool = False) -> None:
        "Renders the button to the screen"
        ## Checks if cursor is on the button 
        condx = self.rect.x <= mouse.x <= self.rect.x + self.rect.w
        condy = self.rect.y <= mouse.y <= self.rect.y + self.rect.h
        if condx and condy:
            self.activeform.show()
            if clicked:
                self.call()
        else:
            self.passiveform.show()

    def call(self) -> None:
        "Executes the buttons function"
        self.func(*self.args, **self.kwargs)

'''
