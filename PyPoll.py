#file_to_load = 'election_results.csv'
#with open(file_to_load) as election_data:
     #print(election_data)

#import os
#dir(os.path)

#file_to_save = os.path.join("election_analysis.txt")
#with open(file_to_save, "w") as txt_file:
     #txt_file.write("Hello World")

 # Write three counties to the file.
     #txt_file.write("Arapahoe")
     #txt_file.write("Denver")
     #txt_file.write("Jefferson")

# Write three counties to the file and separate by comma
     #txt_file.write("Arapahoe, ")
     #txt_file.write("Denver, ")
     #txt_file.write("Jefferson")

#adding all three counties to one line, like this:
     #txt_file.write("Arapahoe, Denver, Jefferson")

#writing each on a new new line with a dash after the header
     #txt_file.write("Counties in the election")
     #txt_file.write("\n-------------------------------")
     #txt_file.write("\nArapahoe\nDenver\nJefferson")
#--------------------------------------------------------------------#
#Now it's time to read the election_results.csv file
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join( "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #after running this bit of code, you get a read out of the csv file
    #for row in file_reader:
        #print(row)      

#Retreiving the first item from each row
#for row in file_reader:
    #print(row[0])

#To skip the header row of the CSV file, use the next() method
    headers = next(file_reader)
    print(headers) #here we have confirmed that we skipped the header row