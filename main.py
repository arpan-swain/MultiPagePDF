from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="L", unit="mm", format= "a4")

df = pd.read_csv("topics.csv")
for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Helvetica", size= 24, style= "B")
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, ln= 1, border=0, align = "l", txt=row["Topic"])
    pdf.line(10,21,285,21)

    for i in range(row["Pages"] - 1):
        pdf.add_page()


pdf.output("output.pdf")

