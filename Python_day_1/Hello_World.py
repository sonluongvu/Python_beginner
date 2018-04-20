print "Hello World!"
print "Hello, Python!"
s = "How are you?"
print s

if False: #Replace with True to get else
    print "Answer"
    print "True"
else :
    print "Answer"
    print "False"

stri = "This is first string!"
print stri #print complete string
print stri[0] #print first character of the string
print stri[2:5] #print characters starting from 3rd to 5th
print stri[2:] #print string starting from 3rd character
print stri * 2 #print string 2 times
print stri + "Test" # prints concatenated string

list = [ 'abcd', 786, 2.23, 'john', 70.2]
tinylist = [ 123, 'john']

print list
print list[0] #print the first element of the list
print list[1:3] #print elements starting from 2nd till 4th
print list[2:] #print elements starting from 3rd
print tinylist * 2 #print list 2 times
print list + tinylist #print concatenated list

tuple = (123, 'john') #same as list but tuple can not be changed

print tuple[1:3] #print elements starting from 2nd till 3rd

dict = {}
dict['one'] = "this is one"
dict[2] = "this is two" #assign value into dictionary

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'} #it is key-value pairs

print dict['one'] #print value for 'one' key
print dict[2] #print value for 2 key
print tinydict
print tinydict.key() #print all the keys
print tinydict.value() #print all the values
