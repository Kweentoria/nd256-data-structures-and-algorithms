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
    # print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls[0][0], calls[0][1], calls[0][2], calls[0][3]) )

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
#receiving number (1)

def longestDuration(calls):
    unique_num_with_duration = {}

    for call in calls:
        caller_number = call[0]
        receiver_number = call[1]
        duration = int(call[3])
        #caller
        if caller_number in unique_num_with_duration:
            unique_num_with_duration[caller_number] += duration
        else:
            unique_num_with_duration[caller_number] = duration
        #receiver
        if receiver_number in unique_num_with_duration:
            unique_num_with_duration[receiver_number] += duration
        else:
            unique_num_with_duration[receiver_number] = duration

    longest_time = 0
    phone = ''

    for key, value in unique_num_with_duration.items():
        if value > longest_time:
            longest_time = value
            phone = key
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone, longest_time))

longestDuration(calls)