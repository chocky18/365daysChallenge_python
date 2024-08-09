'''
Write a Python program to calculate and print the average scores in Physics and Chemistry for each student given in the following dictionary:
data =
'Name': ['Tom', 'nick', 'Tom', 'jack', 'nick'],
'Physics': [20, 30, 80, 50, 40],
'Chemistry': [40, 70, 60, 50, 80]
}
'''


data ={
'Name': ['Tom', 'nick', 'Tom', 'jack', 'nick'],
'Physics': [20, 30, 80, 50, 40],
'Chemistry': [40, 70, 60, 50, 80]
}
avg_scores={}
for name, physics, chemistry in zip(data['Name'],data['Physics'],data['Chemistry']):
    if name in avg_scores:
        avg_scores[name]['physics'].append(physics)
        avg_scores[name]['chemistry'].append(chemistry)
    else:
        avg_scores[name]={'physics':[physics],'chemistry':[chemistry]}
# print(avg_scores)

for name, scores in avg_scores.items():
    # print( scores)
    phy_avg = sum(scores['physics'])/len(scores['physics'])
    chem_avg =sum(scores['chemistry'])/len(scores['chemistry'])
    print(f"{name} got {phy_avg} avg in physics")
    print(f"{name} got {chem_avg} avg in chemisty")