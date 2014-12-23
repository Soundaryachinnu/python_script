print 'test python'

a = 2
b = 3
c = 4

list_test = [1,2,3,4]
stringi = 'dfdfdf'
for var in list_test:
	if c == var:
		print stringi + str(c)		
	else:
		print 'not found'

print 'Sample Program II'
name = raw_input('What is your name?\n')
print 'Hi, %s.' % name

print 'Sample Prgram III'
friends = ['john', 'pat', 'gary', 'michael']
print friends
for i, name in enumerate(friends):
    print i, name
