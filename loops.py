# for i in range(1,11,1):
#     print (i)

# # list is also knwn as hetrogenous array as it can store multiple data type
# list = list(range(22))
# print (list) 

# l1= [10,20,30,40,50,60]
# for item in l1:
#     print (item)

# tuple = (1,2,3,4,5,6,7)
# for t in tuple:
#     print (t)

# company = "amazon"
# for char in company:
#     print (char)

# dt = {'name':'r','branch':'cse','roll_no.':21}
# print (dt.keys())
# for dit in dt.keys():
#     print (dit)

# list = [342,52,32,45,345,32,2,52,454,34,6,63,6,36,3,6]
# target = int(input('enter your target : '))
# for item in list:
#     if item == target:
#         print ('present')


# # it represents the total no. one by one
# list = [342,52,32,45,345,32,2,52,454,34,6,63,6,36,3,6]
# n = 0
# for item in list:
#     if item%2 == 0:
#         n+=1
#         print (n)        
#     else:
#         print ('not')

# # it represent the total number of even numbers
# lst = [342,52,32,45,345,32,2,52,454,34,6,63,6,36,3,6]
# n = 0
# for item in lst:
#     if item%2 != 0:
#         n+=1
# print(n)


#################  while loops

# i = 0
# while i<10:
#     print (i)
#     i+=1


# cond = True
# while cond:
#     print ('hello world')
#     cond = False

# break and continue
for i in range(10):
    if i==7:
        break
    print (i)

for i in range(10):
    if i==7:
        continue # in this the value which is given as refence to check is ignored 
    print (i)

    