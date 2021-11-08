import csv
import os
# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

# open results
file_to_load = os.path.join('Resources/election_results.csv', 'r')
# Open the election results and read the file
with open('Resources/election_results.csv', 'r') as election_data:

     # To do: perform analysis.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.RFT")
# Using the with statement open the file as a text file.
outfile = open("analysis", "election_analysis.RFT", "w")
# Using the open() function with the "w" mode we will write data to the file.
open("analysis", "election_analysis.RFT", "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()

# To do: perform analysis.

# Close the file.


# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. Percent voates each candidate won.
#4. Total number of votes each candidate won
# 5. Winner of election

election_data.close()