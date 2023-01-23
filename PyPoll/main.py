#!/usr/bin/env python
# coding: utf-8

# In[108]:


import os
import pandas as pd


# In[109]:



#files to load

file_in = os.path.join(".", "Resources", "election_data.csv")

df_election = pd.read_csv(file_in)


# In[110]:


winning_candidate = df_election[candidate_column].mode()[0]
print(winning_candidate)


# In[111]:


#Display Results in Terminal

final_outputs = (
    f"Election Results\n\n"
    f"--------------------------\n\n"
    
    f"Total Votes: {total_votes}\n\n"
    f"--------------------------\n")

print(final_outputs)
for value, percentage in value_counts_percent.items():
    count = value_counts[value]
    print(f"{value}: {percentage:.3f}% ({count})\n ")
    
print(f"--------------------------\n")
print (f"Winner: {winning_candidate}\n")
print(f"--------------------------\n\n")


# In[106]:


#Send data to txt file:

with open('poll_analysis.txt', 'w') as f:
    print(final_outputs, file=f)
    #print(final_outputs)
    for value, percentage in value_counts_percent.items():
        count = value_counts[value]
        #print(f"Value: {value}, Count: {count}, Percentage: {percentage:.2f}%")
        print(f"{value}: {percentage:.3f}% ({count})\n ", file=f)
    print(f"--------------------------\n", file=f)
    print (f"Winner: {winning_candidate}\n", file=f)
    print(f"--------------------------\n\n", file=f)
   


# In[ ]:




