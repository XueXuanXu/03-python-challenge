## import the os module to get the path of csv file
import os

## import the csv module to open and read the budget_data csv file
import csv

## create a file path
budget_data_csvpath = os.path.join("Resources", "budget_data.csv")

## read the budget_data csv file
with open(budget_data_csvpath) as budget_data_csvfile:

    ## use reader to specifie the delimiter and variables
    budget_data_csvreader = csv.reader(budget_data_csvfile, delimiter=",")

    ## get the header
    header = next(budget_data_csvreader)

    ## set up the default value for the values we need to use in the loop
    ## defalut value for total months count
    total_months = 0

    ## defalut value for net total
    net_total = 0

    ## defalut value for comparing the difference
    previous_profit_or_losses = 1088983

    ## defalut value for total change in profit
    total_change = 0

    ## defalut value for greatest increase in profit
    greatest_increase_date = "Jan-10"
    greatest_increase_value = 0

    ## defalut value for greatest decrease in profit
    greatest_decrease_date = "Jan-10"
    greatest_decrease_value = 0

    ## loop through the rows in the file
    for row in budget_data_csvreader:
        ## count the total months
        total_months = total_months + 1
        
        ## sum the net total
        net_total = net_total + int(row[1])

        ## calculate the difference between the profit and the previous profit
        difference =  int(row[1]) - previous_profit_or_losses
        ## sum the difference to calculate the total change
        total_change = total_change + difference
        ## store the profit value for next comparison
        previous_profit_or_losses = int(row[1])

        ## compare the value for greatest increase in profit
        if difference > greatest_increase_value:
            ## store the new greatest increase values
            greatest_increase_date = str(row[0])                                      
            greatest_increase_value = difference
        
        ## compare the value for greatest decrease in profit
        if difference < greatest_decrease_value:
            ## store the new greatest decrease values
            greatest_decrease_date = str(row[0])                                      
            greatest_decrease_value = difference

    ## title for the summary
    print(f'Financial Analysis')
    print(f'-----------------------------------')

    ## show the total months
    print(f'Total Months: {total_months}')
    
    ## show the net total profit/losses
    print(f'Total: ${net_total}')

    ## calculate average change
    avg_change = total_change / (total_months-1)
    avg_change_rounded = round(avg_change, 2)
    print(f'Average Change: ${avg_change_rounded}')

    ## show the greatest increase in profit
    print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_value})')

    ## show the greatest decrease in profit
    print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_value})')

budget_data_csvfile.close()

## create a file path to write
summary_txtpath = os.path.join("analysis", "PyBank_summary.txt")

## export the summary to a text file
with open(summary_txtpath, "w") as summary_txtfile:
    ## write the title and break line
    summary_txtfile.write('Financial Analysis' + '\n')
    summary_txtfile.write('-----------------------------------' + '\n')
    
    ## write the total months
    summary_txtfile.write('Total Months: ' + str(total_months) + '\n')
    
    ## write the net profit
    summary_txtfile.write('Total: $' + str(net_total)+ '\n')
    
    ## write the average change in profit
    summary_txtfile.write('Average Change: $' + str(avg_change_rounded) + '\n')
    
    ## write the greatest increase in Profits
    summary_txtfile.write('Greatest Increase in Profits: ' + greatest_increase_date + ' ($' + str(greatest_increase_value) +')\n')
    
    ## write the greatest decrease in Profits
    summary_txtfile.write('Greatest Decrease in Profits: ' + greatest_decrease_date + ' ($' + str(greatest_decrease_value) +')\n')

summary_txtfile.close() 

