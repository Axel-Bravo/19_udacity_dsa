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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def bangalore_call(call):
    return call[0][0:5] == '(080)'


def extract_area_code(call):
    call_other_interloc = call[1]

    if call_other_interloc[:2] == '(0':  # Fix land case
        return call_other_interloc.split(sep=')')[0] + ')'

    if call_other_interloc[:3] == '140':  # Telemarketer case
        return call_other_interloc[:3]

    else:  # Mobile case
        return call_other_interloc[:4]


if __name__ == '__main__':
    bng_called_prefix = []
    # Part A
    for call in calls:
        if bangalore_call(call):
            bng_called_prefix.append(extract_area_code(call))

    bng_called_prefix_resum = list(set(bng_called_prefix))
    bng_called_prefix_resum.sort()

    print("\n The numbers called by people in Bangalore have codes:")
    for related_prefix in bng_called_prefix_resum:
        print(related_prefix)

    # Part B
    bng_recurrent_call_num = 0
    for call_prefix in bng_called_prefix:
        if call_prefix == "(080)":
            bng_recurrent_call_num += 1

    print("\n {} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
       round(bng_recurrent_call_num/len(bng_called_prefix)*100, 2)))
