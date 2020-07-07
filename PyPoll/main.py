import os, csv

#initiate variables
num_votes = 0
candidates = []
unique_candidates = []
most_votes = 0

#name file path
csvpath=os.path.join('Resources','election_data.csv')
#read csv file
with open(csvpath) as datafile:
	csvreader = csv.reader(datafile)

	#skip header row
	header = next(csvreader)

	#Loop through data
	for row in csvreader:
		#get number of votes
		num_votes +=1
		#get all candidates
		each_candidate = row[2]

		#get list of unique candidates
		if each_candidate not in candidates:
			unique_candidates.append(each_candidate)
		#Add candidates to voting list
		candidates.append(each_candidate)

	#print results to terminal
	print('Election Results')
	print('-------------------------')
	print(f'Total Votes: {num_votes}')
	print('-------------------------')

	#create text file
	textpath=os.path.join('analysis','analysis.txt')
	#write text file 
	textfile = open(textpath, "a")

	#print results to text file
	textfile.write("Election Results\n")
	textfile.write('-----------------------------\n')
	textfile.write(f'Total Votes: {num_votes}\n')
	textfile.write('-----------------------------\n')

	#loop through unique candidates to get votes for each candidate
	for candidate in unique_candidates:
		#get the vote count
		candidate_votes = candidates.count(candidate)
		#get percentage of vote
		percent_vote = "{:.3%}".format(candidate_votes / num_votes)
		#print votes by candidate
		print(f'{candidate}: {percent_vote} ({candidate_votes})')
		textfile.write(f'{candidate}: {percent_vote} ({candidate_votes})\n')
		#find the winner
		if candidate_votes > most_votes:
			most_votes = candidate_votes
			winner = candidate
	#print winner
	print('-------------------------')
	print(f'Winner: {winner}')
	print('-------------------------')

	textfile.write('-----------------------------\n')
	textfile.write(f'Winner: {winner}\n')
	textfile.write('-----------------------------\n')