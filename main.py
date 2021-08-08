# PyBank
#=============================================================================

import os
import csv

#Seting my csv path for import
csvpath = os.path.join("Resources", "budget_data.csv" )

#creating a path for exporting the final data text file
analysis_output = os.path.join("Analysis", "budget_analysis.txt")

#Establishing variables to track months, net total Profit/Losses
#Changes in Month, Profits/Losses, Greatest Increase and Decrease

totalMonths = 0
prev_pnl = 0
chgMonth =[]
pnl_chg_lst = []
grt_incr = ["", 0]
grt_decr = ["", 9999999999999999999] #float
pnl_tot = 0


with open(csvpath) as pnl_data:
    csvreader = csv.DictReader(pnl_data)

    for row in csvreader:

        #Tracking total
        totalMonths = totalMonths + 1
        pnl_tot = pnl_tot + int(row["Profit/Losses"])

        #Formula for Profit/loss change
        pnl_chg = int(row["Profit/Losses"]) - prev_pnl
        prev_pnl = int(row["Profit/Losses"])
        pnl_chg_lst = pnl_chg_lst + [pnl_chg]
        chgMonth = chgMonth + [row["Date"]]

        #Formulate if statement for "Greatest Increase
        if (pnl_chg > grt_incr[1]):
            grt_incr[0] = row["Date"]
            grt_incr[1] = pnl_chg

        #Formulate  if statement for "Greatest Decrease"
        if (pnl_chg < grt_decr[1]):
            grt_decr[0] = row["Date"]
            grt_decr[1] = pnl_chg

 
#Figure out the Average Profit/Loss Change
avg_pnl = sum(pnl_chg_lst) / len(pnl_chg_lst)

#Create "Finacial Analysis" summary

output = (
    f"\nFinanical Analysis\n"
    f"================================\n"
    f"Total Months: {totalMonths}\n"
    f"Total: {pnl_tot}\n"
    f"Average Change:{avg_pnl}\n"
    f"Greatest Increase in Profits: {grt_incr[0]} (${grt_incr[1]})\n"
    f"Greatest Decrease in Profits: {grt_decr[0]} (${grt_decr[1]})\n"
)

#Print the output
print(output)

# Export output as text file
with open(analysis_output, "w") as txt_file:
    txt_file.write(output)








