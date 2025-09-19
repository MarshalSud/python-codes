s1 = {1,2,3,5,3,6,7,7,8,4,5}
# print(s1[1]) => this is not possible because indexing and slicing are not possible in set so the objects are not subscriptable
s2 = set(range(1,11))
print(s2)
t1 = ()
# s3 = {1} 
s3 = set()
print(type(s3))
s4 = set('python')
print(s4)
for x in s1:
    print(x)
s1.update((10,20,30))
s1.update(('ruby'))
s1.add((10,20,30))
print(s1)