#import libraries

import os
import csv

#start with 0 for number of votes
total_votes = 0

#set up empty list for candidates
candidates = []

#set up empty list for vote counts
vote_counts = []

#set path to data set
poll_data = "election_data.csv"
poll_path = os.path.join(poll_data)

#open and read csv file 
with open(poll_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    #skip over header
    row = next(csvreader,None) 

    #start for loop to count each vote
    for row in csvreader:

        #add up all the votes for each candidate, increase by 1
        total_votes = total_votes + 1

        #third column is index 2 (beacause of offset)
        candidate = row[2]

#if candidate from candidates list has other votes, then add to vote total
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
#add to candidates list
        else:
            candidates.append(candidate)
            vote_counts.append(1)

#set up empty lists for vote percents and vote counts
vote_percents = []
high_votes = vote_counts[0]
max_index = 0

#calculate percentage of votes for each candidate
#each candidate votes/ total votes * 100
for count in range(len(candidates)):
    percent_votes = vote_counts[count]/total_votes*100
    vote_percents.append(percent_votes)

    if vote_counts[count] > high_votes:
        high_votes = vote_counts[count]
        print(high_votes)
        max_index = count

#assign winner from highest vote count in list
winner = candidates[max_index]

#print statements for results. \n means print next line. set as
#print statements for results. \n means print next line. set as var results to call in print

results = (
    f"Election Results: \n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    f"{candidates[0]}: got {vote_counts[0]} votes {round((vote_counts[0]/total_votes)*100,2)}%\n"
    f"{candidates[1]}: got {vote_counts[1]} votes {round((vote_counts[1]/total_votes)*100,2)}%\n"
    f"{candidates[2]}: got {vote_counts[2]} votes {round((vote_counts[2]/total_votes)*100,2)}%\n"
    f"{candidates[3]}: got {vote_counts[3]} votes {round((vote_counts[3]/total_votes)*100,2)}%\n"
    f"-------------------------\n"
    f"And the winner is {winner}! \n"
    f"\n"
            )

print(results)

# Output to text file
txtOutputPath = os.path.join('PyPoll.txt')
with open(txtOutputPath, "w") as done:
    done.write(results)
