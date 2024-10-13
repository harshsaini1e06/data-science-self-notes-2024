import os
# print (os.getcwd()) # to get the in which we are present
# print (os.listdir(r"C:\mingw32")) # to reach or get the folders and files present in the given path

# os.mkdir("jecrc") # to make the new folder

# os.makedirs("jason" , exist_ok=True) # here "exist_ok" is used to clear the error which is occured dure to again running this line 
# path_1 = r"C:\Users\91992\OneDrive\Desktop\New folder\jason"
# os.chdir(path_1)
# print (os.getcwd())
open('mee.txt','x')

file = open('mee.txt','w')
data = "hello i am here"
file.write(data)
file = open ('mee.txt','w')
data2 = "hey"
file.write(data2)
file = open ('me.txt','r')