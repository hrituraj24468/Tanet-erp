from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, letter
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd

styles = getSampleStyleSheet()
style = styles["BodyText"]

canv = Canvas("doc.pdf", pagesize=A4)

header = Paragraph("<bold><font size=18>TPS Report</font></bold>", style)


data = [['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34'],
        ['20', '21', '22', '23', '24'],
        ['20', '21', '22', '23', '24'],
        ['20', '21', '22', '23', '24'],
        ['20', '21', '22', '23', '24']]
t = Table(data)
t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                       ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)]))
data_len = len(data)

for each in range(data_len):
    if each % 2 == 0:
        bg_color = colors.whitesmoke
    else:
        bg_color = colors.lightgrey

    t.setStyle(TableStyle([('BACKGROUND', (0, each), (-1, each), bg_color)]))

aW = 540
aH = 520

w, h = header.wrap(aW, aH)
header.drawOn(canv, 72, aH)
aH = aH - h
w, h = t.wrap(aW, aH)
t.drawOn(canv, 72, aH-h)
canv.save()