EventHandler = """
def EventHandler(funcy_boi):
    "An event handling decorator"
    def wrapper(*args,**kwargs):
        global _keys_, keydowns, keymods
        try:
            while True:
                ## ---- Event Handling ---- ##
                ## sets all mouse buttons *pressed to 0 this action is for a
                ## momentary click mouse.leftbutton, etc. is for long holds
                mouse.justpressed = (0,0,0)

                ## keyboard controls
                keydowns = py.key.get_pressed()
                keymods  = py.key.get_mods()
                _keys_ = []
                
                for event in py.event.get():
                    if event.type == py.QUIT:       ## quit cond 1 (X button)
                        py.quit()
                        
                    ## Key board handling
                    elif event.type == py.KEYDOWN: 
                        if keymods in (1, 2):       ##   1 - LSHIFT
                            case = upperCase        ##   2 - RSHIFT
                        else:
                            case = lowerCase
                        if event.key == py.K_q:     ## quit cond 2 (CTRL Q)
                            if keymods in (64,128): ##  64 - LCTRL
                                py.quit()           ## 128 - RCTRL
                            else:
                                _keys_.insert(0, case[py.K_q])
                        else:
                            try:
                                _keys_.insert(0, case[event.key])
                            except KeyError as err:
                                raise
                              
                    ## Mouse handling        
                    elif event.type in (py.MOUSEBUTTONDOWN, py.MOUSEBUTTONUP):
                        mouse.justpressed = py.mouse.get_pressed()

                ## run the function
                ret = funcy_boi(*args, **kwargs)
                
                ## handle exit condition of function
                if ret == 'EXIT':
                    return None

        ## IDLE's weird *shrug*
        ## (if you don't know, if you don't include this bit, things get buggy)
        except py.error as err:
            if err.args == ('video system not initialized',): pass
            else: raise
    return wrapper    
"""
