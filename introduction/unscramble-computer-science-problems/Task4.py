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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.

"""
telemarketers = set()

phonecaller = set()
receiver_call = set()
receiver_text = set()
send_text = set()

for call in calls:
  caller = call[0]
  receiver = call[1]
  phonecaller.add(caller)
  receiver_call.add(receiver)

for text in texts:
    texter = text[0]
    receiver = text[1]
    send_text.add(texter)
    receiver_text.add(receiver)

non_telemarketers = receiver_call | receiver_text | send_text
for i in phonecaller:
    if i not in non_telemarketers:
        telemarketers.add(i)
        
print('These numbers could be telemarketers: {}'.format(sorted(telemarketers)))