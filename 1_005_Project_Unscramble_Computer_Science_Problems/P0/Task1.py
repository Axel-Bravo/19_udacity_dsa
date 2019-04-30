"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

if __name__ == '__main__':
    tel_numbers = []
    g = globals()
    for file in ['texts', 'calls']:
        for column in [0, 1]:
            temp_numbers = [data[column] for data in g[file]]
            tel_numbers += temp_numbers

    tel_numbers = set(tel_numbers)

    print("There are {} different telephone numbers in the records.".format(len(tel_numbers)))
