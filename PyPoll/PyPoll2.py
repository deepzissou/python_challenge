#PyRoll
#===========================================================================

import os
import csv
import collections #(Geek for geek)
from collections import Counter #(Geek for geek)

#Set csv path for import


csv_path = os.path.join("PyPoll","election_data.csv")

#creating a path for exporting the final data text file
analysis_output = os.path.join("Analysis", "election_data_analysis.txt")

#Establish variables and lists to track "Votes per Candidate 

vpc = []
Candidates = []


#Read the csv file

with open(csv_path) as elecData:
    reader =csv.reader(elecData, delimiter=",")



#For loop to count the total number of votes through each row in the csv file

    for row in reader:
        
        #Append values to Candidates 
        Candidates.append(row[2])

#Creating a list of candidates with the sorted function (Geek for geek)
#Sorted function: returns a new list containing all items from the iterable in ascending order
    new_list = sorted(Candidates)

#Couning votes for each candidate
cand_cnt = Counter(new_list)

#Appending the new "Counter" list to "Voter per Candidate" variable 
#most_common() is used to produce a sequence of the n most frequently
#  encountered input values and their respective counts. (Geek for geek)

vpc.append(cand_cnt.most_common())

#Formulating Candidate vote percentange per candidate
for item in vpc:

#using format () method
# This method of the built-in string class provides functionality
#  for complex variable substitutions and value formatting. (Geek for Geek)
#Example: item [0][1] row, column

    Winner = format((item[0][1])*100/(sum(cand_cnt.values())),'.2f')
    Runner_up = format((item[1][1])*100/(sum(cand_cnt.values())),'.2f')
    Honorable_mention = format((item[2][1])*100/(sum(cand_cnt.values())),'2f')
    Last_place = format((item[3][1])*100/(sum(cand_cnt.values())),'2f')

#Creating my Election Results Summary and Printing out the results in terminal

print(f"                                            ")
print(f"Election Results")
print(f"===========================================") 
print(f"Total Votes:  {sum(cand_cnt.values())}") #Adding the total Candidates count list for total votes
print(f"===========================================")
print(f"{vpc[0][0][0]}: {Winner}% ({vpc[0][0][1]})")
print(f"{vpc[0][1][0]}: {Runner_up}% ({vpc[0][1][1]})")
print(f"{vpc[0][2][0]}: {Honorable_mention}% ({vpc[0][2][1]})")
print(f"{vpc[0][3][0]}: {Last_place}% ({vpc[0][3][1]})")
print(f"===========================================")
print(f"Winner: {vpc[0][0][0]}")
print(f"===========================================")


with open(analysis_output,'w') as output:

    output.write("Election Results\n")
    output.write(f"===========================================\n")
    output.write(f"Total Votes:  {sum(cand_cnt.values())}\n")
    output.write(f"===========================================\n")
    output.write(f"{vpc[0][0][0]}: {Winner}% ({vpc[0][0][1]})\n")
    output.write(f"{vpc[0][1][0]}: {Runner_up}% ({vpc[0][1][1]})\n")
    output.write(f"{vpc[0][2][0]}: {Honorable_mention}% ({vpc[0][2][1]})\n")
    output.write(f"{vpc[0][3][0]}: {Last_place}% ({vpc[0][3][1]})\n")
    output.write(f"===========================================")
    output.write(f"Winner: {vpc[0][0][0]}\n")
    output.write(f"===========================================")








