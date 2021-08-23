# textobject_demo.py
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def textobject_demo():
    pdfmetrics.registerFont(TTFont('subtitle', 'fonts/Road_Rage.ttf'))

    my_canvas = canvas.Canvas("txt_obj.pdf",
                              pagesize=letter)
    # Create textobject
    textobject = my_canvas.beginText()
    # Set text location (x, y)
    textobject.setTextOrigin(10, 730)
    # Set font face and size
    textobject.setFont('Times-Roman', 12)
    # Write a line of text + carriage return

    textobject.textLine(text='Python rocks!')
    # Change text color
    textobject.setFont('subtitle', 13)
    textobject.setFillColor(colors.red)
    # Write red text
    textobject.textLine(text='Python rocks in red!')
    # Write text to the canvas
    my_canvas.drawText(textobject)
    my_canvas.save()


if __name__ == '__main__':
    textobject_demo()
