#learning about common data type in python
# https://docs.python.org/3/library/stdtypes.html
# https://docs.python.org/3/library/functions.html 
#str,int,float,bool,list,tuple,set,dict,none
#making a string 
"hello"#example of a str
str("hello")#through use of a string constructor function
#string interpolation
My_name = "Samuel"
print(f"My name is {My_name}")
#NB on quotation marks
Height = 6
print(f"My estimate height is in between {Height:.2f}")
#use of .upper(),.lower(),.capitalize() to change the case of a string
print ('hello'.upper())
print ('hello'.lower())
print ('hello'.capitalize())
print(type('hello'))
print(dir('hello'))
print (type(5))
#Numbers
#Type of number 
#int the whole value numbers
#float the decimal numbers
#how to cnvert each
print (int(5.95))
print (float(5))
#list writing 
list = [1,2,3,4,5]
print (list)
list.append(6)
print (list)
#set
set = {1,2,3,4,5}
print (set)
set.add(6)
print (set)
#tuple
tuple = (1,2,3,4,5)
print (tuple)
tuple.append(6)
print (tuple)
#dict
dict = {'key':'value'}
print (dict)
my_dict = {'key1':'value1','key2':'value2'}
my_dict['key3'] = 'value3'
print(my_dict)    
#none
#print (None)
# none is a value of type NoneType
# NoneType is a type of None
# NoneType is a subtype of all types
# NoneType is an instance of all types
# NoneType is an instance of object
no_value = None
print(no_value)   
#representation of boolean value
#print (True)
# print (False)
                                   