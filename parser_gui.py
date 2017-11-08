#Nicholas Pirrello
#10/25/17
#Parse_Gui
#User Interface for summary_csv_parser and billing_csv_parser
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QPushButton, QTableWidget,QTableWidgetItem,QGridLayout,QHeaderView, QFileDialog, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon

import sys
import csv_parser

class Summary(QWidget):

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

		#Window init
		self.setGeometry(300,300,1000,600)
		self.setWindowTitle('Axe Monthly Summary')
		self.show()

	def imprt_click(self):
		filename = QFileDialog.getOpenFileName(self,'Open File','C://','CSV (*.csv)')[0]
		if filename:
			data_list = csv_parser.init_parse(filename)
			self.tableWidget.setRowCount(len(data_list))
			for row in range(0,len(data_list)):
				self.tableWidget.setItem(row, 0, QTableWidgetItem(data_list[row]['name']))
				self.tableWidget.setItem(row, 1, QTableWidgetItem(str(data_list[row]['preproc'])))
				self.tableWidget.setItem(row, 2, QTableWidgetItem(str(data_list[row]['postproc'])))
				self.tableWidget.setItem(row, 3, QTableWidgetItem(str(data_list[row]['percentage'])))


	def reset_click(self):
		self.tableWidget.clear()
		self.tableWidget.setRowCount(0)
		self.tableWidget.setHorizontalHeaderLabels("Company;PreTax;PostTax;Percent".split(";"))

	def savePDF_click(self):
		text, okPressed = QInputDialog.getText(self,"PDF Saving","PDF File Name:",QLineEdit.Normal,"")
		if okPressed and text != '':
			print(text)

			
if __name__ == '__main__':
	app = QApplication(sys.argv)
	summary = Summary()
	sys.exit(app.exec_())