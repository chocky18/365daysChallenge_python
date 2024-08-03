'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example
record = [["chi",20.0],["beta", 33.4],["sigma", 33.4],['alpha',50]]
The ordered list of scores is [20.0,33.4,50], so the second lowest score is 33.4 . There are two students with that score: ['sigma','beta']. Ordered alphabetically, the names are printed as:
'''

record = [["chi",50.0],["beta", 33.4],["sigma", 33.4],['alpha',20]]
values = [i[1] for i in record]
second_highest_value = sorted(values)[1]
# print(second_highest_value)
get_names = [names[0] for names in record if names[1]==second_highest_value]
print((get_names))