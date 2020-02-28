Message = '''
class Message:
    """Shows a message in a little rectangle :)  
    methods : show
    attributes : text, color, surface, borderwidth, bordercolor, rounded, rect
    text: the message you want to display
    color: the background color of the message box
    rect: the rectangle that bounds the message box
    surface = the surface you want the message displayed to 
    borderwidth: the thickness of the border. Starts from the bounds and goes in.
    rounded: How rounded you want the corners to be, should be between 0 & 1
    bordercolor: the color... of the border. 
    text*: See help(Text)
    """
    def __init__(self, text:str = '', color:tuple = None, rect:tuple = None,
                 surface = None, borderwidth:int = None, rounded:float = 0.25,
                 bordercolor:tuple = None, textcolor:tuple = None,
                 textsize:int = None, textfont:str = None, textAA:bool = None):
        """Message.__init__()"""
        ## the basics
        self.color       = _ifelse(color, _fill_)
        self.surface     = _ifelse(surface, _screen_)
        self.borderwidth = _ifelse(borderwidth, _strokeweight_)
        self.bordercolor = _ifelse(bordercolor, _stroke_)

        ## font details
        textcolor        = _ifelse(textcolor, _sysfontcolor_)
        textsize         = _ifelse(textsize, _sysfontsize_)
        textfont         = _ifelse(textfont, _sysfont_)
        textAA           = _ifelse(textAA, _sysfontAA_)       
        if type(text) is str:
            self.text = Text(text, self.surface, textfont, textsize, textAA, textcolor)  
        elif type(text) is Text:
            self.text = text
        else:
            raise TypeError(f'text argument must be Text or str not {text}')

        ## rectangle business
        self.rounded = min(max(0, rounded), 1)
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

    def show(self) -> None:
        "Renders the message to it's surface"
        ## getting some handy variables
        x, y, w, h = self.rect.x, self.rect.y, self.rect.w, self.rect.h
        b = self.borderwidth
        text = self.text
        
        ## Drawing our bubble
        _rrect(self.surface, (x, y, w, h), self.bordercolor, self.rounded)
        _rrect(self.surface, (x + b, y + b, w - 2*b, h - 2*b),
               self.color, self.rounded)

        ## Drawing the text
        tx, ty, tw, th = text.rect
        x, y = x - text.centerx + w//2, y - text.centery + h//2
        text.show((x,y))

'''
