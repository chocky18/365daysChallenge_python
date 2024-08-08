'''
Given the list lst = [1, 2, 3, 1, 4, 2, 3, 5, 6, 5],
 write a Python program to count the occurrences of each element in the list and print the results.

'''

lst = [1, 2, 3, 1, 4, 2, 3, 5, 6, 5]

count_dict ={}
for element in lst:
    if element in count_dict:
        count_dict[element] += 1
    else:
        count_dict[element] = 1
print((count_dict))
for element, occurance in count_dict.items():
    print(f"Element {element} occurred {occurance} times")




