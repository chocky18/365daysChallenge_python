'''
Write a python program using decorator to reorder the sequence of unorder number
in ascending format [8,6,3,6,9,1,0,44,5,23,7,123,6,1,0] (Brute force algorithm).

'''

unsorted_list = [8,6,3,6,9,1,0,44,5,23,7,123,6,1,0]
n = len(unsorted_list)
for i in range(n):
    for j in range(0,n-i-1):
        if unsorted_list[j]> unsorted_list[j+1]:
            unsorted_list[j],unsorted_list[j+1] = unsorted_list[j+1],unsorted_list[j]
print(unsorted_list)
sortedset = set(unsorted_list)
print(list(sortedset))