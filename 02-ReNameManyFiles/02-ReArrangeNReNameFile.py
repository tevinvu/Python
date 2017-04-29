#!/usr/bin/python3

import os
#find out where the folder contain the files you need to use this scripts to automate parsing and rename all of the files
#On command line: use cd to get into the folder you want to rename multiple files
# Type pwd to find out where you at and put into the () below
os.chdir('/Users/tevinvu/Desktop/testTxtBefore')
#to print the directory you are in to check it is the right one or not
print(os.getcwd())


for f in os.listdir(os.getcwd()):
       #print out the list of files
       #print(f) 
       #print(os.path.splitext(f))
       #here how you split the name and the extension of the files
       file_name, file_ext = os.path.splitext(f)

       #print(file_name)
       #print(file_name.split('-'))
       #split 3 parts of the tuples and assign to 3 variables 
       f_title, f_singerName, f_num = file_name.split('-')
       #get rid of all the space things
       f_title = f_title.strip()
       f_singerName = f_singerName.strip()
       f_num = f_num.strip()[1:].zfill(2)


       new_name = ('{}-{}-{}{}'.format(f_num, f_singerName,f_title,file_ext))
       #rename everything
       os.rename(f, new_name)
