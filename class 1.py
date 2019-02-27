# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

name = "hello People, i am ratan"
print(name[-2:-8:-1])

first ="python"
second ="anaconda"
join = first + second
print(join)

alist = [10,10,30,40]
blist =  ["unix","scala","spark","hadoop"]
#clist = [10,20,"unix,"scala",4000,56.44]

print(alist[0])
print(alist[1])
print(alist[0:3])
print(alist[-1])
alist[0] = 100
print("updated list:", alist)

final = alist + blist
print(final)

atup = (10,20,30)
btup = ("perl","java","hadoop","spark")
print(atup)
print(btup[0:4])
# atup[0] = 10000 elements inside tuple cannot be modified 
print("updated tuple : ", atup)

# dictname = {key:value, key:value, key:value } #keys are always unique
#dictionary keys are always unique

book = {"chap1":10,"chap2":20}
print(book["chap1"])


alist=[[10,20],[30,40],[40,50]]
print(alist)
print(alist[0][0])

# set is group of elements
#set elements are defined in {}
# indexing is not permitted for set

aset = {10,20,30,40,50}
print(aset)

#list to set conversion
alist=[10,20,30,40,10,20]

print(set(alist))

#display output in tuple format

print(tuple(alist))
final=tuple(alist)
print("output is", final)


# everything in python is object
# every object contains set of methods

name= "python"
print(name.upper())
print(name.replace('python','puneet'))
print(name.isalpha())
print(name.isalnum())

alist=[10,20,30,40]
print(alist.count(20))

# dir(__builtins__) # list of all predefined functions
getindex=alist.index(20)
print(getindex)
alist.reverse()
print(alist)
alist.pop(1)
print(alist)

print(book.values())
print(book.keys())
print(book.items())

# two functions -- builtin and user defined

name= input("enter any name:")
print(name)

#sum of two numbers

first = int(input("enter first value:"))
second = int(input("enter second number:"))

total=first + second
print(total)




