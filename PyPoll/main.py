#Dependencies
import os
import csv

# File path
pollcsv = os.path.join('','Resources','election_data.csv')

# Open and read csv 
with open (pollcsv,newline='') as csvfile:
    poll_csvreader = csv.reader(csvfile,delimiter=',')
    # read header
    poll_header =next(csvfile)

    cnt = 0
    candidate_list =[]

    # Read through content of the csvreader
    for row in poll_csvreader:
        cnt += 1
        candidate_list.append(row[2])

# To get unique candidate name list, create a unique name list(empty) and a counter list(empty)
unique_list = [] 
can_count = []

for i in candidate_list:
    # check if exists in unique_list or not 
    if i not in unique_list: 
        unique_list.append(i)
        can_count.append(0)

for m in unique_list:
    for n in candidate_list:
        if m==n:
            can_count[unique_list.index(m)] +=1

#print(unique_list)
#print(can_count)

# Print poll statistics to terminal
print(f"Election Results"
  f"\n-------------------------"
  f"\nTotal Votes: {cnt}\n-------------------------")

for x in range(len(unique_list)):
    print(f"{unique_list[x]}: {can_count[x]/cnt:.3%} ({can_count[x]})")

print(f"-------------------------"
  f"\nWinner: {unique_list[can_count.index(max(can_count))]}\n-------------------------")


# File path for output
filepath = os.path.join('','','new.txt')

with open(filepath,'w+') as fileout:
  fileout.write(f"Election Results"
  f"\n-------------------------"
  f"\nTotal Votes: {cnt}\n-------------------------")
  for x in range(len(unique_list)):
    line = f"\n{unique_list[x]}: {can_count[x]/cnt:.3%} ({can_count[x]})"
    fileout.write(line)
  fileout.write(f"\n-------------------------"
  f"\nWinner: {unique_list[can_count.index(max(can_count))]}\n-------------------------")