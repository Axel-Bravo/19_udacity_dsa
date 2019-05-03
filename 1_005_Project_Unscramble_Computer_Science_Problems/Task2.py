"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

if __name__ == '__main__':
    telephone_time = dict()
    for call in calls:
        for call_element in [0, 1]:
            if call[call_element] in telephone_time:  # Telephone already in our dictionary
                telephone_time[call[call_element]] += int(call[3])
            else:  # Telephone not in our dictionary
                telephone_time[call[call_element]] = int(call[3])

    max_call_time = 0
    max_telephone_num = ''

    for telephone in telephone_time:
        if telephone_time[telephone] >= max_call_time:
            max_call_time = telephone_time[telephone]
            max_telephone_num = telephone

    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
        max_telephone_num, max_call_time))
