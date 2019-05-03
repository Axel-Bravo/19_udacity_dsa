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
    bangalore_id = '(080)'
    for interlocutor in [0, 1]:
        if bangalore_id in call[interlocutor]:
            return True, interlocutor
    return False, -1


def extract_area_code(call, call_bangalore_pos):
    call_other_interloc = call[1 - call_bangalore_pos]

    if call_other_interloc[0] == '(':  # Fix land case
        return call_other_interloc.split(sep=')')[0] + ')'

    if len(call_other_interloc.split(sep=' ')) > 1:  # Mobile case
        return call_other_interloc.split(sep=' ')[0]

    else:  # Telemarketer case
        return call_other_interloc[:3]


if __name__ == '__main__':
    bangalore_related_prefix = []
    # Part A
    for call in calls:
        is_bangalore_call, bangalore_interlocutor = bangalore_call(call)
        if is_bangalore_call:
            bangalore_related_prefix.append(extract_area_code(call, bangalore_interlocutor))

    bng_related_prefix = list(set(bangalore_related_prefix))
    bng_related_prefix.sort()

    print("The numbers called by people in Bangalore have codes: \n")
    for related_prefix in bng_related_prefix:
        print(related_prefix + "\n")

    # Part B
    bng_recurrent_call_num = 0
    for call_prefix in bangalore_related_prefix:
        if call_prefix == "(080)":
            bng_recurrent_call_num += 1

    print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
       round(bng_recurrent_call_num/len(bangalore_related_prefix), 2)))
