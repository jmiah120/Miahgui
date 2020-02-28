Startmenu = '''
class Startmenu:
    """Creates a little startmenu :)  Just call it to run it.
    E.g. startmenu = Startmenu(); startmenu();
    methods : show, __call__
    attributes : surface, bgcolor, width, height, startbutton, exitbutton,
    buttons, title

    surface: the surface you want the menu to run on
    startbutton: a button to start running the program
    exitbutton: a button to stop running the program
    bgcolor: back ground color for the menu
    buttons: want any other buttons? add 'em here
    title: the title of your program
    """
    def __init__(self, surface = None, startbutton:Button = True,
                 exitbutton:Button = True, bgcolor:py.Color = black,
                 buttons:list = [], title:str = ''):
        """Startmenu.__init__()"""
        ## taking care of some system globals
        global _startmenuexists_, _startmenu_
        _startmenuexists_ = True
        _startmenu_ = self

        ## the basics
        self.surface = _ifelse(surface, _screen_)
        if self.surface == _screen_ == None:
            self.surface = Screen(600, 400)
        self.bgcolor = _ifelse(bgcolor, black)
        self.width, self.height = self.surface.get_size()

        ## ---- Buttons ---- ##
        ## start
        if startbutton is True:
            rect = (self.width//2 - 50, self.height//2 - 31, 100, 62)
            self.startbutton = Button(_setup_, text = 'Start!', rect = rect,
                                      surface = self.surface,
                                      passivecolor = green2,
                                      activecolor = green3, rounded = 0.1)
        elif type(startbutton) is Button:
            self.startbutton = startbutton
        elif startbutton is False:
            self.startbutton = Button(None)
        else:
            raise TypeError(f'Button value must be boolean or Buttton not {startbutton}')

        ## exit
        if exitbutton == True:
            rect = (self.width - 55, 5, 50, 31)
            self.exitbutton = Button(py.quit, text = 'Quit', rect = rect, 
                                     surface = self.surface,
                                     passivecolor = red2,
                                     activecolor = red4)
        elif type(exitbutton) == Button:
            self.exitbutton = exitbutton
        elif exitbutton == False:
            self.exitbutton = Button(None)
        else:
            raise TypeError(f'Button value must be boolean or Buttton not {exitbutton}')

        ##others
        self.buttons = [self.startbutton, self.exitbutton] + buttons

        ## title
        if type(title) == str:
            self.title = Text(title, self.surface, size = 40)
        elif type(title) == Text:
            self.title = title
        else:
            raise TypeError(f'Title must be Text or str not {title}')

    def show(self, clicked:bool = False) -> None:
        """Renders the menu to the screen. Clicked is the criteria
        for a button to be considered pressed. 
        """
        self.surface.fill(self.bgcolor)
        _x, _y = self.title.width, self.title.height
        ## Displays title in the middle and 100 pix down
        self.title.show((self.width//2 - _x//2, 100 - _y))
        ## Shows the buttons and takes care of calling them if needed
        for button in self.buttons:
            button.show(clicked)

    @EventHandler
    def __call__(self) -> None:
        "Runs the menu"
        self.show(mouse.leftbuttonpressed)
        py.display.update()
        py.time.delay(10)

'''
