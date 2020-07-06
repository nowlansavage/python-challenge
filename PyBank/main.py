import csv, os

#set variables
total_months = 0
net_total = 0
biggest_profit = 0
biggest_loss = 0
num_changes = 0
last_month_prof_loss = 0
sum_change = 0

#name file path
csvpath=os.path.join('Resources','budget_data.csv')
#read csv file
with open(csvpath) as datafile:
	csvreader = csv.reader(datafile)

	#skip header row
	header = next(csvreader)

	#initiate list to calculate changes of profits or losses
	changes=[]

	#loop through each row of the data
	for row in csvreader:

		prof_loss = float(row[1])
		#count months
		total_months +=1 
		#calculate net total
		net_total += prof_loss

		#calculate profit change
		
		prof_change = prof_loss - last_month_prof_loss
		changes.append(prof_change)

		#if value is greater than keep and store date
		if prof_loss > biggest_profit:
			biggest_profit = prof_loss
			prof_date = row[0]

		#if value is less than keep and store date
		if prof_loss < biggest_loss:
			biggest_loss = prof_loss
			loss_date = row[0]
		#set current profit loss to previous profit loss to calculate change
		last_month_prof_loss = prof_loss

	#calculate average profit/loss change
	for change in changes: 
		num_changes += 1
		sum_change += change
	avg_change = sum_change / num_changes

	#format values into dollar format
	avg_change_dollars = "${:,.2f}".format(avg_change)

	biggest_loss_dollars = "${:,.2f}".format(biggest_loss) 
	biggest_profit_dollars = "${:,.2f}".format(biggest_profit)

	net_total_dollars =  "${:,.2f}".format(net_total)

#Add summary to terminal and text file
	print("Financial Analysis")
	print('-----------------------------')
	print(f'total months: {total_months}')
	print(f'Net Profit/Loss: {net_total}')
	print(f'Greatest Profit: {biggest_profit_dollars} on {prof_date}')
	print(f'Greatest Loss: {biggest_loss_dollars} on {loss_date}')
	print(f'Average change: {avg_change_dollars}')

	#create text file
	textpath=os.path.join('analysis','analysis.txt')
	#write text file 
	textfile = open(textpath, "a")

	textfile.write("Financial Analysis\n")
	textfile.write('-----------------------------\n')
	textfile.write(f'total months: {total_months}\n')
	textfile.write(f'Net Profit/Loss: {net_total_dollars}\n')
	textfile.write(f'Greatest Profit: {biggest_profit_dollars} on {prof_date}\n')
	textfile.write(f'Greatest Loss: {biggest_loss_dollars} on {loss_date}\n')
	textfile.write(f'Average change: {avg_change_dollars}\n')


