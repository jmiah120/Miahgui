""" A module to do basic animations and algorithms.
    Uses a Setup and a Draw function.
"""

s = '''
## This centers the screen
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
## cleanup
del os

## import necessary thingies
import pygame as py
from pygame.color import THECOLORS as C
import pygame.gfxdraw as pyg
from MiahNum import *

## Defines some colors for us... a lot of colors
    ## 657 of them
colors = []
for name, val in C.items():
    exec(f'{name} = py.Color{val}')
    colors.append(name)
## cleanup
del C

## initializing py modules
py.init()

## keyboard inputs
from myguipackages.keyboarddicts import lowerCase, upperCase
exec(f'lowerCase = {lowerCase}')
exec(f'upperCase = {upperCase}')

## Event Handling Decorator 
from myguipackages.EventHandler import EventHandler
exec(EventHandler)

## -------------------------- Some Helpful Classes -------------------------- ##

from myguipackages.Text import Text
exec(Text)

from myguipackages.Message import Message
exec(Message)
        
from myguipackages.Button import Button
exec(Button)
        
from myguipackages.Startmenu import Startmenu
exec(Startmenu)
        
from myguipackages.Mouse import Mouse
exec(Mouse)
        
from myguipackages.Colorshader import Colorshader
exec(Colorshader)
        
from myguipackages.Canvas import Canvas
exec(Canvas)
        
class IDE:
    pass

class Menu:
    pass

## ------------------ Our two main functions!! (and go...) ------------------ ##

def _setup_() -> None:
    "Internal function for setting up your canvas"
    global _hasbeensetup_
    ## we only want to call this once
    if not _hasbeensetup_:
        try:
            Setup()
            py.display.update(_focusrect_)
            _hasbeensetup_ = True
            _draw_()
        except NameError as err:
            if err.args ==("name 'Setup' is not defined",):
                raise NameError('You gotta have a Setup function')
            else: raise
    else: raise Exception('_setup_ has already been called')

def _draw_() -> None:
    "Internal function for drawing your canvas"
    if _hasbeensetup_:
        #getting the defaults left by Setup
        bgcolor      = _bgcolor_
        fill         = _fill_
        strokeweight = _strokeweight_
        stroke       = _stroke_

        @EventHandler
        def _draw_handler_():
            """A function to handle eveything in the draw function"""
            ## Reset our defaults (otherwise things get screwy)
            Background(bgcolor)
            Fill(fill)
            StrokeWeight(strokeweight)
            Stroke(stroke)

            ## run our loop
            if _loop_:
                if _bgcolor_:
                    py.draw.rect(_screen_,_bgcolor_,(-10,-10,width+20,height+20))
                try: Draw()
                except NameError as err:
                    if err.args == ("name 'Draw' is not defined",):
                        raise NameError('You gotta have a Draw function')
                    else:
                        py.quit()
                        raise
                except:
                    py.quit()
                    raise
                py.display.update(_focusrect_)
            else:
                ## function for if _loop_ is False
                try: Except()
                except NameError as err:
                    if err.args == ("name 'Except' is not defined",):
                        pass
                    else: raise

        ## this handles the screen/click functionality
        _draw_handler_()
    else:
        raise Exception("Didn't get setup properly")    

def go() -> None:
    "Starts running the program"
    try:
        if _screen_ == None: Screen(600, 400)
        if _startmenuexists_: _startmenu_()
        else: _setup_()
    except py.error as err: ## -- pygame is weird -- ##
        if err.args == ('video system not initialized',): pass
        else: raise
    except:
        py.quit()
        raise

## -------------------------------------------------------------------------- ##

def NoLoop() -> None:
    """Prevents Draw() from looping"""
    global _loop_
    _loop_ = False

def YesLoop() -> None:
    """Starts Draw looping again. Only works in Except()
    or the same call of Draw() as NoLoop()."""
    global _loop_
    _loop_ = True

def Screen(W, H, **kwargs) -> 'screen':
    "Cretes a lil window to do things on."
    global width, height, _screen_
    _screen_      = py.display.set_mode((W, H), **kwargs)
    width, height = _screen_.get_size()
    setfocus(0,0,width,height)
    return _screen_

def Background(*args) -> None:
    """background(int) -> greyscale
    background(r,g,b) -> color
    background(None) -> None
    Sets the color of the background.
    """
    global _bgcolor_
    if args == (None,):
        _bgcolor_ = None
    elif type(args[0]) == py.Color:
        _bgcolor_ = args[0]
        py.draw.rect(_screen_, _bgcolor_, (0, 0, width, height))
    else:
        color = py.Color(args[0], args[0], args[0]) if len(args) == 1 else py.Color(*args)
        _bgcolor_ = color
        py.draw.rect(_screen_, _bgcolor_, (0, 0, width, height))

def _rrect(surface,rect,color,radius=0.25) -> None:
    """Makes a rounded rectangle :)
    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """
    x1,y1,w,h = rect
    r = int(min(w,h)*radius/2)
    d = (2*r,)*2
                ## upper left  |  upper right #######
    corners = ((x1+r,y1+r),     (x1+w-r-1,y1+r),     ## shhh, just imagine
               (x1+r,y1+h-r-1), (x1+w-r-1,y1+h-r-1)) ## this looks nice. 
                ## lower left  |  lower right #######
    circles = [i+(r,) for i in corners]
            ##    up/down     |    left/right   ##
    rects = ((x1+r,y1,w-2*r,h), (x1,y1+r,w,h-2*r))
    for i in rects: py.draw.rect(surface, color, i)
    for i in circles:
        i = [int(j) for j in i]
        pyg.filled_circle(surface,*i,color)
        pyg.aacircle(surface,*i,color)

def _ifelse(A, B):
    "Returns A if A is not None else B"
    return A if A is not None else B

## ----------------------------- Draw commands ------------------------------ ##

def rrect(x, y, w, h, color=None, radius=0.25, NoStroke = False) -> None:
    """Makes a rounded rectangle :)
    x, y    : upper left corner coordinates
    w, h    : width and height of bounding rectangle
    color   : rgb or rgba value
    radius  : 0 <= radius <= 1
    """
    if _stroke_ and not NoStroke:
        _rrect(_screen_, (x,y,w,h), _stroke_, radius)
        x += _strokeweight_
        y += _strokeweight_
        w -= 2 * _strokeweight_
        h -= 2 * _strokeweight_
        
    color = _ifelse(color, _fill_)
    _rrect(_screen_, (x,y,w,h), color, radius)

def circle(x:int, y:int, r:int, color:py.Color = None, NoStroke = False) -> None:
    "Draws a circle on the screen!"
    color = _ifelse(color, _fill_)
    stroke = min(max(0, r - _strokeweight_), r)

    ## the stroke
    if _stroke_ and not NoStroke:
        pyg.aacircle(_screen_, x, y, r, _stroke_)
        pyg.filled_circle(_screen_, x, y, r, _stroke_)

    ## the actual circle
    pyg.aacircle(_screen_, x, y, stroke, color)
    pyg.filled_circle(_screen_, x, y, stroke, color)
   
def ellipse(x:int, y:int, r_x:int, r_y:int, color:py.color = None, NoStroke = False) -> None:
    "Draws an ellipse on the screen"
    color = _ifelse(color, _fill_)
    var = _strokeweight_/min(r_x, r_y)
    strokex = min(max(0, r_x - _strokeweight_), r_x)
    strokey = min(max(0, r_y - _strokeweight_), r_y)

    ## the formulas for a big ellipse and lil ellipse
    ell1 = lambda x,y: ((x*x)/(r_x*r_x)) + ((y*y)/(r_y*r_y))
    ell2 = lambda x,y: ((x*x)/(strokex*strokex)) + ((y*y)/(strokey*strokey))

    ## the stroke and actual ellipse
    if _stroke_ and not NoStroke:
        for i in range(x-r_x-1, x+r_x+1):
            for j in range(y-r_y-1, y+r_y+1): 
                if ell2(i-x,j-y) <= 1: ## the ellipse
                    pyg.pixel(_screen_, i,j, color)
                    continue
                elif ell1(i-x,j-y) <= 1: ## the stroke
                    pyg.pixel(_screen_, i,j, _stroke_)
                    continue
        pyg.aaellipse(_screen_, x, y, strokex, strokey, color) ## the ellipse
        pyg.aaellipse(_screen_, x, y, r_x, r_y, _stroke_) ## the stroke
        return None ## call this for just a lil more speed

    else:
        ## or just the ellipse
        for i in range(x-r_x-1, x+r_x+1):
            for j in range(y-r_y-1, y+r_y+1): 
                if ell2(i-x,j-y) <= 1:
                    pyg.pixel(_screen_, i,j, color)
        pyg.aaellipse(_screen_, x, y, strokex, strokey, color)

def arc():
    #center, start point, stop_point
    #py.draw.arc(_screen_, _fill_,  )
    pass

def rect(x:int, y:int, w:int, h:int, color: py.Color = None, NoStroke = False):
    "Draws a rectangle on the sceen!"
    color = _ifelse(color, _fill_)
    if _stroke_ and not NoStroke:
        py.draw.rect(_screen_, _stroke_, (x,y,w,h))
        _x = x + _strokeweight_ 
        _y = y + _strokeweight_ 
        _w = w - 2*_strokeweight_ 
        _h = h - 2*_strokeweight_ 
        py.draw.rect(_screen_, color, (_x, _y, _w, _h))
    else:
        py.draw.rect(_screen_, color, (x,y,w,h))
        
def line(startpos, endpos, color, width = 1):
    x1, y1 = startpos
    x2, y2 = endpos
    x, y = x2-x1, y2-y1
    h = dist(x1, y1, x2, y2)
    w = width
    if h == 0:
        py.draw.circle(_screen_, color, startpos, 1)
        return None
    elif w == 1:
        py.draw.aaline(_screen_, color, startpos, endpos)
        return None
    elif x == 0:
        a, b = w/2, 0
    elif y == 0:
        b, a = w/2, 0
    else:
        a, b = -(w*y)/(2*h), (w*x)/(2*h)

    points = [(x1+a, y1+b), (x2+a, y2+b),
              (x2-a, y2-b), (x1-a, y1-b)]
    
    pyg.aapolygon(_screen_, points, color)
    pyg.filled_polygon(_screen_, points, color)

def polygon(x, y, z):
    py.draw.polygon()
    pass

def Print(message:str, **kwargs):
    """Prints a string to the screen
    possible kwargs: 
    surface, font, size, AA (anti-aliasing), color,
    pos. See help(Text) for more info.
    """
    text = Text(message, **kwargs)
    text.show()


#py.draw.polygon
#py.draw.lines
#py.draw.line
#py.draw.aalines
#py.draw.aaline

## ------------------------------ Draw tools! ------------------------------- ##

def Fill(color):
    "Sets the color for any shapes you want to draw"
    global _fill_
    if type(color) == py.Color:
        _fill_ = color
    elif type(color) == int:
        _fill_ = py.Color(color, color, color)
    else:
        raise TypeError(f'Fill argument must be color or int not {color}')

def Stroke(color):
    global _stroke_
    if type(color) == py.Color:
        _stroke_ = color
    elif type(color) == int:
        _stroke_ = py.Color(color, color, color)
    elif color is None:
        NoStroke()
    else:
        raise TypeError(f'Stroke argument must be color or int not {color}')

def StrokeWeight(thickness):
    global _strokeweight_
    if type(thickness) == int:
        _strokeweight_ = thickness
    else:
        raise TypeError(f'StrokeWeight argument must be int not {thickness}')

def NoStroke():
    global _strokeweight_, _stroke_
    _strokeweight_ = 0
    _stroke_ = None



    
    
def setfocus(x = 0, y=0, w=None, h=None, rect=None) -> None:
    """Makes it so the screen only updates in the given rect.
    Defaults to the whole screen. 
    """
    global _focusrect_
    w = _ifelse(w, width)
    h = _ifelse(h, height)
    rect = _ifelse(rect, (x,y,w,h)) 
    _focusrect_ = rect

## ---------------------------- Setting defaults ---------------------------- ##

## Text defaults
_sysfont_      = 'Arial'
_sysfontsize_  = 12
_sysfontcolor_ = black
_sysfontAA_    = True

## System defaults/operational variables
_hasbeensetup_    = False
_startmenuexists_ = False
_startmenu_       = None
_screen_          = None

## Things you call
width  = 0
height = 0
mouse  = Mouse()

## Secret things you can call w/ functions
_loop_         = True
_focusrect_    = py.Rect(0,0,width,height)
_bgcolor_      = black
_fill_         = white
_strokeweight_ = 2
_stroke_       = black 

del s
'''

if __name__ == '__main__':
    try:
        ## --- Need this --- ##
        ## Need s, don't write it as a string tho
        "from Miahgui2 import s"

        ## --- Need this --- ##
        ## This line imports all the necessary functions as native
        exec(s)

        ## --- Need this --- ##
        ## Sets up a screen 
        Screen(600, 400)

        ## makes a startmenu
        startmenu = Startmenu(title = 'Hello, World!', bgcolor = grey78)

        ## A friendly button
        button = Button(print, ('clicked',), {'end':'!\t'}, 'Click Me!',
                        (width//2 + 50, height//2 - 31, 100, 62))

        #colorshader = Colorshader(100, 10, 100, _screen_)
        canvas = Canvas(10, 10, 300, 300)

        ## --- Need this --- ##
        ## Sets up your program 
        def Setup():
            Background(grey40)
            print('Start!')

        ## --- Need this --- ##
        ## This Loops over and over again
        def Draw():
            button.show(mouse.leftbuttonpressed)
            canvas.show()            
                
        ## This gets called if you don't want Draw to loop anymore
        def Except():
            pass
        
        ## --- Need this --- ##
        ## runs the program
        go()
        
    except:
        py.quit()
        raise
















