#Import OS AND CSV
import os
import csv

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname,'Resources','election_data.csv')

#Starting the Loop with Zero
results = {}
totalvotes = 0

#OPEN CSV
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    #HEADER - SKIP
    csv_header = next(reader)
    #Loop - Row
    for row in reader:
        totalvotes = totalvotes + 1
        #Dictionary
        if results.get(row[2]) == None:
            counter = 1
            results[row[2]] = counter
        else:
            counter = results[row[2]] + 1
            results[row[2]] = counter            
#PATH FOR TXT FILE
txtpath = os.path.join(dirname,'Analysis','Results.txt')
#READ AND WRITE IN TXT FILE + OVERWRITE IF NEEDED
File = open(txtpath,"w+")
#PRINT IN TXT FILE
print("Election Results\n-----------------", file = File)
print(f"Total Votes: {totalvotes}\n-----------------", file = File)

#PRINT RESULTS
for candidate in results:
    print(f"{candidate}: {(results[candidate]/totalvotes*100): .3f}% ({results[candidate]})", file = File)

#MAX VOTE COUNT
winner = max(results, key=results.get)

print(f"-----------------\nWinner: {winner}\n-----------------", file = File)
#PRINT IN COMMAND LINE/GIT BASH/VS CODE
File.seek(0)
print(File.read())
