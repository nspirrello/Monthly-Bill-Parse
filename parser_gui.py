#Nicholas Pirrello
#10/25/17
#Parse_Gui
#User Interface for summary_csv_parser and billing_csv_parser
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QPushButton, QTableWidget,QTableWidgetItem,QGridLayout,QHeaderView, QFileDialog, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
import os
import sys
import csv_parser
import summary_pdf

class Summary(QWidget):
	
	def resource_path(self, relative_path):
		base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
		return os.path.join(base_path, relative_path)

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):

		#button init
		import_bttn = QPushButton('Import')
		reset_bttn = QPushButton('Reset')
		save_pdf_bttn = QPushButton("Save PDF")
		
		import_bttn.clicked.connect(self.imprt_click)
		reset_bttn.clicked.connect(self.reset_click)
		save_pdf_bttn.clicked.connect(self.savePDF_click)

		#Table init
		self.tableWidget = QTableWidget()
		self.tableWidget.setRowCount(0)
		self.tableWidget.setColumnCount(4)
		self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.tableWidget.setHorizontalHeaderLabels("Company;PreTax;PostTax;Percent".split(";"))

		#Grid Layout init
		grid_layout = QGridLayout()
		grid_layout.setSpacing(10)

		grid_layout.addWidget(import_bttn,3,1,1,1)
		grid_layout.addWidget(reset_bttn,3,3,1,1)
		grid_layout.addWidget(save_pdf_bttn,3,2,1,1)
		grid_layout.addWidget(self.tableWidget,1,1,1,3)

		self.setLayout(grid_layout)
		path = self.resource_path('axe_logo.png')
		self.setWindowIcon(QIcon(path))

		#Window init
		self.setGeometry(300,300,1000,600)
		self.setWindowTitle('Axe Monthly Summary')
		self.show()

	def convert_data(self,data):
		new_data = [['Company','PreTax','PostTax','percentage']]

		for i in range(0,len(data)):
			new_data.append(list(data[i].values()))
		return new_data

	def imprt_click(self):
		filename = QFileDialog.getOpenFileName(self,'Open File','C://','CSV (*.csv)')[0]
		if filename:
			self.data_list = csv_parser.init_parse(filename)
			self.tableWidget.setRowCount(len(self.data_list))
			for row in range(0,len(self.data_list)):
				self.tableWidget.setItem(row, 0, QTableWidgetItem(self.data_list[row]['name']))
				self.tableWidget.setItem(row, 1, QTableWidgetItem(str(self.data_list[row]['preproc'])))
				self.tableWidget.setItem(row, 2, QTableWidgetItem(str(self.data_list[row]['postproc'])))
				self.tableWidget.setItem(row, 3, QTableWidgetItem(str(self.data_list[row]['percentage'])))


	def reset_click(self):
		self.tableWidget.clear()
		self.tableWidget.setRowCount(0)
		self.tableWidget.setHorizontalHeaderLabels("Company;PreTax;PostTax;Percent".split(";"))

	def savePDF_click(self):
		text, okPressed = QInputDialog.getText(self,"PDF Saving","PDF File Name:",QLineEdit.Normal,"")
		if okPressed and text != '':

			parsed_data = self.convert_data(self.data_list)
			print(parsed_data)
			print(text)
			doc = summary_pdf.PdfSummary(text+".pdf",parsed_data)
			doc.gen_pdf()
			
if __name__ == '__main__':
	app = QApplication(sys.argv)
	summary = Summary()
	sys.exit(app.exec_())