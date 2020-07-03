from guietta import Gui, _, ___, III, HS, VS

gui = Gui(

    ['Big label',    ___,       ___,  VS('slider1')],
    [III,    III,       III,       III],
    [III,    III,       III,       III],
    [_, 'a label', 'another label',        _],
    [HS('slider2'),    ___,       ___,        _]
)

gui.run()
