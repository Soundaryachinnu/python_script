# def print_func( par ):
# 	print "Hello : ", par
# 	return
#!/usr/bin/python

class mathfunc:
	def __init__(self, a, b):
		self.a = float(a)
		self.b = float(b)

   # def __str__(self):
   #    return 'Result (%d)' % (self.a)
   
   # def __add__(self,other):
   # 		return mathfunc(self.a+other.a);

   # def __sub__(self,other):
   # 		return mathfunc(self.a-other.a);

   # def __mul__(self,other):
   # 		return mathfunc(self.a*other.a);

   # def __div__(self,other):
   # 		return mathfunc(self.a/other.a);  

   # def funcadd(self,other):
   # 		print self.a+other;

   # def funcsub(self,other):
   # 		print self.a-other;

   # def funcmultiply(self,other):
   # 		print self.a*other;

   # def funcdivide(self,other):
   # 		print self.a/other;

	def funcadd(self):
		print self.a+self.b;

	def funcsub(self):
		print self.a-self.b;

	def funcmultiply(self):
		print self.a*self.b;

	def funcdivide(self):
		print self.a/self.b;  

	def __del__(self):			
		class_name = self.__class__.__name__
		print class_name, "destroyed"

# class hello:
# 	def __init__(self, a, b):
# 		self.a = a   
# 		self.b = b
# 	def additionfunc(self):
# 		print self.a + self.b;