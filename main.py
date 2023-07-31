from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    with open(filepath, "r") as file_r:
        filename = Path(filepath).stem
        heading = filename.capitalize()
        file_data = file_r.read()

        pdf.add_page()

        pdf.set_font(family="Times", size=16)
        pdf.cell(w=0, h=8, txt=heading, ln=1)

        pdf.set_font(family="Times", size=10)
        pdf.multi_cell(w=0, h=6, txt=file_data)

pdf.output("output.pdf")