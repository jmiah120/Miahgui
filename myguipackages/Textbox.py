from miahgui import s

exec(s)

class TextBox:
    def __init__(self, x, y, w, h, buffer = 10, **kwargs):
        self.rect = (x, y, w, h)
        self._txt_ = ''
        self.kwargs = kwargs
        self.buffer = buffer
        self.slider = Slider(self, self.x + self.width - 25,
                             self.y + self.buffer,
                             self.height - 2 * self.buffer)
        self.subsurf = py.Surface((self.innerwidth, self.innerheight))
        self.subsurf.fill((255,255,255,0))
        self.kwargs['surface'] = self.subsurf
        kwargs = self.kwargs.copy()
        kwargs['color'] = grey69
        self.Text = Text('Type text here', **kwargs)
        self.Text.show((0,0))

    @property
    def txt(self):
        return self._txt_

    @txt.setter
    def txt(self, value):
        self._txt_   = value
        self.Text    = Text(value, **self.kwargs)
        self.subsurf = py.Surface((self.innerwidth, self.Text.height))
        self.kwargs['surface'] = self.subsurf
        self.subsurf.fill(white)
        self.Text.surface = self.subsurf
        self.Text.show((0,0))

    @property
    def bufferrect(self):
        slider = 26 if self.slider else 0
        return (self.x + self.buffer,
                self.y + self.buffer,
                self.width - 2 * self.buffer - slider,
                self.height - 2 * self.buffer)
    @property
    def innerrect(self):
        bx, by, bw, bh = self.bufferrect
        return (bx + 2, by + 2, bw - 4, bh - 4)

    @property
    def x(self): return self.rect[0]
        
    @x.setter
    def x(self, value):
        x, y, w, h = self.rect
        self.rect  = (value, y, w, h) 
        
    @property
    def y(self): return self.rect[1]
        
    @property
    def width(self): return self.rect[2]
        
    @property
    def height(self): return self.rect[3]

    @property
    def bufferx(self): return self.bufferrect[0]
        
    @property
    def buffery(self): return self.bufferrect[1]
        
    @property
    def bufferwidth(self): return self.bufferrect[2]
        
    @property
    def bufferheight(self): return self.bufferrect[3]
        
    @property
    def innerx(self): return self.innerrect[0]
        
    @property
    def innery(self): return self.innerrect[1]
        
    @property
    def innerwidth(self): return self.innerrect[2]
        
    @property
    def innerheight(self): return self.innerrect[3]

    @property
    def bumpheight(self):
        Ih = self.innerheight
        Th = self.Text.height
        Bh = self.bufferheight - 20
        if Th <= Ih:
            return Bh
        else:
            thing1 = 15
            thing2 = Bh*Ih/Th
            return max(thing1, thing2)
        
    @staticmethod
    def _fit_text(string):
        yield string
        words = string.split(sep = ' ')
        yield f"{' '.join(words[:-1])}\n{words[-1]}"
        yield f"{string[:-2]}-\n{string[-2:]}"
        yield f"{string[:-3]}-\n{string[-3:]}"

    def show(self):
        rrect(*self.rect, cornflowerblue, 0.1, True)
        rect(*self.bufferrect, white, True)
        self.slider.bump.height = self.bumpheight
        p  = self.slider.percent 
        ## manipulate this line to make less white space at the bottom
            ## of the text box. Also make the slider bump change size
            ## as we type more text. :) Night, love you <3
        ## Done :)
        _control = min(self.Text.height, 0.5*self.height)
        _py = Map(p, 0, 1, 0, self.Text.height - _control) 
            
        _screen_.blit(self.subsurf, (self.innerx, self.innery),
                      (0,_py,self.innerwidth, self.innerheight),
                      py.BLEND_RGBA_MIN)
        try:
            if _keys_[0] == 'DEL':
                newtxt = self.txt[:-1]
            else:
                newtxt = f'{self.txt}{_keys_[0]}'
               
            for trial in TextBox._fit_text(newtxt):
                self.txt = trial
                if self.Text.width <= self.innerwidth: break
    
        except NameError as err:
            if err.args[0] != "name '_keys_' is not defined": raise
        except IndexError as err:
            pass
        finally:
            self.slider.show()

class Slider:
    def __init__(self, parent, x = None, y = None, h = None,
                 orientation = 'vert', side = 'right'):
        if orientation == 'vert' and side == 'right':
            self.x = _ifelse(x, parent.x + parent.width - 15)
            self.y = _ifelse(y, parent.y)
            self.height = _ifelse(h, parent.height)
            self.bump = Bump(self.x + 2, self.y + 10, 15, self.y + self.height - 10)
            
    def show(self):
        rect(self.x, self.y, 15, self.height, grey91, True)
        self.bump.show()

    @property
    def percent(self):
        return self.bump.percent

class Bump:
    def __init__(self, x, y, h, bottom):
        self.x, self.y = x, y
        self.width, self.height = 11, h
        self.bottom = bottom
        self.top = y
        
    @property
    def rect(self):
        return (self.x, self.y, self.width, self.height)

    @property
    def percent(self):
        total = (self.bottom - self.height) - self.top + 1
        perce = (self.y - self.top)/(total)
        return perce

    def show(self):
        x, y, w, h = self.rect
        if self.x - 5 <= mouse.x <= self.x + 10 and mouse.leftbutton:
            self.y = minmax(self.top, self.bottom - self.height, mouse.y)
        rect(x, self.y, w, h, grey31, True)

def Map(thing, whichisfrom, to, From, To) -> float:
    destRange = To - From
    srceRange = to - whichisfrom
    thingZ    = (thing - whichisfrom)/srceRange 
    thingEnd  = float(thingZ*destRange + From)
    return thingEnd
      

Screen(600, 400)

textbox = TextBox(10, 10, 300, 200)

def Setup():
    Background(51)

def Draw():
    try:
        textbox.x += 1
        textbox.show()
    except OverflowError:
        print(textbox.x - 1)
        raise
go()

