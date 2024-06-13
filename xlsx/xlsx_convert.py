from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_no, date = filename.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice No. {invoice_no}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    columns = list(df.columns)
    headers = [column.replace("_", " ").title() for column in columns]

    pdf.set_font(family='Arial', size=8, style='B')
    pdf.cell(w=30, h=8, txt=headers[0], border=1)
    pdf.cell(w=70, h=8, txt=headers[1], border=1)
    pdf.cell(w=30, h=8, txt=headers[2], border=1)
    pdf.cell(w=30, h=8, txt=headers[3], border=1)
    pdf.cell(w=30, h=8, txt=headers[4], border=1, ln=1)

    for index, row in df.iterrows():
        pdf.set_font(family='Arial', size=8)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    total = df['total_price'].sum()
    pdf.set_font(family='Arial', size=8)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total), border=1, ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=10, txt=f"Total Due: {total}", ln=1)
    pdf.cell(txt='your company', w=50, ln=1)
    pdf.ln(5)
    pdf.image("logo.png", w=10)

    pdf.output(f"pdfs/{filename}.pdf")



