from guietta import _, Gui, Quit

gui = Gui(
    ['Enter numbers:', '__a__', '+', '__b__',  ['Calculate']],
    ['Result:  -->', 'result',  _,    _,       ['Reset']],
    [_,    _,  _,   _, Quit]
)

with gui.Calculate:
    gui.result = float(gui.a) + float(gui.b)

with gui.Reset:
    gui.a = 0
    gui.b = 0
    gui.result = 'result'

gui.run()
