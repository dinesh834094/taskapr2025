set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3=set1.intersection(set2)
print(set3)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.union(set2)
print(set3)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.difference(set2)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3= set1.symmetric_difference(set2)
print(set3)

my_set = {1, 2, 3, 4, 5}
if 3 in my_set:
    print('true')
else:
    print('false')



