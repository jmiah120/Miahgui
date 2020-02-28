Canvas = '''
class Canvas:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = (x, y, w, h)
        self.innerrect = (x + 10, y + 60, w - 20, h - 70)
        self.colorshader = Colorshader(x + 10, y + 10, 20)
        self.pen = black
        self.points = [[]]

    def show(self):
        self()
        _rrect(_screen_, self.rect, grey69)
        _rrect(_screen_, self.innerrect, white)
        self.colorshader.show()
        for curve in self.points:
            for i, point in enumerate(curve):
                x, y, C = point
                try:
                    x2, y2, C2 = curve[i+1]
                except IndexError:
                    pass
                except:
                    raise
                else:
                    Canvas.line((x, y), (x2, y2), C, 2)

    def mouse_in_draw_area(self):
        x,y,w,h = self.innerrect
        return (x < mouse.x < x+w) and (y < mouse.y < y+h)

    def __call__(self):
        x, y = mouse.x, mouse.y
        if self.colorshader.is_near(x, y) and mouse.leftbutton:
            self.pen = self.colorshader(x, y)
        elif self.mouse_in_draw_area() and mouse.leftbutton:
            self.addpoint(x, y, self.pen)
        else:
            self.addpoint(None)

    def addpoint(self, *args):
        if args == (None,):
            if self.points[-1] != []:
                self.points.append([])
        else:
            self.points[-1].append(args)

    @classmethod
    def line(cls, startpos, endpos, color, width = 1):
        line(startpos, endpos, color, width)
        pyg.aacircle(     _screen_, *startpos, width//2, color)
        pyg.filled_circle(_screen_, *startpos, width//2, color)
        pyg.aacircle(     _screen_, *endpos,   width//2, color)
        pyg.filled_circle(_screen_, *endpos,   width//2, color)

'''
