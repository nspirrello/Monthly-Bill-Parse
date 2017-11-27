#Summary_pdf
#Nicholas Pirrello
#11/08/17
#PDF generator for Summary reports
from reportlab.platypus import Paragraph, Table, Image, TableStyle, SimpleDocTemplate
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch, mm
import os.path
import os
import sys
import time
import datetime
#Reference of https://www.blog.pythonlibrary.org/2012/06/27/reportlab-mixing-fixed-content-and-flowables/
class PdfSummary():

	def resource_path(self, relative_path):
		base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
		return os.path.join(base_path, relative_path)

	def __init__(self, filename, data):
		i = 1
		original_name = filename
		while os.path.isfile(filename):
			docname = filename[0:len(original_name) - 4]
			extension = '.pdf'
			filename = docname + '(' + str(i) + ')' + extension
			i+=1
		self.file = filename
		self.doc = SimpleDocTemplate(filename,pagesize=letter,rightMargin=30,leftMargin=30,topMargin=30,bottomMargin=18)
		self.elements = []
		self.styles = getSampleStyleSheet()
		self.stylesWrap = self.styles["BodyText"]
		self.data = data


	def gen_pdf(self):
		#Create Header bar

		path = self.resource_path('axe_logo_pdf.png')	
		logo = Image(path)

		self.elements.append(logo)

		#Description
		description = """<font size="12">This table has been outputted through the Billing Summary application's pdf generator. This file, {}, was generated {}.</font>""".format(self.file,datetime.datetime.now().strftime("%m-%d-%y"))
		desc = Paragraph(description, self.stylesWrap)


		self.elements.append(desc)

		bufferwords = Paragraph("",self.stylesWrap)

		self.elements.append(bufferwords)

		#Create data table
		style_table = TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
                       ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                       ('VALIGN',(0,0),(0,-1),'TOP'),
                       ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                       ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ])

		wrap = self.stylesWrap
		wrap.wordWrap = 'CJK'

		data2 = [[Paragraph(cell,wrap) for cell in row] for row in self.data]
		data_table = Table(data2)
		data_table.setStyle(style_table)

		self.elements.append(data_table)

		self.doc.build(self.elements)

	def coord(self, x, y, unit=1):
		x, y = x * unit, self.height - y * unit
		return x, y