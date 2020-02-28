from miahgui import s
from MiahNum import *

exec(s)

class Vertex:
    def __init__(self, x=0, y=0, r=10, color=black):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
    def show(self):
        circle(self.x, self.y, self.r, self.color)

class Edge:
    def __init__(self, vert1, vert2, color=black):
        self.verts = [vert1, vert2]
        self.color = color
        self.thickness = 4
    def show(self):
        v1, v2 = self.verts
        line((v1.x, v1.y), (v2.x, v2.y), self.color, self.thickness)

class Graph:
    def show(self):
        for edge in self.edges:
            edge.show()
        for vert in self.vertices:
            vert.show()
    
class Kgraph(Graph):
    def __init__(self, n):
        self.vertices = []
        r = 50
        cx, cy = 70, 70
        for vert in range(n):
            x = floor(r*cos(2*pi*vert/n - pi/2) + cx)
            y = floor(r*sin(2*pi*vert/n - pi/2) + cy)
            lil_r = minmax(2, 5, 100//n)
            self.vertices.append(Vertex(x, y, lil_r,color_list[vert]))
    
        self.edges = []
        for i in range(n):
            for j in range(i+1, n):
                vert1, vert2 = self.vertices[i], self.vertices[j]
                E = Edge(vert1, vert2)
                E.thickness = 2
                self.edges.append(E)
        self.edges.pop(0)
        self.used = []

    def getNeighbors(self, vert):
        for edge in self.edges:
            if vert in edge.verts:
                v0, v1 = edge.verts
                color = v0.color if vert == v1 else v1.color
                self.edges.remove(edge)
                self.used.append(edge)
                return color
        return None
    
    def remove(self, v0, v1):
        v0, v1 = self.vertices[v0], self.vertices[v1]
        for edge in self.edges:
            if v0 in edge.verts and v1 in edge.verts:
                self.edges.remove(edge)

    def show(self):
        for edge in self.edges:
            edge.color = black
        for edge in self.used:
            edge.color = blue
            edge.show()
        super().show()
    ##----------------------------------------------------------------------
                
class Cgraph(Graph):
    def __init__(self, n):
        self.vertices = []
        for vert in range(n):
            x = floor(r*cos(2*pi*vert/n - pi/2) + cx)
            y = floor(r*sin(2*pi*vert/n - pi/2) + cy)
            lil_r = minmax(2, 10, 300//n)
            self.vertices.append(Vertex(x, y, 5))
    
        v0 = self.vertices[-1]
        v1, v2 = self.vertices[:2]
        v1.y -= 20
        self.edges = [Edge(v0,v1,color_list[0]),
                      Edge(v1,v2,color_list[1]),
                      Edge(v0,v2,color_list[2])]
        for i, v in enumerate(self.vertices[2:]):
            next_v = self.vertices[i+1]
            self.edges.append(Edge(v, next_v))
        
screen = Screen(1000,600)
py.display.set_caption('VDEC of C+_n')

cx, cy = width//2, height//2
r = min(width, height)//2 - 50
vertices = 7

color_list = [green1, red, blue1, mediumorchid, skyblue4,
              lightcoral, lightyellow, coral1, chocolate2,
              rosybrown3, darkgoldenrod2, orange, deepskyblue4,
              cyan3, violetred3, turquoise2,
              orangered2, seashell2, chartreuse, palevioletred4, snow1, cadetblue3, mistyrose3, forestgreen, honeydew3, dodgerblue, mediumseagreen, darkviolet, royalblue, lightgoldenrodyellow, paleturquoise3, grey36, rosybrown2, grey55, darkgrey, pink4, palegreen1, darkslateblue, gray15, sandybrown, grey11, lightskyblue, grey98, turquoise, grey7, lightsteelblue1, grey29, cornsilk2, grey14, lightsteelblue2, gray11, mediumorchid4, gray32, sienna, cornsilk, violetred4, violet, bisque4, darkslategray, darkblue, pink2, gray48, darkorchid3, lemonchiffon4, grey46, burlywood, gray3, grey18, lightblue3, pink3, seagreen1, gray5, cyan2, darkslategray4, palegreen3, grey86, palevioletred, grey52, sienna4, magenta2, bisque2, darkslategrey, cadetblue, green2, thistle, gray74, slategray1, skyblue1, lemonchiffon2, darkolivegreen3, chartreuse1, antiquewhite2, olivedrab2, lightpink, grey73, thistle2, mediumvioletred, mediumspringgreen, grey100, goldenrod3, ivory4, darkorchid4, navajowhite4, floralwhite, lightsteelblue3, darkmagenta, grey70, firebrick1, plum1, orchid3, purple, khaki2, lightyellow2, salmon2, maroon4, lavenderblush, yellow, maroon, orchid4, mediumorchid3, azure2, gray45, lightsalmon4, lightsteelblue4, lightblue1, aquamarine, gray60, green, slategray2, grey51, cornsilk3, royalblue1, plum2, darkseagreen, grey16, grey64, grey53, gray22, grey44, grey49, brown, bisque3, gray24, orangered4, gray71, lightgoldenrod, bisque1, green4, purple3, gray36, seagreen4, steelblue, firebrick2, burlywood1, gray14, thistle4, grey63, goldenrod, sienna1, slateblue4, purple2, paleturquoise, orchid, grey57, slateblue2, slateblue3, lavenderblush1, snow3, steelblue4, gainsboro, saddlebrown, gray75, brown3, gray37, lavender, hotpink1, cadetblue4, powderblue, chartreuse2, gray17, steelblue3, grey21, sienna2, mistyrose1, deeppink3, snow, lightslategray, tomato2, skyblue2, goldenrod4, lightsalmon3, antiquewhite4, tomato4, lightseagreen, skyblue, blanchedalmond, steelblue1, honeydew1, grey83, coral3, blue3, gray57, orange4, hotpink3, grey76, burlywood4, grey40, grey71, lightblue2, navajowhite1, darkorchid, grey94, seagreen2, seashell4, gray100, deeppink2, chartreuse4, salmon4, springgreen2, grey10, olivedrab, gray, gray52, gray76, ivory1, seagreen, purple1, azure1, snow4, gray4, gray29, deepskyblue, gray97, aliceblue, mediumturquoise, yellow2, aquamarine2, rosybrown, grey25, tan3, grey72, brown1, springgreen4, lightskyblue3, darkorange1, grey42, gray53, gray26, gray58, gray6, gold3, indianred4, gray50, grey96, gray85, darkslategray1, gray34, yellow4, lightcyan3, wheat3, grey87, grey31, darkgray, palegreen4, lightgreen, gray54, rosybrown1, seashell1, grey95, seagreen3, grey47, gray44, gray61, cadetblue2, palegreen2, honeydew, orangered1, plum3, orangered, grey37, darkolivegreen4, tomato3, grey69, lightslategrey, gray43, navyblue, olivedrab1, orchid2, grey27, gray77, darkslategray2, gray0, lightgoldenrod2, gray13, darkcyan, grey26, mediumorchid2, grey38, gray42, gray90, gray88, grey2, lightcyan1, mediumpurple1, blue4, khaki3, lightgoldenrod1, slategrey, ivory2, antiquewhite1, sienna3, darkolivegreen1, firebrick, gray80, gray9, gray63, mistyrose4, gray69, azure, maroon3, brown4, red2, gray40, dodgerblue4, darkorange3, blueviolet, grey43, goldenrod2, cyan1, grey48, gray62, navajowhite2, grey82, slategray, chocolate1, grey3, coral, azure3, gray39, mediumpurple4, grey20, midnightblue, grey12, gray78, firebrick4, oldlace, darkgoldenrod4, grey93, plum4, magenta1, grey92, grey68, tomato1, lightgray, gold1, paleturquoise1, gray83, thistle1, grey34, palevioletred1, gray28, gray2, magenta, gray16, grey65, orange1, orangered3, mediumpurple2, grey97, cadetblue1, grey67, beige, gray30, bisque, chocolate4, cornsilk1, aquamarine1, grey13, lightsteelblue, gray27, lavenderblush2, violetred2, dodgerblue3, darksalmon, gray46, wheat, rosybrown4, grey89, steelblue2, lightgoldenrod3, magenta3, gold2, pink, grey60, peachpuff3, grey1, gray65, palevioletred3, coral4, lightskyblue4, lawngreen, grey56, antiquewhite, lightgrey, dimgray, chocolate3, deepskyblue3, gray35, deeppink1, salmon, gray81, plum, thistle3, honeydew4, mistyrose, wheat2, tomato, red1, gray96, lightyellow4, lightsalmon, wheat1, gray91, chartreuse3, grey85, indianred, salmon3, gray41, lightpink1, indianred3, grey91, palevioletred2, greenyellow, cyan4, palegreen, slateblue1, yellow3, gray49, olivedrab4, mediumaquamarine, grey78, lightsalmon2, lavenderblush4, mediumpurple3, gray72, orange2, honeydew2, linen, darkkhaki, gray25, khaki4, gray51, white, peru, peachpuff1, lightcyan2, blue2, salmon1, ivory, darkgreen, antiquewhite3, gray92, lightblue4, gold, indianred1, mediumpurple, burlywood2, aquamarine3, gray99, lightyellow1, royalblue2, moccasin, orchid1, green3, darkgoldenrod, navy, lightpink3, gray38, peachpuff, whitesmoke, grey50, peachpuff2, cornsilk4, grey54, royalblue3, darkolivegreen2, paleturquoise4, gray10, deepskyblue1, mintcream, snow2, grey19, gray66, slategray4, magenta4, gray19, ivory3, darkorange4, darkorchid2, grey45, violetred1, seashell3, gray82, hotpink2, gray64, grey23, gray79, turquoise1, gray87, gray84, seashell, grey9, grey32, orange3, darkgoldenrod1,  ]

#button = Button(screen, (width-30,0,30,20), NoLoop, text='||')
starttitle = Text('Graph Coloring', color = white, size = 70)
start = Startmenu(title = starttitle, bgcolor = (51, 51, 51))

j = max(4, int((sqrt(8*vertices - 15) + 3)//2))
if (j*(j-2)/2+1 < vertices-3) and (j%2 == 0): j += 1

C = Cgraph(vertices)
K = Kgraph(j)

if j % 2 == 1:
    K.remove(0,1)
    K.remove(0,j-1)
else:
    for i in range(0,j-3,2):
        K.remove(i, i+1)

done = False

def circle(x, y, r, color):
    pyg.filled_circle(screen, x, y, r, color)
    pyg.aacircle(screen, x, y, r, color)    

def Setup():
    Background(51)
    C.show()
    
def Draw():
    global done, vertices, C, K
    exists = False
    for edge in C.edges:
        if edge.color == black:
            exists = C.edges.index(edge)
            break

    if exists:
        Next = C.edges[exists]
        if exists == 3:
            color = K.vertices[-1].color
        else:
            start = C.edges[exists - 1]
            ## find vertex of K from edge of C
            that = color_list.index(start.color)
            that_vert = K.vertices[that]
            color = K.getNeighbors(that_vert)
        if color == None:
            ## find a way to add back the edges and start again
            K.edges.append(K.used.pop())
            start.color = black
        else:
            if Next == C.edges[-1] and color in (blue, green):
                pass
            else:
                Next.color = color
            
    elif not done:
        done = True

    else:
        vertices += 1
        
        print(f'vertices : {vertices}')

        j = max(4, int((sqrt(8*vertices - 15) + 3)//2))
        if (j*(j-2)/2+1 < vertices-3) and (j%2 == 0): j += 1

        C = Cgraph(vertices)
        K = Kgraph(j)

        if j % 2 == 1:
            K.remove(0,1)
            K.remove(0,j-1)
        else:
            for i in range(0,j-3,2):
                K.remove(i, i+1)

        done = False
        
    C.show()
    K.show()

    if vertices < 15:
        py.time.delay(500)
    elif vertices < 40:
        py.time.delay(200)        

go()
