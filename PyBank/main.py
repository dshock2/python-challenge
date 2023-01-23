# import libriaries
import os
import pandas as pd

# files to load

file_in = os.path.join(".", "Resources", "budget_data.csv")

# Put in dataframe and figure out total months pt1
df_budget = pd.read_csv(file_in)

# Put in dataframe and figure out Financial sheet
column_date = 'Date'
total_months = df_budget[column_date].count()

# Sum of Profit/Loss column
column_profit_loss = 'Profit/Losses'
total_sum = df_budget[column_profit_loss].sum()

# Avg Change
avg_change = df_budget[column_profit_loss].diff().mean()

# Greatest Increase
greatest_increase = df_budget[column_profit_loss].diff().max()
greatest_increase_match = df_budget[column_profit_loss].diff().idxmax()
match_increase_date = df_budget.loc[greatest_increase_match, column_date]

# Greatest Decrease
greatest_decrease = df_budget[column_profit_loss].diff().min()
greatest_decrease_match = df_budget[column_profit_loss].diff().idxmin()
match_decrease_date = df_budget.loc[greatest_decrease_match, column_date]

final_outputs = (
    f"Financial Analysis\n"
    f"--------------------------\n"

    f"Total Months: {total_months}\n"
    f"Total:  ${total_sum}\n"
    f"Average Change:  ${avg_change: .2f}\n"
    f"Greates Increase in Profits:  {match_increase_date}  (${greatest_increase: .0f})\n"
    f"Greates Decrease in Profits: {match_decrease_date} (${greatest_decrease: .0f})\n"

)

# Print Final Output to Screen:

print(final_outputs)

Financial
Analysis
--------------------------
Total
Months: 86
Total:  $22564198
Average
Change:  $-8311.11
Greates
Increase in Profits: Aug - 16($ 1862002)
Greates
Decrease in Profits: Feb - 14($-1825558)

# Send data to txt file:

with open('budget_analysis.txt', 'w') as f:
    print(final_outputs, file=f)


