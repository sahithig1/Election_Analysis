import csv
import os
# declaring a variable to store the data set
file_to_read = 'election_results.csv'
with open('election_results.csv') as election_data:
    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)
# Print each row in the CSV file.
    # for row in file_reader:
   #  print(row)
# Read and print the header row.
    headers = next(file_reader)
    print(headers)


file_to_write = 'Election_Final_Result.txt'
output = open(file_to_write, 'w')
output.write("Counties in the Election\n--------------\nArapahoe\nDenver\nJefferson")



