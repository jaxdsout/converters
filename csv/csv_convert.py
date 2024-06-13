from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Helvetica', size=16, style="B")
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align='L', ln=1)
    pdf.line(10, 22, 200, 22)

    for i in range(38, 270, 12):
        pdf.ln(12)
        pdf.line(12, i, 198, i)

    pdf.ln(10)
    pdf.set_font(family='Helvetica', size=10, style="B")
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=8, txt=f"{pdf.page_no()}", align='R', ln=1)

    pdf.set_font(family='Helvetica', size=8, style="I")
    pdf.set_text_color(140, 140, 140)
    pdf.cell(w=0, h=8, txt=f"{row['Topic']}", align='R', ln=1)

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        for r in range(20, 270, 12):
            pdf.ln(12)
            pdf.line(12, r, 198, r)

        pdf.ln(10)
        pdf.set_font(family='Helvetica', size=10, style="B")
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=8, txt=f"{pdf.page_no()}", align='R', ln=1)

        pdf.set_font(family='Helvetica', size=8, style="I")
        pdf.set_text_color(140, 140, 140)
        pdf.cell(w=0, h=8, txt=f"{row['Topic']}, cont.", align='R', ln=1)

pdf.output("output.pdf")
