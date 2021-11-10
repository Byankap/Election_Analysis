# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Resources","analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
candidate_options = []
candidate_votes = {}
# Open the election results and read the file.
with open(file_to_load) as election_data:
# To do: read and analyze the data here.
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
# Print the header row.
     headers = next(file_reader)
   # # Print each row in the CSV file.
     for row in file_reader:
          #add total vote count
          total_votes += 1
          #print candidate name from each row
          candidate_name = row[2]
          # If the candidate does not match any existing candidate...
          if candidate_name not in candidate_options:
            # Add it to the list of candidates.
               candidate_options.append(candidate_name)
                # 2. Begin tracking that candidate's vote count
               # Begin tracking that candidate's vote count.
               candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
          candidate_votes[candidate_name] += 1
     # Determine the percentage of votes for each candidate by looping through the counts.
     for candidate_name in candidate_votes:
          #retrieve vote count of candidate
          votes = candidate_votes[candidate_name]
          #percent of votes
          vote_percentage = float(votes) / float(total_votes) * 100
          print(f'{candidate_name}: received {vote_percentage}% of the vote.')
print(total_votes)
print(candidate_options)
print(candidate_votes)
# # Close the file.
election_data.close()

#2. A complete list of candidates who received votes

#3. Percent voates each candidate won.
#4. Total number of votes each candidate won
# 5. Winner of election

election_data.close()