#sql factory
#read a csv and use data in it to generate sql

#ask user which column contains the IDs, and if the csv file includes a header row
id_column = int(input("Which column in the csv file has the IDs? (Enter 1 for column A, 2 for column B, 3 for column C, etc.: "))
id_column -= 1
start_row = 0
start_row_response = input("Does the csv file include a header row? [Y/N]: ")
if start_row_response.upper() == "Y":
	start_row += 1

#read csv file and save output to list named 'ids'
import csv

with open('TestOutput.csv', newline='') as csvfile:
	filereader = csv.reader(csvfile, delimiter=',')
	rows = list(filereader)
	ids=[]
	for row in rows[start_row:]:
		ids.append(row[id_column])


#define function to write SQL statement(s)
def generate_sql(list):
	#create / open file:
	sql_file = open("sql_output.sql", "a")
	#write sql statement to file for each id
	for id in list:
		#sql_file.write(id + "\n")
		sql_file.write("SELECT ps.PublicationID," + "\n")
		sql_file.write("ps.PublicationSectionID as [SectionID]," + "\n")
		sql_file.write("ps.Name as [SectionName]," + "\n")
		sql_file.write("p.PlacementID," + "\n")
		sql_file.write("p.Name as [PlacementName]" + "\n")
		sql_file.write("FROM dbo.PublicationSection as ps" + "\n")
		sql_file.write("INNER JOIN dbo.Placement as p (nolock) on" + "\n")
		sql_file.write("ps.PublicationSectionID = p.PublicationSectionID" + "\n")
		sql_file.write("WHERE ps.PublicationID = '{}' and ps.IsActive = '1' and p.IsActive = '1' and ps.Name != 'System';".format(id) + "\n")
		sql_file.write("--End Current Statement" + "\n")
	#close file
	sql_file.close()


generate_sql(ids)
#print(ids)