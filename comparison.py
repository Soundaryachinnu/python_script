#def fngreatest(strList):
# varlist = raw_input('Enter the numbers to be sorted : ');
# sublist = varlist.split(',');
# maxstring = max(sublist);
# print "Given List :", sublist;
# sublist.remove(maxstring);
# maxstring = max(sublist);
# print "Second Largest String :", maxstring;

# import json
# import heapq
# varlist = raw_input('Enter the numbers to be sorted : ');
# sublist = varlist.split(',');
# res 	= heapq.nlargest(2, sublist);
# print res[1]; 

# varlist = raw_input('Enter the numbers to be sorted : ');
# sublist = varlist.split(',');
# #sublist.sort();
# print sublist;
# sublist.sort();
# # print sortedvalue[0];
# # print sortedvalue[1];
# # print sortedvalue[2];
# import urllib2
# import json
# j = urllib2.urlopen('https://api.github.com/users/mralexgray/repos');
# j_obj = json.load(j);
# print "JSON parsing example: ", j_obj['name'];

# actual code 

# import heapq
# varlist = raw_input('Enter the numbers to be sorted : ');
# sublist = varlist.split(',');
# res 	= heapq.nlargest(2, sublist);
# print res[1]; 

# import json
# import urllib2
 
# j = urllib2.urlopen('https://api.github.com/users/mralexgray/repos');
# json_input = json.load(j);
# for name in json_input:
# 	if name['fork']:
# 		print name['name'];


# import os
# import datetime
# filename	=	'toberead1.txt';
# outfile		=	'newtestfile.txt';
# filesize 	= 	os.path.getsize(filename);
# getinput	=	open(filename, "rw+");

# try:
# 	if filesize < 1048576:
# 		print 'hiii';
# 		OldfileContent 	= 	getinput.read();		
# 		writefile 		= 	open(outfile,'w');	
# 		writefile.write(OldfileContent);		
# 		writefile.close();
# 		appendfile 		= 	open(outfile,'a');
# 		currenttime 	= 	datetime.datetime.now();	
# 		appendfile.write(str(currenttime))
# 		appendfile.close();
# 		print "Written content in the file successfully";
# except IOError:
#    print "Error: can\'t find file or read data"
# else:
#    print "File size is greater than 1MB"

# getinput.close();

# myList = [1,2,3,4,5]
# print myList
# index = input("Enter the index you would like to see: ")
# try:
# 	print myList[index]
# except IndexError:
# 	print "You have entered an invalid index."


#   try:
#        i_num = int(input("Enter a number: "))
#        if i_num < number:
#            raise ValueTooSmallError
#        elif i_num > number:
#            raise ValueTooLargeError
#        break
#    except ValueTooSmallError:
#        print("This value is too small, try again!")
#        print()
#    except ValueTooLargeError:
#        print("This value is too large, try again!")
#        print()

# print("Congratulations! You guessed it correctly.")


class ValueTooSmallError():
   """Raised when the file size is too large"""
   pass

import os
import datetime
filename		=	'toberead1.txt';
outfile			=	'output.txt';
filesize 		= 	os.path.getsize(filename);
inputfileSize 	= 	float(filesize) / (1024*1024);

try:
	if inputfileSize > 1:		
		raise ValueTooSmallError;
	else:
		writefile			=	open(outfile, "w");
		inputFileCont		= 	"Size of the Input File : %.2f" % inputfileSize + '\n';		
		appendfileContent 	= 	open(outfile,'a');
		writefile.write(inputFileCont);		
 		writefile.close();

 		appendfile 			= 	open(outfile,'a');
		currenttime 		= 	datetime.datetime.now();	
		appendfile.write(str(currenttime))
		appendfile.close();

except ValueTooSmallError:
 	print "File size is greater than 1MB";





