#!/usr/bin/python
import MySQLdb
# Open database connection
db 		= 	MySQLdb.connect("localhost","root","password","pythondb");
cursor 	= 	db.cursor()

print "Please select the action to be performed : \n 1. List \n 2. Insert \n 3. Update \n 4. Delete \n";
getActionType = raw_input("Select the Option :");

if getActionType == '1':
	cursor.execute("SELECT Id,title,author,published_date FROM books_tbl");
	results = cursor.fetchall();
	print "*******************************************************************";
	for row in results:
		id 		= 	row[0];
		title 	= 	row[1];
		author 	= 	row[2];
		pdate 	= 	row[3];
		
		print "Id : %s,Title : %s, Autor : %s, Published Date : %s " % \
             (id, title,author,pdate)
     	print "***************************************************************";
elif getActionType == '2':	

	argtitle		=	raw_input("Enter the Book Title : ");
	argauthor		=	raw_input("Enter the Author Name : ");
	insqry 			= 	"INSERT INTO books_tbl(title,author) VALUES ('%s','%s')" % (argtitle,argauthor);

	try : 
		cursor.execute(insqry);	
		db.commit();
		print "Inserted Successfully";
	except :
		print "Something went Wrong. Try Again !!!";
	
elif getActionType == '3':

	argid		=	raw_input("Enter the Id to be updated : ");
	argtitle	=	raw_input("Enter the Book Title : ");
	argauthor 	=  	raw_input("Enter the Author Name : ");	
	updqry		=	"UPDATE books_tbl SET title = '%s',author = '%s' WHERE Id = %s" % (argtitle,argauthor,argid);		
	
	try : 
		cursor.execute(updqry);	
		db.commit();
		print "Updated Successfully";
	except :
		print "Something went Wrong. Try Again !!!";

elif getActionType == '4':
	argid		=	raw_input("Enter the Id to be deleted : ");
	delqry		=	"DELETE FROM books_tbl WHERE Id = %s" % (argid);

	try : 
		cursor.execute(delqry);	
		db.commit();
		print "Deleted Successfully";
	except :
		print "Something went Wrong. Try Again !!!";

else:
	print "Invalid option chosen";

db.close();