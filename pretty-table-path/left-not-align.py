import os
from prettytable import PrettyTable

# Get PATH environment variable and split by semicolon
path_entries = os.environ["PATH"].split(";")

# Create PrettyTable
table = PrettyTable()
table.field_names = ["Index", "Path Entry"]

# Populate table with zero-padded index
for index, path in enumerate(path_entries, start=1):
    table.add_row([f"{index:03}", path])

# Print the table
print(table)