# one =1 
# two =2 
# three = 3 
# four = 4 
# five = 5 
# six = 6

# d1 = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6}

# # d1 = {'one':'1','two':'2','three':'3','four':4,'five':'5','six':'6'}
# d1['four'] = 7
# d1['seven'] = 7
# print(d1['four'])
# print(d1)

# now let us learn about dict traversing
# d1 = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6}

# for i in d1:
#     print(i,d1[i])

# L1 = [1,2,3,4,5]
# L2 =['one','two','three','four']
# d1= dict(zip(L1,L2))
# print(d1)

# # this is only useful for keys when you want them in the integer format if you want them in different format then you should not use ths enumerate function 
# L3 = ['one','two','three','four','five']
# d2 = dict(enumerate(L3,start=10))
# print(d2)

# dictionary comprehensions
# d1 = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6}
# R1 = [(1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five')]
# dict_2 = dict (R1)
# print(dict_2)
# dict_1 = {x:y for x,y in R1}
# dict_12 = {x for x in R1}
# dict_3 = {x:y for x,y in zip(L1,L2)}
# print(dict_12)
# print(type(dict_12))
# print(dict_3)

d1 = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6}
# for x in d1.keys():
#     print(d1[x])
#     print(x)

for key,value in d1.items():
    print(key,value)

print(d1.get('ten','missing mf'))
print(d1('ten'))
