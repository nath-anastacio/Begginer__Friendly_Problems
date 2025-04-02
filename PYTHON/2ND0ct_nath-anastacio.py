#Binary Search Algorithm in Python

import time

def binary_search(list, start, end, item):
    """
    Perform Binary Search on a Sorted List

    Args:
        list: A sorted list of elements
        start: Starting index of the search range
        end: Ending index of the search range
        item: Element to search for

    Returns: 
        Index of the item if found, None otherwise
    """
    if start <= end:
        middle = (start + end)//2
        #If item is greater, search in the right half
        if item > list[middle]:
            return binary_search(list, middle+1, end, item)
        #If item is smaller, search in the left half
        elif item < list[middle]:
            return binary_search(list, start, middle-1, item)
        #Item found
        else:
            return middle
    #Item not found
    return None
        

#Get user input for list range
start_of_list= int(input('Enter the beginning of the list: '))
end_of_list = int(input('Enter the end of the list: '))
list1 = list(range(start_of_list, end_of_list))
print(f'list = {list1}')

#Get item to search for
item=int(input('Enter the number you want to find in the list: '))

#Measure execution time
time_before = time.time()
position = binary_search(list1, 0, len(list1)-1, item)
time_after = time.time()
time_spent = (time_after - time_before) * 1000

#Display results
if position == None:
    print(f'The item {item}, is not on the list')
else:
    print(f'The item {item} is in the position {position}')
    print(f'The total time spent was: {time_spent:.2f} ms')