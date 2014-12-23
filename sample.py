#!/usr/bin/python

print "Hello, Python!";

if True:
	print "Answer";
	print "True";
else:
   	print "Answer";
  	print "False";

total = 'item_one' + \
        'item_two' + \
        'item_three'

print total;

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print days

paragraph = """This is a paragraph. It is
made up of multiple lines and sentences.""";

print paragraph;

raw_input("\n\nPress the enter key to exit.")

import sys; x = 'foo'; sys.stdout.write(x + '\n')

var1 = 1;
del var1;
#print var1;

str = 'Hello World!';
print str[2:6];
print str[2:];

list1 = [ 'abcd', 786 , 2.23, 'john', 70.2  ];
list1[2] = 1000;

print list1;

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print tinydict.keys();
print tinydict.values();

a = 2;
b = 3;
print a | b;
print a * b;
print a ** b;

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
	if fruits[index] !='':
   		'Current fruit :', fruits[index]

#print "Good bye!"


for letter in 'Python': 
   if letter == 'h':
      continue      
      print 'This is pass block'
   print 'Current Letter :', letter

print "Good bye!"


def printme( str ):   
	print str;
   	return

printme('function test');