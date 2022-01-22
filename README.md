# election_analysis
Using Python to analyze election outcomes 

Overview of Election Audit: Explain the purpose of this election audit analysis.

The purpose of this audit analysis was to evauate the outcomes of the election in three counties in Colorodo. 

Election-Audit Results: Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.

  1) How many votes were cast in this congressional election?
 
    There were a total of 369,711 votes cast in this congressional election. I was able to determine this by first loading and reading the csv file with a csv reader. Before that however, I made sure to initialize a total voter count using total_votes = 0. Next, I kipped the header row of the csv file using the next() method. I then retreived the first item of the each row using a for loop in the file reader. Lastly, to count up all the votes, I iterated through each row and incremented the total_votes using total_votes +=1. To print this in the terminal, the code print(total_votes) can be used. Please see code visual below.
    
   ![image](https://user-images.githubusercontent.com/96396696/150655872-30b63b9d-4305-44d7-a5c9-d68b9add8c04.png)

  2) Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  
    There are three counties in this data set: Jefferson, Denver, and Arapahoe. The turnout for Jefferson was 38,855, which is 10.5% of the toal turnout. Denver had 306,055 people vote, which was 82.8% of the total turnout, and lastly at 6.7% Arapahoe had a turnout of 24,801. For this result, I first extrated teh county name from each row using indexing on the for loop variable, row. Next, I used an if statement with the not in membership operator to check if the county has been added to the list. Please see screenshot below. I then used the append() method to add county_options to a list. Lastly, I made sure to move the county_votes[county_name] += 1 outside of the if state so that it will count counties. 
    
 ![image](https://user-images.githubusercontent.com/96396696/150656225-45c0094d-b67e-47ee-beff-c40f3661d1b2.png)  
    
  3) Which county had the largest number of votes?
     
     Denver had the largest number of votes.
     
   4) Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
   
      There are three candidates in this data set:Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. Charles received 23.0% of the total votes (n=85,213), Diana received 73.8% of the total votes (n=272,892) and Raymon received 3.1% of the total votes (n=11,606).
     
Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
