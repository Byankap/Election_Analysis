import os

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Resources","analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties of the Election\n______________________")
    txt_file.write("\nArapahoe\nDenver\nJefferson")

# Close the file
txt_file.close()