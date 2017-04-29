#!/user/bin/python3

import os

os.chdir('/Users/tevinvu/Desktop/testTxt')
#to print the directory you are in
print(os.getcwd())

#print out all the file in the directory
for f in os.listdir(os.getcwd()):
       #print(f)
       #print(os.path.splitext(f))
       file_name, file_ext = os.path.splitext(f)
       #print(file_name)
       #print(file_name.split('-'))
       f_title, f_singerName, f_num = file_name.split('-')
       f_title = f_title.strip()
       f_singerName = f_singerName.strip()
       f_num = f_num.strip()[1:].zfill(2)
       new_name = ('{}-{}-{}{}'.format(f_num, f_singerName,f_title,file_ext))

       os.rename(f, new_name)