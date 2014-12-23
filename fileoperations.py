import os;

# file = open("outfile.txt", "w");
# file.write("hello world in the new file\n");
# file.write("and another line\n");

# file = open('outfile.txt', 'r');
# #print file.read();
# #print file.read(5);
# #print file.readline();

# file = open('outfile.txt', 'r');

# for line in file:
#     print line,

# file = open('outfile.txt', 'w');

# #lines_of_text = ["a line of text", "another line of text", "a third line"];
# #file.writelines(lines_of_text);

# fh = open("outfile.txt", "a");
# fh.write("Hello World again");
# fh.close;

# with open("outfile.txt") as file:
# 	data = file.read();
# 	#print data;

#file = open('outfile.txt', 'r');
#content = file.readlines()
#print content;


#os.rename('outfile1.txt','outfile2.txt');
#os.remove('outfile2.txt');
#os.mkdir("newdir");
#print os.getcwd();
#os.rmdir('newdir');

# Open a file
fo = open("toberead.txt", "rw+")
#print "Name of the file: ", fo.name


line = fo.readlines();
#print "Read Line: %s" % (line);

#line = fo.readlines(2)
#print "Read Line: %s" % (line[1])

# Close opend file
fo.close()

with open("outfile.txt",'r') as file1:
	for fileval in file1.readlines():
		print fileval,
