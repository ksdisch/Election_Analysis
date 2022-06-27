# Colorado Congressional Election Analysis

## Project Overview

### Purpose
A Colorado Board of Elections employee gave me the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

### Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.68.1

## Election Audit Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates receiving votes were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
    Diana DeGette, who received 73.8% of the vote and 272,892 votes.
    
## Election Audit Summary
This script has value beyond this particular election audit because of its versatility. That versatility comes from the fact that this script is not just counting votes, but it also finds the information that it is counting votes for. In this situation it was able to determine the candidates who received votes and the counties that the votes were coming from. This ability allows the script to be used effectively for other elections with a few simple modifications.

### Ballot Proposals, Ballot Initiatives, Veto Referendums
One example where the script could easily be modified are these situations where citizens are voting yes/no on and whichever option wins the popular vote. I would simply replace the portion of the script that determines candidates receiving votes with options for yes and no. Then, I would adjust the rest of the script accordingly for yes and no options. Now, the script would be able to count the votes for each option, calculate each option's percentage of the votes, and do the same for the counties that those votes came from and generate a report of the results. 

### Presidential Elections
Using this script to determine Colorado's results for presidential elections would require little to no modifications. The script would be able to determine the candidates that received votes, calculate each candidate's percentage of the votes, and do the same for the counties that those votes came from and generate a report of the results. With the extent of the media coverage on the day of presidential elections, the speed of the script would be valuable for quick and accurate reporting to the press.
