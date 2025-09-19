# let us create a list of the elements and let us learn the creation of the list 

# l1 = [1,2,3,4,5,6]
# l2 = []
# l3 = list('sudarshan')
# l4 = ['sudarshan']
# l5 = list ((1,2,3,4))
# print(l3)
# print(l4) 
# print(l5) 

# travwerse a string 

# l1 = [1,2,3,4,5,6]
# for i in l1:
#     print (i)

# l2 = [1,3.4,'love',[1,2,3],(1,2,3),True]
# print(l2)

# l1[1]=10
# print (l1)
# l1.append(23)
# print (l1)

# indexing and slicing for read and write 

# l1 = [1,2,3,4,5,6]
# if (l1[2]==l1[-4]):
#     print('alright this thing is matching')
#     print(l1[2],l1[-4])

# print(l1[1:4])

# l1[2] = 10
# print(l1) 

# for writing in list using slicing 

# l1 = [1,2,3,4,5]
# l1[0:0]=[2]
# print(l1)
# l1[1:4] = [6,7,8,9,10]
# print(l1)
# l1[4:1:-1]=[2,3,4]
# print(l1)
# l1[::2]=[11,11,11,11]
# print(l1)

# list concatenation

# l1 = [1,2,3,4,5,6,7,8,9,10]
# l2 = [11,12,13,14,15]
# l3=l2[:]
# l2.extend([100])
# print(l3)
# print(id(l2))
# print(id(l3))
# l2 = l2 + [4]
# print(id(l2))
# print(l2)

# l1.extend([11,12,13])
# print(l1)

# list travering 

# l1 = [10,11,12,13,14,15,16,17,18,19,20]

# for i in l1:
#     print(i)
# # for i in [1,2,3,4,5,6,7,8,9,10]:
# #     print(i)
# print('##########################')

# for i in range(len(l1)):
#     print(l1[i])

# print('##########################')
# i = 0 
# while (range(len(l1))):
#     print('shit')
    
# list methods 
# l2 = list(range(1,21))
# l4 = ['Sudarshan','Pandurang','all is well','best comes at the last','name of the game is money']
# l4.sort(key=str.lower,reverse=False)
# print(l4)
# # l2.remove(x)
# print(l2.index(20))
# print(l2.count(20))
# print(l2)
# print(id(l2))
# l3 = l2.copy()
# print(id(l3))
# l1 = [10,11,12,13,14,15,16,17,18,19,20]
# l1.append([100])
# print(l1)

# list comprehensions

l2 = list(range(1,21))
L = [x**2 for x in l2 if x%2== 0]
# here i am applying filter for even nos 
print(L) 

list = [list(range(1,4)),list(range(4,7)),list(range(7,10))]
print(list[0][0])