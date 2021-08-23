from pysvg.gradient import *
from pysvg.linking import *
from pysvg.script import *
from pysvg.shape import *
from pysvg.structure import *
from pysvg.style import *
from pysvg.text import *
from pysvg.builders import *
from pysvg.parser import parse

from collections import Counter


class dashboard():

    def __init__(self, vehicle, fonts=["Zekton", "Zekton", "Zekton"], colors=['magenta', 'red']) -> None:
        self.vehicle = vehicle

        self.svg = Svg(width=1000, height=600)

        d = Defs()
        lg = LinearGradient()
        lg.set_gradientTransform("rotate(90)")
        lg.set_id("fire")
        s = Stop(offset="0%")
        s.set_stop_color(colors[0])
        s.set_stop_opacity(1)
        lg.addElement(s)
        s = Stop(offset="100%")
        s.set_stop_color(colors[1])
        s.set_stop_opacity(1)
        lg.addElement(s)
        d.addElement(lg)
        self.svg.addElement(d)

        self.shape_builder = ShapeBuilder()

        self.title_style = StyleBuilder()
        self.title_style.setFontFamily(fontfamily=fonts[0])
        self.title_style.setFontSize('30pt')
        self.title_style.setFontWeight('bold')
        self.title_style.setFilling(fill="url(#fire)")

        self.sub_title_style = StyleBuilder()
        self.sub_title_style.setFontFamily(fontfamily=fonts[1])
        self.sub_title_style.setFontSize('20pt')
        self.sub_title_style.setFontWeight('bold')
        self.sub_title_style.setFilling(fill="darkred")

        self.text_style = StyleBuilder()
        self.text_style.setFontFamily(fontfamily=fonts[2])
        self.text_style.setFontSize('15pt')
        self.text_style.setFontWeight('bold')

        self.rule_style = StyleBuilder()
        self.rule_style.setFontFamily(fontfamily=fonts[2])
        self.rule_style.setFontSize('12pt')
        self.text_style.setFontWeight('bold')

    def titleblock(self, x, y):
        txt = Text(self.vehicle.name, x, y)
        txt.set_style(self.title_style.getStyle())
        self.svg.addElement(txt)
        y += 40

        txt = Text(self.vehicle.v_type, x, y)
        txt.set_style(self.text_style.getStyle())
        self.svg.addElement(txt)
        x += 200

        txt = Text(self.vehicle.weight, x, y)
        txt.set_style(self.text_style.getStyle())
        self.svg.addElement(txt)
        x += 200

        txt = Text(self.vehicle.sponsor, x, y)
        txt.set_style(self.text_style.getStyle())
        self.svg.addElement(txt)

    def ruleblock(self, x, y, width=80,  title="Rules"):
        txt = Text(title, x, y)
        txt.set_style(self.sub_title_style.getStyle())
        self.svg.addElement(txt)
        y += 30

        rules = Counter(self.vehicle.rules)
        for r in rules.keys():
            if not "Ammo" in r.name:
                lines = self.split_text(r.short, width)
                t = f"- {r.name}: {lines[0]}"
                txt = Text(t, x, y)
                txt.set_style(self.rule_style.getStyle())
                self.svg.addElement(txt)
                y += 15
                for l in lines[1:]:
                    txt = Text("   "+l, x, y)
                    txt.set_style(self.rule_style.getStyle())
                    self.svg.addElement(txt)
                    y += 15
                y += 5

    def upgradeblock(self, x, y, title="Weapons & Upgrades"):
        txt = Text(title, x, y)
        txt.set_style(self.sub_title_style.getStyle())
        self.svg.addElement(txt)
        y += 30

        wps = Counter(self.vehicle.weapons)
        ups = Counter(self.vehicle.upgrades)

        for w in wps.keys():
            t = f"- {wps[w]}x {w.direction} {w.name}"
            if len(w.rules) > 0:
                t += ": Rules: "
                for r in w.rules:
                    t += f"{r.name}, "

            txt = Text(t, x, y)
            txt.set_style(self.text_style.getStyle())
            self.svg.addElement(txt)
            y += 25
        for u in ups.keys():
            txt = Text(f"- {ups[u]}x {u.name}", x, y)
            txt.set_style(self.text_style.getStyle())
            self.svg.addElement(txt)
            y += 25

    def attributesblock(self, x, y, title="Attributes", x_spacing=100):
        txt = Text(title, x, y)
        txt.set_style(self.sub_title_style.getStyle())
        self.svg.addElement(txt)
        y += 30

        txt = Text(f"- Handling:", x, y)
        txt.set_style(self.text_style.getStyle())
        self.svg.addElement(txt)

        txt = Text(f"{self.vehicle.handling}", x+x_spacing, y)
        txt.set_style(self.text_style.getStyle())
        self.svg.addElement(txt)

        y += 25

        txt = Text(f"- Max Gear:", x, y)
        txt.set_style(self.text_style.getStyle())
        self.svg.addElement(txt)

        txt = Text(f"{self.vehicle.max_gear}", x+x_spacing, y)
        txt.set_style(self.text_style.getStyle())
        self.svg.addElement(txt)
        y += 25

        txt = Text(f"- Crew:", x, y)
        txt.set_style(self.text_style.getStyle())
        self.svg.addElement(txt)

        txt = Text(f"{self.vehicle.crew}", x+x_spacing, y)
        txt.set_style(self.text_style.getStyle())
        self.svg.addElement(txt)
        y += 25

        txt = Text(f"- Free Slots:", x, y)
        txt.set_style(self.text_style.getStyle())
        self.svg.addElement(txt)

        txt = Text(f"{self.vehicle.slots}", x+x_spacing, y)
        txt.set_style(self.text_style.getStyle())
        self.svg.addElement(txt)
        y += 25

        txt = Text(f"- Gas:", x, y)
        txt.set_style(self.text_style.getStyle())
        self.svg.addElement(txt)

        txt = Text(f"{self.vehicle.cost}", x+x_spacing, y)
        txt.set_style(self.text_style.getStyle())
        self.svg.addElement(txt)
        y += 25

    def hullblock(self, x, y, squaresize=20, x_spacing=60):
        txt = Text("Hull", x, y)
        txt.set_style(self.sub_title_style.getStyle())
        self.svg.addElement(txt)
        x += x_spacing
        y -= squaresize
        for i in range(int(self.vehicle.hull/2)):
            self.svg.addElement(self.shape_builder.createRect(
                x, y, squaresize, squaresize, strokewidth=2))
            self.svg.addElement(self.shape_builder.createRect(
                x, y-squaresize, squaresize, squaresize, strokewidth=2))
            x += squaresize

    def gearblock(self, x, y, squaresize=150, x_spacing=60):
        txt = Text("Gear", x, y)
        txt.set_style(self.sub_title_style.getStyle())
        self.svg.addElement(txt)
        x += x_spacing
        y -= squaresize
        self.svg.addElement(self.shape_builder.createRect(
            x, y, squaresize, squaresize, strokewidth=2))

    def save_svg(self, filename):
        self.svg.save(filename)

    def split_text(self, text, length=80):
        if len(text) <= length:
            return [text]
        ret = []
        s = ""
        for t in text.split():
            if len(s) + len(t)+1 <= length:
                s += t+" "
            else:
                ret.append(s)
                s = t
        return ret
