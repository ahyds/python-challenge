import os
import csv

# Define path of file
bank_csv = os.path.join('','Resources','budget_data.csv')

# Open and read csv
with open(bank_csv,newline="") as csvfile:
    bank_csvreader= csv.reader(csvfile,delimiter=',')
        # Reader header first
    bank_header = next(csvfile)
    #print(f"Header is:  {bank_header}")
            
    # Read through each row of data after the header
    cnt = 0
    total = 0
    change =[]
    result = 0
    date = []
    
    for row in bank_csvreader:
        cnt = cnt +1
        total = total + int(row[1]) 
        if cnt != 1:        
            change.append(int(row[1]) - result)  #fill up list of changes
            date.append(row[0])                  #fill up list of dates
        result = int(row[1])                     #reset result as most recent month value

    #Find extreme change values
    max_chg = max(change)
    min_chg = min(change)

    #Find matching dates by referring index
    date_max = date[change.index(max_chg)]
    date_min = date[change.index(min_chg)]

    print("Financial Analysis\n-----------------------------------")
        
    print(f"Total Months: {cnt}")
    print(f"Total: ${total}")
    print(f"Average Change: ${sum(change)/len(change):.2f}")
    print(f"Greatest Increase in Profits: {date_max} (${max_chg})")
    print(f"Greatest Decrease in Profits: {date_min} (${min_chg})")

    # Output file path
    file_out = open('Resources/output.txt','w+')

    #Write content to file,'\n' to start a new line
    file_out.write (f"Financial Analysis\n-----------------------------------"
        f"\nTotal Months: {cnt}"
        f"\nTotal: ${total}"
        f"\nAverage Change: ${sum(change)/len(change):.2f}"
        f"\nGreatest Increase in Profits: {date_max} (${max_chg})"
        f"\nGreatest Decrease in Profits: {date_min} (${min_chg})"
        )





    





