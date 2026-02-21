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

# def unique_records(texts, calls):
#     checklist = set()
#     for text in texts:
#         checklist.add(text[0])
#         checklist.add(text[1])
        
#     for call in calls:
#         checklist.add(call[0])
#         checklist.add(call[1])
           
#     print("There are {} different telephone numbers in the records.".format(len(checklist)))


def unique_records(texts, calls):
    unique_numbers = {}
    for text in texts:
        unique_numbers[text[0]] = True
        unique_numbers[text[1]] = True
        
    for call in calls:
        unique_numbers[call[0]] = True
        unique_numbers[call[1]] = True
    counter = 0      
    for i in unique_numbers:
        counter += 1
    print("There are {} different telephone numbers in the records.".format(counter))
unique_records(texts, calls)



# def uniqueRecords(texts, calls):
#     """
#     This checks the phone numbers in texts and calls and stores the unique numbers in a list, 
#     then counts the unique records
#     """
#     checklist = []
#     def checkUnique(phone_number):
#         """
#         Checks if phone number previosuly exist in the list
#         """    
#         number_exists = False
#         for item in checklist:
#             if phone_number == item:
#                 number_exists = True
#                 break
#         if not number_exists:
#             checklist.append(phone_number)


#     for phone_number in texts:
#         checkUnique(phone_number[0])
#         checkUnique(phone_number[1])

#     for phone_number in calls:
#         checkUnique(phone_number[0])
#         checkUnique(phone_number[1])
#     counter = 0
#     for i in checklist:
#         counter += 1
#     print("There are {} different telephone numbers in the records.".format(counter))

# uniqueRecords(texts, calls)