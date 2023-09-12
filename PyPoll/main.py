## import the os module to get the path of csv file
import os

## import the csv module to open and read the election data csv file
import csv

## create a file path
election_data_csvpath = os.path.join("Resources", "election_data.csv")

## read the election data csv file
with open(election_data_csvpath) as election_data_csvfile:

    ## use reader to specifie the delimiter and variables
    election_data_csvreader = csv.reader(election_data_csvfile, delimiter=',')

    ## store the header
    header = next(election_data_csvreader)

    ## set up the defalut values we need to use
    ## defalut value for counting the total votes
    total_votes = 0

    ## defalut value for candidates list
    candidates_list = []

    ## defalut value for count of candidate vote
    vote_number = []

    ## defalut value for the percentage of votes each candidate won
    percent_vote =[]
    
    ## loop through the rows in the file
    for row in election_data_csvreader:

        ## sum the total votes
        total_votes = total_votes + 1

        ## set up condition to store the candidate list and vote count list
        if row[2] not in candidates_list:
            
            ## store the candidate name in the candidate list
            candidates_list.append(row[2])
            
            ## store the count of vote for this candidate and add it up 
            vote_number.append(0)
            index = candidates_list.index(row[2])
            vote_number[index] += 1

            ## store a value for percent of vote for the index space
            percent_vote.append(0)
        
        else:
            ## add up the count of vote for the candidate
            index = candidates_list.index(row[2])
            vote_number[index] += 1

    ## title for the summary
    print(f'Election Results')
    print(f'-------------------------')
    
    ## show the total votes
    print(f'Total Votes: {total_votes}')

    ## break the line
    print(f'-------------------------')

    ## loop through the index of the lists
    for i in range(len(candidates_list)):
        percent_vote[i] =  round((vote_number[i]/ total_votes *100),3)
        print(f'{candidates_list[i]}: {percent_vote[i]}% ({vote_number[i]})')

    ## break the line
    print(f'-------------------------')

    ## show the winner
    for i in range(len(candidates_list)):
        if vote_number[i] == max(vote_number):
            print(f'Winner: {candidates_list[i]}')
    
    ## break the line
    print(f'-------------------------')

election_data_csvfile.close()

## create a file path to write
summary_txtpath = os.path.join("analysis", "PyPoll_summary.txt")

## export the summary to a text file
with open(summary_txtpath, "w") as summary_txtfile:

    ## write the title and break line
    summary_txtfile.write(f'Election Results \n')
    summary_txtfile.write(f'------------------------- \n')
    
    ## write the total number of votes and break line
    summary_txtfile.write(f'Total Votes: {total_votes} \n')
    summary_txtfile.write(f'------------------------- \n')
    
    ## write each candidate with percentage of vote and total vote and break line
    for i in range(len(candidates_list)):
        summary_txtfile.write(f'{candidates_list[i]}: {percent_vote[i]}% ({vote_number[i]}) \n')
    summary_txtfile.write(f'------------------------- \n')
    
    ## write the winner of the election based on the number of votes
    for i in range(len(candidates_list)):
        if vote_number[i] == max(vote_number):
            summary_txtfile.write(f'Winner: {candidates_list[i]}\n')
    summary_txtfile.write(f'------------------------- \n')

summary_txtfile.close()