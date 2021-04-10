#Import OS AND CSV
import os
import csv

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname,'Resources','budget_data.csv')

#Starting the Loop with Zero
Total_Months = 0
Net = 0
Max_Change = 0
Max_Date = ""
Min_Change = 0
Min_Date = ""
Change = 0
Total_Change = 0  
Total = 0  

#Open CSV
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    #HEADER - SKIP
    csv_header = next(reader)
    #Loop - Row
    for row in reader:
        if Total_Months == 0:
            Total_Months = Total_Months + 1
            Total = Total + int(row[1])
            Net = int(row[1])
        else:
            Total_Months = Total_Months + 1
            Total = Total + int(row[1])
            Change = int(row[1]) - Net
            Net = int(row[1])
            Total_Change = Total_Change + Change
            #MAX CHANGE AND MIN CHANGE (REF - VBA) 
            if Change > Max_Change:
                Max_Change = Change
                Max_Date = row[0]   
            elif Change < Min_Change:
                Min_Change = Change
                Min_Date = row[0]       
#PATH FOR TXT FILE
txtpath = os.path.join(dirname,'analysis','fin_analysis.txt')
#READ AND WRITE IN TXT FILE + OVERWRITE IF NEEDED
File = open(txtpath,"w+")
#PRINT RESULTS
print(f"Fin Analysis\n------\nTotal Months: {Total_Months}\nTotal: ${Total}\nAverage Change: ${Total_Change/(Total_Months-1):.2f}\nGreatest Increase in Profits: {Max_Date} (${Max_Change})\nGreatest Decrease in Profits: {Min_Date} (${Min_Change})", file = File)
#PRINT IN COMMAND LINE/GIT BASH/VS CODE
File.seek(0)
print(File.read())
