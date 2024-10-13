#  to count any letter in any string , list and tuple
a = "hello world"
print (a.count('l'))

a = [1,2,3,3,4,5]
print (a.count(3))

a = (1,2,3,4,4,5,6)
print (a.count(4))

# unpacking is used to pick out a thing out of round brackets eg. ->a,b = (1,2)

a = "hello world"
print (a.capitalize())

a = ' hello world  '
a1=a.strip()
print (a1)
print (a)

print (a1.split())

print ('@'.join(a1)) # here the indexing is from 0 to 10 so there are several string members

a2 = a1.split()
print (a2)
print ('@'.join(a2)) # here the string elements are two 

# inserting single element

l = [1,2,3,4,5]
print (l)
l.insert(0,23) # first index then the desired insert no.
print (l)

# insert multiple no.

l.append([6,7,])
print (l)

l.remove(23) # to remove any element
print (l)

l2 = [8,9]
l+=l2 # to add lists together
print (l)

l3 ='start' # it has indexing 0 to 4 so it finally add in a string manner not a complete 'start'
l+=l3
print (l)

l6 = [2,3,4,5]
l3 = ['start'] #here start become a list and join as a single element
l6+=l3
print (l6)

l = [3,2,5,7]
l.reverse() # here it only invers the indexes of the list
print (l)
l.sort()
print (l)
l.reverse() # now it is in desending order
print (l)

# l1 = [1,5,8,4,6,3,9,0] #### throwing error
# l1.sort(reverse=true)
# print (l1)

l1 = ['banana','apple']
l1.sort()
print (l1)

a = 'a'
print (type(a))

# dictionary {keys : values}
# set{1,}
# maling a dictionary
d1 = {'Age':[31,23,45,62,41],'name':['r','t','y']}
print (d1)
print (type(d1))
print (d1['name'])

d2 = { 'age':(1,2,3)}
print (type(d2))

d1 = {'Age':[31,23,45,62,41],'name':['r','t','y'],'weight':[56,78,65]}
d1['name'] += 'frg' # to add name 
print (d1)

d3 = {1:'aka'}
print (d3) 

d4 = {'A':30,'b':34}
print (d4.get('A'))

s1 = {1,2,3,4}
print (s1.pop())
print (type(s1))
s2 = {4,5,6,7}
print (s1.union(s2))
print (s1.intersection(s2))

s1 = {1,2,3,4}
s1.add('h1')
print (s1)

s3 = {7,8,9}
s1.update(s3)
print (s1)

s1.clear()
print (s1)

###############################################################

##  user inputs

a = input('enter your name')

