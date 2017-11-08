#Summary_pdf
#Nicholas Pirrello
#11/08/17
#PDF generator for Summary reports
from reportlab.platypus import Paragraph, Table, Image
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch, mm

#Reference of https://www.blog.pythonlibrary.org/2012/06/27/reportlab-mixing-fixed-content-and-flowables/
class PdfSummary():

	def __init__(self, filename):
		self.c = canvas.Canvas(filename,pagesize=letter)
		self.styles = getSampleStyleSheet()
		self.width, self.height = letter

	def gen_pdf(self):
		#Create Header bar
		words = """<font size="16">Summary Billing Report</font>"""
		header_para = Paragraph(words, self.styles["Heading1"])

		logo = Image("axe_logo.png")
		logo.drawHeight = 1*inch
		logo.drawWidth = 1*inch

		headerbr = [[logo,header_para]]
		header = Table(headerbr, colWidths=4*inch)
		header.setStyle([("VALIGN",(0,0),(0,0),"TOP")])
		header.wrapOn(self.c,self.width,self.height)
		header.drawOn(self.c,*self.coord(18,60,mm))

		#Create data table

	def coord(self, x, y, unit=1):
		x, y = x * unit, self.height - y * unit
		return x, y

	def savePDF(self):
		self.c.save()

def main():
	doc = PdfSummary("test4.pdf")
	doc.gen_pdf()
	doc.savePDF()

if __name__ == '__main__':
	main()

