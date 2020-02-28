Colorshader = '''
class Colorshader:
    """ Draws a colorshader to the screen! Working on click-ability...
    methods : show, is_in, is_near
    attributes : x, y, r, centerx, centery, surf, surfPar

    x : the x position you want the top left corner of the bounding rectangle
    y : the y position you want the top left corner of the bounding rectangle
    r : the radius of the color shader
    surface : the surface you want the color shader drawn to 
    """
    def __init__(self, x:int, y:int, r:int, surface = None):
        """Colorshader.__init__()"""
        ## the surface of the color shader
        self.surf = py.Surface((2*r+1,2*r+1))
        self.surf.fill((255,255,255,0))

        ## the surface it gets drawn to 
        self.surfPar = _ifelse(surface, _screen_)
        
        ## coords
        self.x, self.y, self.r     = x, y, r 
        self.centerx, self.centery = x + r, y + r

        ## figuring out the pixel values of each pixel in the rect
        ## v v slow
        self._draw_()

    def _pointCircle(self, a, b, h, k, r, sign='='):
        """Returns distance between a point (a,b)
        and an empty or filled circle r^2=(x-h)^2+(y-k)^2
        """
        if sign=='>' and r**2<(a-h)**2+(b-k)**2: return 0
        elif sign=='<' and r**2>(a-h)**2+(b-k)**2: return 0            
        else: return abs(r-sqrt((a-h)**2+(b-k)**2))

    def _findColor(self,fx,fy):
        """Finds the desired color of a given pixel
        """
        x,y,r = self.x,self.y,self.r
        fx,fy = fx-r,fy-r
        m = sqrt(3)
        if (fx)*(fx)+(fy)*(fy)>r*r:
            return (255,255,255,0)
        else:
            s = '<'
            sub = 255/r
            var = 1.5
            red = sub*var*self._pointCircle(fx,fy,0,r,r,sign=s)
            red = 255-min(max(0, red), 255)
            green = sub*var*self._pointCircle(fx,fy,m*r/2,-r/2,r,sign=s)
            green = 255-min(max(0, green), 255)
            blue = sub*var*self._pointCircle(fx,fy,-m*r/2,-r/2,r,sign=s)
            blue = 255-min(max(0, blue), 255)
            return (red, green, blue, 255)

    def show(self):
        """Renders the colorshader to the screen 
        """
        x, y, r = self.x, self.y, self.r

        py.draw.circle(self.surfPar,(255,255,255),(x+r,y+r),r)
        self.surfPar.blit(self.surf,(self.x,self.y),special_flags=py.BLEND_RGB_MIN)

        pyg.aacircle(self.surfPar, r+x, r+y, r, black)
        pyg.aacircle(self.surfPar, r+x, r+y, r-2, black)

    def _draw_(self):
        w, h = self.surf.get_size()
        r = self.r
        for i in range(w):
            for j in range(h):
                if (r-2)**2 <= (i-w//2)**2 + (j-h//2)**2 <= r**2:
                    py.draw.rect(self.surf,black,(i,j,1,1))
                else:
                    color = self._findColor(i,j)
                    py.draw.rect(self.surf,color,(i,j,1,1))
                
    def is_in(self,x,y):
        "Returns true if (x,y) is in the bounding circle."
        return self.r**2 >= (y-self.centery)**2+(x-self.centerx)**2

    def is_near(self, x, y):
        "Returns true if (x,y) is in the bounding rect."
        return (self.x <= x <= self.x+2*self.r) and (self.y <= y <= self.y+2*self.r)

    def __call__(self, x, y):
        if self.is_in(x, y):
            try:
                return self.surf.get_at((x-self.x, y-self.y))
            except IndexError as err:
                if err.args == ('pixel index out of range',):
                    return black
                else:
                    raise
        else: return black

'''
