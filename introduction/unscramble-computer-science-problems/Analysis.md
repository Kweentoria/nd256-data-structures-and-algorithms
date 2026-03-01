## Task0

**Description**: The problem involves printing the first record of texts and the last record of calls.

**Approach**: Selected the first row in texts using index 0 and the last row in calls using index -1

**Complexity Analysis**:
- **Algorithm**: No loop runs.
- **Big O Notation**: $O(1)$ where $1$ is constant.
- **Justification**: The complexity of the algorithm is not determined by the value of the inputs, rather by the index of the element.

## Task1

**Description**: The problem involves calculating the number of unique telephone numbers in the call and text records.

**Approach**: Iterated through both arrays, adding each number to an empty set. Counting the length of unique items in the set.

**Complexity Analysis**:
- **Algorithm**: A single loop runs through each element of the array once, and this is done for call and text records separately.
- **Big O Notation**: $O(n)$ and $O(m)$ where $n$ and $m$ are the number of elements in the call and text records respectively, resulting in $O(n + m)$.
- **Justification**: Each element is accessed once; hence, the time complexity is directly proportional to the array size.

## Task2
**Description**: The problem involves calculating the max total time spent on the phone from one number.

**Approach**: Iterated through the calls array twice; once to build the duration dictionary, and once to find the maximum.

**Complexity Analysis**:
- **Algorithm**: Two sequential loops, one through calls to build the duration dictionary and the other to find the phone number with max duration.
- **Big O Notation**: $O(n)$ where $n$ is the number of elements in the calls record.
- **Justification**: Each element is accessed once; hence, the time complexity is directly proportional to the array size.

## Task3
**Description**: The problem involves finding all of the area codes and mobile prefixes called by people in Bangalore, and percentage of calls from fixed lines in Bangalore that are made to fixed lines also in Bangalore

**Approach A**: Iterated through the records a single time, using if/else to find the area codes and adding it to an empty set.

**Approach B**: Iterated through the records a single time, counting the number of total calls made from bangalore and the total number of fixed lines calls from bangalore, then divide to get the percentage.

**Complexity Analysis**:
- **Algorithm**: A single loop runs through each element of the array once.
- **Big O Notation**: $O(n)$ where $n$ is the number of elements in the array.
- **Justification**: Each element is accessed once; hence, the time complexity is directly proportional to the array size.

## Task4

**Description**: The problem involves finding all telemarketers from the call and text records. Telemarketers only make calls and never receive calls, receive texts, or send texts.

**Approach**: Iterated through calls and texts separately, building sets of callers, receivers, and texters. Computed the union of non-telemarketers and filtered out any phone caller that appeared in the union.

**Complexity Analysis**:
- **Algorithm**: Three sequential loops run through calls, texts, and phonecallers respectively. A set union is computed once before the final loop.
- **Big O Notation**: $O(n + m)$ where $n$ is the number of calls and $m$ is the number of texts.
- **Justification**: Each element is accessed once across the loops, and set operations (add, union, lookup) are $O(1)$ on average; hence, the time complexity is directly proportional to the input sizes.
