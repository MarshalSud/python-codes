# import sys
# s1 = "Hello How are you"
# print(id(s1))
# print(s1[0])
# print(s1[-9])

# length = len(s1)
# print (length)

# for i in s1:
#     print(i)

# for i in  range (len(s1)):
#     print(s1[i])

# let us learn now string indexing and slicing 

# print (s1[: :-1])

# s2 = s1 
# s3 = s1 [: :]
# print (id(s2))
# print (id(s1))
# print (id(s3))

# result = ' z'in s1
# print(result)

# class = we gruop the data and related operations on the data together and that's basically is the class 
# find and index 

# s1 = "Hello How are you"
# index = s1.find('H')
# rindex = s1.rfind("H")
# a = s1.index('h')
# print(index)
# print(a)
# print(rindex)

#alignement and padding

# s1 = "Hello"
# new = s1.ljust(10,"&")
# print(new)
# rnew = s1.rjust(10,"&")
# print(rnew)
# cnew = s1.center(11,"*")
# print(cnew)

# strip methods
# s1 = "000www00Hello6666"
# # new = s1.lstrip('0w')
# new = s1.strip('0w6')
# print(new)

# split and join methods 

# s1 = 'ss156831gmail@gmail.com'
# s2 = s1.replace('gmail','outlook',1)
# print(s2)

# a1 ='Marshal'
# a2 =" "
# a3 = a2.join(a1)
# print(a3)

# q1 = 'my name is sudarshan and i like dancing'
# q2 = q1.split(' ',2)
# print(q2)

# prefix and suffix and partition

# s1 = 'ss156831@gmail.com'
# result = s1.startswith('ss',2)
# print(result)
# result2 = s1.endswith('gmail.com',2)
# print(result2)
# final_result = s1.partition('@')
# print(final_result)

# case conversion 
s1 = 'hello Sud'
# s2 = s1.capitalize()
s2 = s1.upper()
print(s2)
s3 = s2.lower()
print(s3)





