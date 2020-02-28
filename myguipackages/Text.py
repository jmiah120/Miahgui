Text = '''
class Text:
    """ Creates an object to render text on the screen. Fully mutable.
        methods : show, get_rect
        attributes : string, surface, font, txt, x, y, width, height,
        centerx, centery
    
        string:  the string you want displayed
        surface: the surface you want string displayed to
        font:    the font you want string displayed with
        size:    the size of the font you want string displayed as
        AA:      if you want anti aliasing or not
        color:   the color you want your string to display as
        pos:     the position you want to render the top-left corner of string at
    """
    def __init__(self, string:str, surface = None, font:str = None,
                 size:int = None, AA:bool = None,
                 color:tuple = None, pos:tuple = (None, None)):
        """Text.__init__()"""
        ## the basics
        self._string_ = string
        self.strings  = string.split(sep = '\\n') 
        self.surface  = _ifelse(surface, _screen_)
        
        ## font dict                                                    
        self._FONT_   = _ifelse(font, _sysfont_)                         
        self.size     = _ifelse(size, _sysfontsize_)                     
        self.font     = self._FONT_          
        
        ## render details                                               
        self.AA       = _ifelse(AA, _sysfontAA_)                         
        self.color    = _ifelse(color, _sysfontcolor_)                   
        self.x        = _ifelse(pos[0], 0)                               
        self.y        = _ifelse(pos[1], 0)   
        self.txt      = [self.font.render(STR, self.AA, self.color)
                         for STR in self.strings]                 

        ## things we'll want after we have a txt object 
        self.width    = max(line.get_width() for line in self.txt)
        self.height   = len(self.strings)*(self.size + 2)

    @property
    def centerx(self):
        return self.width//2 + self.x

    @property
    def centery(self):
        return self.height//2 + self.y

    @centerx.setter
    def centerx(self, value):
        self.x = value - self.width//2
        
    @centery.setter
    def centery(self, value):
        self.y = value - self.height//2

    @property
    def center(self):
        return (self.centerx, self.centery)

    @center.setter
    def center(self, value: tuple):
        self.x = value[0]
        self.y = value[1]

    @property
    def string(self):
        return self._string_
    
    @string.setter
    def string(self, value):
        self._string_ = value
        self.strings  = value.split(sep = '\\n')
        self.txt      = [self.font.render(STR, self.AA, self.color)
                         for STR in self.strings]            
        self.width    = max(line.get_width() for line in self.txt)
        self.height   = len(self.strings)*(self.size + 2)
        self.centerx  = self.width//2 + self.x
        self.centery  = self.height//2 + self.y

    @property
    def font(self):
        return py.font.SysFont(self._FONT_, self.size)

    @font.setter
    def font(self, name):
        try:
            self._FONT_ = name
            self.txt      = [self.font.render(STR, self.AA, self.color)
                             for STR in self.strings]
        except AttributeError:
            self._FONT_ = name
                                                                                         
    @property
    def rect(self):
        return (self.x, self.y, self.width, self.height)
    
    @property
    def pos(self):
        return (self.x, self.y)
    
    @pos.setter
    def pos(self, value):
        self.x, self.y = value
    
    def show(self, pos:tuple = None, rect:tuple = None) -> None:  
        """Renders self onto screen at the given position.
        (top-left corner)"""
        if pos  is None: pos  = self.pos
        w, h = max(self.width, width), max(self.height, height)
        if rect is None: rect = (0, 0, w, h)
        for num, line in enumerate(self.txt):
            k = num*(self.size + 2)
            if rect[0] <= pos[1] + k <= rect[3]:
                self.surface.blit(line, (pos[0], pos[1] + k))

'''



                
