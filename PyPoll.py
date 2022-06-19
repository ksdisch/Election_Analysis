# Add our dependencies
import csv
import os
# The data we need to retrieve

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Initialize a list of candidates
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    
    # Read the file object with the reader function. 
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Add candidates to candidate_options list
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

# 3. Print the total votes.
print(total_votes)

# Print the list of candidates
print(candidate_options)

# initialize a list of dictionaries to count/store voting data for each candidate
voting_data = []
# initialize and append a dictionary for each candidate to voting data list
for candidate in candidate_options:
    candidate_dict = {
        "candidate": candidate, 
        "candidate votes": 0, 
        "percentage of votes": 0}
    voting_data.append(candidate_dict)
    

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    
    # Read the file object with the reader function. 
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    for row in file_reader:
        candidate_name = row[2]
        for item in voting_data:
            if item["candidate"] == candidate_name:
                # add to that candidates vote total
                item["candidate votes"] += 1


# initialize a list of vote totals to find maximum number
vote_totals = []

for entry in voting_data:
    #calculate percentage of votes for each candidate
    entry["percentage of votes"] = (entry["candidate votes"] / total_votes) * 100
    # append each candidates vote totals to list of vote totals
    vote_totals.append(entry["candidate votes"])
#use max function to create variable for winning vote total
winning_vote_count = max(vote_totals)

for entry in voting_data:
    # match the winning vote total to the candidate to identify the winner
    if entry["candidate votes"] == winning_vote_count:
        election_winner = entry["candidate"]
        winning_percentage = entry["percentage of votes"]

for entry in voting_data:
    print(f"{entry['candidate']}: {entry['percentage of votes']:.1f}% ({entry['candidate votes']:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {election_winner}\n"
    f"Winning Vote Count: {winning_vote_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


# 1. The total number of votes cast



# 2. A complete list of candidates who received votes



# 3. The percentage of votes each candidate won



# 4. The total number of votes each candidate won




# 5. The winner of the election based on popular vote