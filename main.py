from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="L", unit="mm", format= "a4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")
for index, row in df.iterrows():
    pdf.add_page()

    #set header
    pdf.set_font(family="Helvetica", size= 24, style= "B")
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, ln= 1, border=0, align = "l", txt=row["Topic"])
    pdf.line(10,21,285,21)
    for y in range(20,298,10):
        pdf.line(10,y,285,y)
    #set footer
    pdf.ln(175)
    pdf.set_font(family="Times", size=10, style="I")
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=12,ln=1,align="R", txt=row["Topic"])

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        for y in range(20, 298, 10):
            pdf.line(10, y, 285, y)

        pdf.ln(187)
        pdf.set_font(family="Times", size=10, style="I")
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, ln=1, align="R", txt=row["Topic"])


pdf.output("output.pdf")

