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
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
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


#Part A
list_of_codes = set()
for call in calls:
  caller = call[0]
  receiver = call[1]
  if caller[:5] == '(080)' and receiver[:2] == '(0':
     list_of_codes.add(receiver[1:receiver.index(')')])
  elif caller[:5] == '(080)' and '(' not in receiver and ' ' in receiver and receiver[0] in '789':
     list_of_codes.add(receiver[:4])
  elif caller[:5] == '(080)' and receiver[:3] == '140':
     list_of_codes.add(receiver[:3])
# print('The numbers called by people in Bangalore have codes: {}'.format(sorted(list_of_codes)))   
print('The numbers called by people in Bangalore have codes:')
print('\n'.join(sorted(list_of_codes)))

#Part B
total_ban_callers_receivers = 0
total_ban_callers = 0
for call in calls:
  caller = call[0]
  receiver = call[1]
  if caller[:5] == '(080)' and receiver[:5] == '(080)':
    total_ban_callers_receivers += 1
  
  if caller[:5] == '(080)':
    total_ban_callers += 1
perc = round((total_ban_callers_receivers/total_ban_callers)*100, 2)
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(perc))

