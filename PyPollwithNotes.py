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
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("election_analysis.txt")

# Open the election results and read the file.
#we will initialize a variable called total_votes to zero.
#The total_votes variable needs to be placed above the code where we open the file, using the with open() statement. 
total_votes = 0
#add candidate options
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
    #after running this bit of code, you get a read out of the csv file
    #for row in file_reader:
        #print(row)      

#To skip the header row of the CSV file, use the next() method
     headers = next(file_reader)
    #print(headers) #here we have confirmed that we skipped the header row

#Retreiving the first item from each row
     for row in file_reader:
          print(row[0])

#To count up all the votes, we iterate through each row and increment the total_votes
          total_votes += 1
#print(total_votes) prints out the total votes

#To get the candidate from each list when we iterate through the row, 
#we can use indexing on the for loop variable, row. 
          # Print the candidate name from each row
          candidate_name = row[2]

          #Add the candidate name to the candidate list.
          #andidate_options.append(candidate_name)

#we do not want every candidate from each row. 
#Instead, we need to get only the unique candidate names.
#To get the unique names in the candidate_options list, 
#we can use an if statement with the not in membership operator 
#to check if the candidate has been added to the list.
# If the candidate does not match any existing candidate...
          if candidate_name not in candidate_options:
            # Add it to the list of candidates.
               candidate_options.append(candidate_name)

               candidate_votes[candidate_name] = 0
          candidate_votes[candidate_name] += 1 
          #we moveed the line of code above outside of the if statement so that it will count candidates, it wont do that inside the if statement
     

#Print the candidate list.
     #print(candidate_options) 

#print the candiate vote dictionary
     #print(candidate_votes) 

#count the votes for each candidate in the if statement as you 
#iterate through the rows of the CSV file, but first we need a dictionary
#this will help us give each candidate a key and 1 value for their name which then can be summed
#first you have to create an empty dictionary just like we did with candidate_options
#candidate_votes = {"candidate_name1": votes, "candidate_name2": votes, "candidate_name3": votes}

#Inside the if statement, we need to instantiate a candidate as a key for the dictionary. In other words, we need to create a key from the unique candidates.
#We can use dictionary_name[key] to create a key
#to create each candidate as a key, use candiate_votes[candidate_name] = 0 and add it inside the if statement 

#How to get percentages
#vote_percentage = (votes / total_votes)*100 but we need another for loop to do this
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
     votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
     vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
#This is code below is what will get you the % for each candidate
print(f"{candidate_name}: received {vote_percentage:,.{2}} % of the vote.")

#determine the winning candidate, vote count, and percentage
#need to use a decision statement to compare the number of votes each candidate received
#first step is to declare a variable but always put it before the with open()
#winning_candidate = ""
#winning_count = 0
#winning_percentage = 0
# To do: print out each candidate's name, vote count, and percentage of

# votes to the terminal.
#print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#second step: we will create an if statement inside the for loop and do the following (3.5.5)
#Determine if the vote count that was calculated is greater than the winning_count.

if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent = vote_percentage.
          winning_count = votes
          winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
          winning_candidate = candidate_name

with open(file_to_save, "w") as txt_file:
#  To do: print out the winning candidate, vote count and percentage
     winning_candidate_summary = (
     f"-------------------------\n"
     f"Winner: {winning_candidate}\n"
     f"Winning Vote Count: {winning_count:,}\n"
     f"Winning Percentage: {winning_percentage:.1f}%\n"
     f"-------------------------\n")
print(winning_candidate_summary)