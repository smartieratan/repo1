# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:44:46 2019

@author: RSingh78
"""

##Program 1 :  
#input a filename and print seperate file and extension
#enter any filename: data.csv
#filename : data
#extension : csv

name=input("Enter any filename:")
full=str(name)
sp=full.split('.',1)
alist=sp
print("filename", alist[0])
print("extension", alist[1])

##program 2: 
#write a program to capture type string and the output in terms of list
#enter any list : perl,unix,spark,scala
#list output : ['perl','unix','spark','scala']
#length of list : 4

string1= input("Enter your 1st list:")
string2= input("Enter your 1st list:")
string3= input("Enter your 1st list:")
string4= input("Enter your 1st list:")

alist=[string1,string2,string3,string4]
print("list output",alist)
k=len(alist)
print("length of list",k)

#Program 3:
#write a program to remove all the duplicates from the list
#alist=[ 10,20,10,20,30,40,50,20,30,40,60,70,80,10]
#output= [10,20,30,40,50,60,70,80]    

alist=[10,20,10,20,30,40,50,20,30,40,60,70,80,10]
blist=set(alist)
clist=list(blist)
clist.sort(reverse=True)
print(clist[::-1])

#Program 4:
#write a program to read anyfile ( employees.log ) and convert its extension to
#employees.csv
#Enter any filename : employees.log
#new file           : employees.csv

name=input("Enter any filename:")
full=str(name)
sp=full.split('.',1)
alist=sp
alist.pop(1)
alist.insert(1,'.csv')
j=str(alist[0])
k=str(alist[1])
l=j+k
print("newfile",l)

#program5
#name = "python is general purpose and python is interactive and python is cross 	platform language"
#-write a program to count all the occurences of python in the above string.
#-write a program to count all the no. of words in the above string.
#-convert the string to uppercase
#-replace python with spark and display the output

name="python is general purpose and python is interactive and python is cross 	platform language"
print(name.count('python'))
a=name.split()
k=list(a)
print(len(k))
print(name.upper())
print(name.replace('python','spark'))

#program6
#write a program to create some empty list and perform the below operations.
#1. append 100 to the list
#2. append 60 to the list
#3. append 30 to the list
#4. append 1000 to the list
#5. extend the list with 90,3543,53,43,42,534,10,10,10,20
#6. remove the element 3543.
#7. pop the element which is at index 5.
#8. find the element at the index 6
#9. count the no. of occurences of the value 10 and display it.

alist= []
alist.append(100)
alist.append(30)
alist.append(1000)
blist = [90,3,3543,53,43,42,534,10,10,10,20]
alist.extend(blist)
print(alist) 
alist.pop(5)
print(alist)
print(alist[6])
k=str(alist)
l=k.count('10')
print(l)

##program7
#write a program to verify the file extension
#if file endswith .py display "python file"
#if file endswith .txt displya "text file"
#if file endswith .csv  display "csv file"
#if file endswith .pl   display "perl file"
#if file endswith .ksh  display "korn shell file"
#Enter any fileenmae:  hello.py
#Input file is python file
#Enter any filename : hello.c
#input file is C source file

name=input("Enter any filename:")
full=str(name)
sp=full.split('.',1)
b=sp[1]
if b=='py':
    print("python file")
elif b=='txt':
    print("text file")
elif b=='csv':
    print("csv file")
elif b=='pl':
    print("perl file")
elif b=='ksh':
    print("korn shell file")    
else:
    print("cannot recognize")    
    
#program 8
#write a program to capture any name from keyboard and perform the below operation.
#if length of the string is less than 10 ... string is too small
#if length of the string is greater than 30 .. string is too big.    
#    
    
name=input("Enter the name:")
b=len(name)
if b < 10:
   print("string is too small")
elif b>30:
   print("string is too big")
else:
    print("perfect")    
    
#program9
#write a program to display all the list if IPs in the below format.
#192.168.0.1
#192.168.0.2
#192.168.0.3
#...
#..
#...
#...
#192.168.0.99
    
name="192.168.0.1"
a=name.split('.',3)
b=a[3]
    
for i in range(0,100,1):
    k=str(i)
    b=k
    g=a[0]+'.'+a[1]+'.'+a[2]+'.'+b
    print(g)
    

#program 10
#alist = ["google","unix","facebook","linkedin"]
#write a program to read the above list and add "http://www" at the beginning
#and append ".com" at the end of each element.
#http://www.google.com
#http://www.unix.com
#http://www.facebook.com
#http://www.linkedin.com
    
alist=["google","unix","facebook","linkedin"]

for i in range(0,3,1):
    k=str(alist[i])
    print("http://www."+k+".com")
    
#Write a program to check the validity of password input by user.
#Following are the criteria for checking the password:
#
#1. At least 1 character from [$#@]
#2. Minimum length of transaction password: 6
#3. Maximum length of transaction password: 12
#display "Valid password" if all the conditions are 
#satisfied or "Invalid password"    


 name=input("Enter the name:")
 a=list(name)
 if (len(a) >= 6) and (len(a)<=12):
     b=str(a)
     if('#'in b) or ('$' in b) or ('@' in b):
        print("valid password")
     else:
        print("invalid pass")
 else:
     print("invalid password")
     


     