#!/usr/bin/python

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class Child(Parent): # define child class
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

# c = Child()          # instance of child
# c.childMethod()      # child calls its method
# c.parentMethod()     # calls parent's method
# c.setAttr(130)       # again call parent's method
# c.getAttr()          # again call parent's method

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vecdddtor (%d, %d)' % (self.a, self.b)
   
   def __sub__(self,other):      
      return Vector(self.a - other.a, self.b - other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 - v2 


class chkgreater:
   def __init__(self,a,b):
      self.a = a;
      self.b = b;

   def __str__(self):
      return 'greater (%d)' % (self)

   def _gt__(self,a,b):
      if(self.a > self.b):
         return chkgreater(self.a);
      else:
         return chkgreater(self.b);

print chkgreater(10,4);
