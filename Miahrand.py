""" Hey! Whats up, this is my 'Rawr XD' #random
    library. I made this cause I'm drunk with power
    and I refuse to let something I use not be coded
    from scratch. So,,, yeah. cool.

    Miah - jmiah120@gmail.com
"""
###############################
##      
## Next steps:
##      [X] make randint
##      [X] make choice
##      --- make other distributions
##          ( ) Normal
##          ( ) Beta
##          ( ) Gamma
##          ( ) Binomial
##          ( ) Etc. 
##      [X] Display distribution
##      
##      

_a,_c,_m = 1823972231321,2873943278932,170141183460469231731687303715884105727

from time import time
_num = time()
_x, _y, *_= _num.as_integer_ratio()
_seed = int((_x + _y * _a) ** 4) % _m
del time

def _rand():
    global _seed
    _seed = (_a * _seed + _c) % _m
    _seed = (_a * _a * _seed + _c) % _m
    return _seed

def random() -> float:
    """ Returns a random number on the interval [0,1)
    """
    return _rand()/_m

def randint(a:int, b:int) -> int:
    """ Returns a random integer on the interval [a,b]
    """
    return round((b - a + 1) * random() + a - 0.5)

def choice(seq):
    """ Returns a random value from seq
    """
    seq = list(seq)
    assert len(seq) > 0, 'Cannot choose from empty list'
    i = randint(0, len(seq)-1)
    return seq[i]
    
def choices(k:int, seq) -> list:
    """ Returns k random values from seq with no repeats
    """
    assert k <= len(seq), f'Cannot choose {k} entries from a list of length {len(seq)}'
    seq1, ret = list(seq), []
    for i in range(k):
        c = choice(seq1)
        ret.append(c)
        seq1.remove(c)
    return ret

def rchoices(k:int, seq) -> list:
    """ Returns k random values from seq with repeats
    """
    ret = [choice(seq) for i in range(k)]
    return ret

def randrange(a,b):
    """ Returns a random number on the interval [a,b)]
    """
    return (b - a) * random() + a
    
def EXPO(beta):
    pass

def GAMM(alpha,beta):
    pass

def BETA(alpha,beta):
    pass

def NORM(mu,sigma):
    pass

def UNIF(theta1,theta2):
    pass

def TRIA(theta1,theta2,midpoint):
    pass

def LGNO(mu,sigma):
    pass

def NGEX(beta):
    pass

def PARE():
    pass

def WEIB():
    pass

if __name__ == '__main__':            
    import pygame as py

    def color():
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        return (r,r,r)

    try:
        win = py.display.set_mode((600,600))
        win.fill((255,255,255))

        sidelength = 1
        for x in range(0,600,sidelength):
            for y in range(0,600,sidelength):
                c = color()
                py.draw.rect(win,c,(x,y,sidelength,sidelength))
            py.display.update()

        values = [randint(0,600) for i in range(6000)]

        rect_w = 2
        for x in range(0,600,rect_w):
            k = 0
            for val in values:
                if x<=val<x+rect_w: k += 25/rect_w
            py.draw.rect(win,(0,0,200),(x,550,rect_w,-int(k)))
            py.display.update()
        
        run = 1
        while run:
            for event in py.event.get():
                if event.type == py.QUIT:
                    run = 0
    finally:
        py.quit()
        del py, values
