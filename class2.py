# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:29:11 2019

@author: RSingh78
"""

##-functions---------
#
#in python... functions block starts with keyword def
#def add(firs,second):
#    total=first+second
#    return total
#
#gettotal=add(10,20)
#print(gettotal)

def display(*data):
    print(data)
    for item in data:
        print(item)

display(10,20,["java",20,"python"],40,50,60,70,80,90,"l")


# File Handling
#-------------------------------------
#working with flat files
#
#how to open file in python
#
#obj=open(filename,mode)
#
#example:
#    fobj=open("customer.txt","r") ---read mode
#    fobj=open("customer.txt","w") ---write mode
#    fobj=open("customer.txt","a") ---append mode
#
#r--readmode
#
#case1 : if file doesnot exist it displays error message
#case2 : if file exists ..it displays the file contents
#
#--write mode
#if file is not available , it creates the file and write the data
#if file exists it overwrites the data    
#
#---append mode
#case 1: if file doesnot exits create and writes the data
#case 2:  if exists appends the data

fobj=open("demo.txt","w")
fobj.write("python programming\n")
fobj.write("Ruby programming\n")
fobj.close()
fobj=open("demo.txt","r")
content=fobj.read()
print(content)
fobj.close()

#program 1:
#write a program to capture any string from keyboard and write the output to the file.

name=input("enter your content")
fobj=open("name.txt","w")
fobj.write(name)
fobj.close()
fobj=open("name.txt","r")
content=fobj.read()
print(content)
fobj.close()

#program 2:
#write a program to write all the odd numbers from 700 to 400 to the file and the
#file name should be with today's timestamp.
#Eg: 27_Feb_2019.txt

# ----------------file operation operation
#
#reading line by line
#
#reading the whole file at a time(fobj.readlines() fobj.read())

#--read line by line

fobj=open("demo.txt","r")
for line in fobj:
    #remove whitespace at the end of each line
    line=line.strip()
    #split the line with, as the delimeter
    data=line.split(" ")
    #display 1st field
    print(data[0])
fobj.close()

#***************************************************************************

# write a program to display to count female and male employees

i=0
k=0
fobj=open("employees.csv","r")
for line in fobj:
  if "Male" in line:
      i=i+1
  elif "Female" in line:
      k=k+1
print(i)
print(k)
fobj.close()

#*************************************************************************

# write a program to display the lines where salary > 100000

fobj=open("employees.csv","r")
#context manager
# with open("employees.csv","r") as fobj:

line=fobj.readline()
for line in fobj:
    a=line.split(",")
    k=int(a[4])
    if(k>100000):
        print(k)
fobj.close()    


#**************************************************
# print from line 4 to 10

with open("employees.csv","r") as fobj:
    data=fobj.readlines()
for line in data[4:10]:
    print(line)
    
#**************************************************

# Libraraies ########################################
#
#builtin : are installed with python
#path: c:\anaconda3\lib
    # math, os,sys,time,copy,calendar,datetime,loggin,shutil,json,unitest,pytest,xml,email,sqlite3
#
#third part library : based on requirement developer has to install the third party lib
#path: c:\anaconda3\lib\sit-packages
#    all the third party library are availabe in pypi.org


import math as m
print (m.ceil(4.9))
print(m.tan(3))
print(m.floor(3.99))

###########

from math import ceil,log
print(ceil(4.9))
print(log(3))

import os
print (os.listdir("c:\\"))

# write a program to display only .csv file

import os
for file in os.listdir():
    if os.path.isfile(file):
        b=list(file.split('.'))
        if (b[1] == 'py'):
            print (file)
            getsize=os.path.getsize(file)
            print (getsize)
#************************************************#
import os
for files in os.walk("."):  
    for filename in files:
        print(filename)

#***************************************************











    