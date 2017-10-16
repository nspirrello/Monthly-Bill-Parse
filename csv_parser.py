#Nicholas Pirrello
#10/16/2017
#CSVParser
#CSV --> JSON Parser for monthly billing form
import csv

def main():
	file = open('J:/New folder/SummaryTaskOne.csv')
	reader = csv.reader(file)
	data = list(reader)
	
	parse_list(data)


def parse_list(list):
	post_tax_total_col = 0;
	company_name_col = 0;
	identifier_row = 0;
	
	important_data_block = []
	i = 0
	while list[i][0] != "Daily Usage" or list[i][0] ==" ":
		if list[i][0] == "PartnerId":
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
	#go from ident to end of list 
	#for every occurence where ccn isnt AXE creatives, take the post tax and add it to a total
	discluded_company = 'AXE CREATIVES'
	seen_companies = []

	i = identifier_row
	for i in range(i+1, len(list)):
		comp_name = list[i][company_name_col]
		if comp_name != "AXE CREATIVES": 
			comp_data = {'name':comp_name, 'preproc':0, 'postproc':0}
			seen_companies.append(comp_data)
	print(seen_companies)

#def update_tax_total(list):


if __name__ == "__main__":
	main()