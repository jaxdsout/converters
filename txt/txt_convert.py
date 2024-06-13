import glob

import pandas as pd
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem.title()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=40, h=12, txt=f"{filename}", ln=1)

    with open(filepath, "r") as file:
        content = file.read()

    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)


pdf.output("files/output.pdf")