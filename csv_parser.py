#Nicholas Pirrello
#10/16/2017
#CSVParser
#CSV --> JSON Parser for monthly billing form
import csv
import json
import datetime

def main():
	#Open the specified .csv file, read in the file to the "data" variable, then
	#call parse_list on "data" in order change to a more suitable format.
	file = open('J:/Tasks/Task1.csv')
	reader = csv.reader(file, delimiter=',')
	data = list(reader)
	parse_list(data)

def parse_list(list):
	#Loop through the .csv reader output, since only the first set of data is needed
	#stop interating when a blank entry is found in the reader list. If you 
	#find "PartnerId" store it as "identifier_row", this is the begining row of the data.
	#for every iteration that occurs before a blank is found, append it to a new list
	#which holds the needed data. Find the column where the "CustomerCompanyName" and
	#"PostTaxTotal" data can be found and store these column values. Call 
	#"parse_relevant_sections" with the new list, "important_data_block", our starting
	#row and our columns where the data we need can be found. 
	post_tax_total_col = 0;
	company_name_col = 0;
	identifier_row = 0;
	
	important_data_block = []
	i = 0
	while len(list[i]) != 0:
		if "PartnerId" in list[i]:
			identifier_row = i
		important_data_block.append(list[i])
		i+=1
	
	for j in range(0, len(important_data_block[identifier_row])):
		
		if important_data_block[identifier_row][j] == "CustomerCompanyName":
			company_name_col = j
		elif important_data_block[identifier_row][j] == "PostTaxTotal":
			post_tax_total_col = j
	parse_relevant_sections(important_data_block, identifier_row, company_name_col, post_tax_total_col)

def parse_relevant_sections(list, identifier_row, company_name_col, post_tax_total_col):
	#For every company that is not the disculed_company, if they are already "seen"
	#then add the new charge value to their current dictionary value. If they haven't 
	#been seen then create their dictionary space and store their charge value as 
	#"preproc". Then call calculate.
	discluded_company = 'AXE CREATIVES'
	seen_companies = []

	i = identifier_row
	for i in range(i+1, len(list)):
		comp_name = list[i][company_name_col]
		comp_tax = list[i][post_tax_total_col]
		if comp_name != discluded_company and comp_name != '':
			if is_in(seen_companies, comp_name) == True:
				for i in seen_companies:
					if i['name'] == comp_name:
						preproc = float(i['preproc'])
						i['preproc'] = round(float(comp_tax) + preproc,2)
			else:
				comp_data = {'name':comp_name, 'preproc':round(float(comp_tax),2), 'postproc':0, 'percentage':.40}
				seen_companies.append(comp_data)						
	calculate(seen_companies)

def is_in(list, name):
	#If the specified name is found in the list, return True, otherwise False
	for i in list:
		if i['name'] == name:
			return(True)
	return(False)

def calculate(list):
	#For every company in the seen list, calculate using their pre-tax charges 
	#by multiplying their charges by their percentage, follwed by storing the total
	for i in list:
		preproc = i['preproc']
		percent = i['percentage']
		postproc = preproc * percent + preproc
		i['postproc'] = round(float(postproc), 2)
	print(list)

def to_JSON(list):
	#JSON fille structure
	current = datetime.datetime.now()
	file_date = 
	with open()

if __name__ == "__main__":
	main()