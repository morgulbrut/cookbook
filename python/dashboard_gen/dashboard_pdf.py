#!/usr/bin/python

from reportlab.lib import colors
from reportlab.lib.pagesizes import A5, landscape

from reportlab.pdfgen import canvas

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from collections import Counter


class dashboard():

    def __init__(self, vehicle,
                 title_font="fonts/Railway To Hells.ttf",
                 subtitle_font="fonts/Road_Rage.ttf",
                 text_font="fonts/AGENCYB.TTF",
                 title_colour='magenta',
                 subtitle_colour='darkred',
                 text_colour='black') -> None:
        self.vehicle = vehicle
        pdfmetrics.registerFont(TTFont('subtitle', subtitle_font))
        pdfmetrics.registerFont(TTFont('title', title_font))
        pdfmetrics.registerFont(TTFont('text', text_font))
        try:
            self.title_colour = colors.getAllNamedColors()[title_colour]
        except KeyError:
            self.title_colour = colors.black
        try:
            self.subtitle_colour = colors.getAllNamedColors()[subtitle_colour]
        except KeyError:
            self.subtitle_colour = colors.black
        try:
            self.text_colour = colors.getAllNamedColors()[text_colour]
        except KeyError:
            self.text_colour = colors.black
        self.canvas = canvas.Canvas(
            self.vehicle.name+".pdf", pagesize=landscape(A5))

    def titleblock(self, x, y):
        textobject = self.canvas.beginText()
        textobject.setTextOrigin(x, y)
        textobject.setFont('title', 15)
        textobject.setFillColor(self.title_colour)
        textobject.textLine(self.vehicle.name)
        textobject.setFont('text', 10)
        textobject.setFillColor(self.text_colour)
        textobject.setTextOrigin(x+20, y-15)
        textobject.textLine(
            f"{self.vehicle.v_type}  -  {self.vehicle.weight}  -  Crew: {self.vehicle.crew}  -  Handling: {self.vehicle.handling}  -  Max. Gear: {self.vehicle.max_gear}  -  Empty Slots: {self.vehicle.slots}  -  Gas: {self.vehicle.cost}")
        self.canvas.drawText(textobject)

    def ruleblock(self, x, y, width=80,  title="Rules"):
        textobject = self.canvas.beginText()
        textobject.setTextOrigin(x, y)
        textobject.setFont('subtitle', 15)
        textobject.setFillColor(self.subtitle_colour)
        textobject.textLine(title)
        textobject.setTextOrigin(x, y-15)
        textobject.setFont('text', 10)
        textobject.setFillColor(self.text_colour)

        rules = Counter(self.vehicle.rules)
        for r in rules.keys():
            if not "Ammo" in r.name:
                lines = self.split_text(r.short, width)
                t = f"- {r.name}: {lines[0]}"
                textobject.textLine(t)
                for l in lines[1:]:
                    textobject.textLine("    "+l)

        self.canvas.drawText(textobject)

    def upgradeblock(self, x, y, title="Weapons & Upgrades"):
        textobject = self.canvas.beginText()
        textobject.setTextOrigin(x, y)
        textobject.setFont('subtitle', 15)
        textobject.setFillColor(self.subtitle_colour)
        textobject.textLine(title)

        textobject.setTextOrigin(x, y-15)
        textobject.setFont('text', 10)
        textobject.setFillColor(self.text_colour)

        wps = Counter(self.vehicle.weapons)
        ups = Counter(self.vehicle.upgrades)
        for w in wps.keys():
            t = f"- {wps[w]}x {w.direction} {w.name}"
            if len(w.rules) > 0:
                t += ": Rules: "
                for r in w.rules:
                    t += f"{r.name}, "
            textobject.textLine(t)

        for u in ups.keys():
            t = f"- {ups[u]}x {u.name}"
            if len(u.rules) > 0:
                t += ": Rules: "
                for r in u.rules:
                    t += f"{r.name}, "
            textobject.textLine(t)

        self.canvas.drawText(textobject)

    def hullblock(self, x, y, squaresize=15):
        textobject = self.canvas.beginText()
        textobject.setTextOrigin(x, y)
        textobject.setFont('subtitle', 15)
        textobject.setFillColor(self.subtitle_colour)
        textobject.textLine("Hull")

        self.canvas.drawText(textobject)

        y -= squaresize+10
        for i in range(int(self.vehicle.hull/2)):
            self.canvas.rect(x, y, squaresize, squaresize)
            self.canvas.rect(x, y-squaresize, squaresize, squaresize)
            x += squaresize

    def gearblock(self, x, y, squaresize=60):
        textobject = self.canvas.beginText()
        textobject.setTextOrigin(x, y)
        textobject.setFont('subtitle', 15)
        textobject.setFillColor(self.subtitle_colour)
        textobject.textLine("Gear")
        self.canvas.drawText(textobject)

        y -= squaresize+10
        self.canvas.rect(x, y, squaresize, squaresize)

    def save_pdf(self):
        self.canvas.save()

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

    def default_dashboard(self):
        self.titleblock(30, 380)
        self.upgradeblock(50, 330)
        self.hullblock(330, 330)
        self.gearblock(500, 330)
        self.ruleblock(50, 200)

        self.save_pdf()


def main():
    c = canvas.Canvas(r"coords.pdf", pagesize=landscape(A5))
    pdfmetrics.registerFont(TTFont('subtitle', 'fonts/Road_Rage.ttf'))
    pdfmetrics.registerFont(TTFont('title', 'fonts/Road_Rage.ttf'))
    pdfmetrics.registerFont(TTFont('text', 'fonts/AGENCYB.TTF'))

    # c.setFont("title", 10)  # choose your font type and font size
    # c.drawString(50, 600, "Welcome to Reportlab!")
    # c.setFont("text", 10)  # choose your font type and font size
    # c.drawString(10, 500, "Welcome to Reportlab!")

    for x in [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]:
        for y in [50, 100, 150, 200, 250, 300, 350, 400, 450]:
            c.drawString(x, y, f"{x}x{y}")

    c.save()


if __name__ == "__main__":
    main()
