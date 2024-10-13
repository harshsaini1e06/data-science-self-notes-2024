# data type ->
# 1. numeric data type :-
# integer , float , char , 

print (type(10))
print (type(2.3))

# print (type(3+4i))

# boolean data type -> true , false
# print (type(true))

# sequence data type -> string , list , tuple 
# indexing is start from 0
# eg. a="hello world" -> in this the indexing is 0 to 10 and from right to left it starts from ->-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1

a='hello world'
print(a[5])
print(a[6])
print(a[-5])

# slicing in this first value is starting value, second value is ending value and the third value is jump value
print (a[0:5:1])
print (a[-11:-6:1])
print (a[-7:-12:-1])

# user defined functions -> 
# 1. library functions
# 2. inbuild function -> eg. (string) is a inbuid fumction

print (a.isupper())

k = "ram"
print (k.isupper())
print (k.islower())

a = 'hello python'
print (a.center(50,"@"))

print (a.title()) # title function
print (a.startswith('h1'))
print (a.startswith('he'))


# list (use square brackets) also mutable,slicing,indicies

a = [1,2,3,4]
print (type(a))
print (a[0:3:1])

a = [1,2,[3,[4]],[5,6]]
print (a[0])
print (a[2])
print (a[2][1][0])


##############################################

a = [2,3,[[4,5]],6,8]
print (a[2][0][1])
print (a[2][0][0:2])
print (a[2][0])

a,b=2,3
print (a,b)

a = [2,3,[[4,5]],6,8]
print (a[2][0][0],a[2][0][1])
a = [1,2,3,4]
print (a)
print (a.append(6)) # to in sert any no. at the end if the list 
print (a)
print (a.pop()) # to pop out a no. from last
print (a.pop(2)) # to pop out a no. fron the particular index

a = {1,2,3,4,3,4,5,6} # sets
print (a)

