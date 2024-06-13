import glob

import pandas as pd
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    df = pd.read_csv(filepath)

    pdf.add_page()
    filename = Path(filepath).stem.title()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=40, h=12, txt=f"{filename}")
    pdf.cell(w=200, h=50, txt="")

pdf.output("files/output.pdf")