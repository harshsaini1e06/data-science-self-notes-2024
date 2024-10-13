print ('hello world')

print (3*'hello')

# key words

import keyword
print (keyword.kwlist) 
print (len (keyword.kwlist))

# arthematic operators -> //(floor division), ** -> exponential

print (4**2)
print (8//2)

# relational operator ->
 
print (2==3)
print (2>3)
print (2<3)
print (2>=3)
print (2<=3)
print (2!=3)

_ = 2
print (_)

# assignment operator -> =, += (x+=3-> x=x+3), -= , *=, 

x=3
x+=3
print (x)

# logical operators -> and, or , not

print (2<3 and 3>2)
print (2<3 or 3<2)

# bit wise operator -> other logical operators other than previous one (& , ||, ..... , ^ , etc.)

# identity operators -> is , is not

x=3
y=3
print (x is y)
print (x is not y)

# membership operators -> in , not in 

x = [1,2,3]
print (1 in x)
print (5 in x)


# data type 
# 1. sequence data type -> list , string , tuple (comma seperated) 

x = 'ram'
print (type(x))
print (len(x))
print (x[1])
# print (x[1]=k) -> it is immuable (string)

x = [1,2,3,4]
print (type(x))
print (x[1])
x[1] = 5
print (x)

x = [1,2,3,3,4,4,5,6]
print (x)
print (type (x))
print (x)
