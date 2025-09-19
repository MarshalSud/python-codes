# t1 = 1,2,3,4,5
# t2 = (1,2,3,4,5,6,7)
# t3 =()
# t4 =(1)
# t5 = 1,
# print (t1)
# print (t2)
# print (type(t3))
# print (type(t4))
# print (type(t5))

# print(t1[1])

# t6 = tuple ([1,2,3,4,5])
# print(t6)

# tuple comprehensions

T = (*(x**2 for x in [1,2,3,4,5,6,7,8,9,10] if x%2==0),)
T1 = tuple((x**2 for x in [1,2,3,4,5,6,7,8,9,10] if x%2==0))

print(T)
print(T1)

# indexinbg and slicing 

print(T[::-1])

# packing and unpacking of the tuple
y1= 1,2,3,4,5
s1 = 'hello'
a,b,*c = s1
print (a,b,c)
l1 = [1,2,3,4,5]
a,b,*c = l1
print (a,b,c)
# a,b,c,d,e = 1,2,3,4,5
*a,b,c = y1
print (a,b,c)