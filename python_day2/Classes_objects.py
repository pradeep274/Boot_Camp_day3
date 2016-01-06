

class Person:        # define Person class
	def getGender(self):
      		print 'person'


class Male(Person): # define Male class
	def getGender(self):
      		print 'male'

class Female(Person): # define Female class
	def getGender(self):
      		print 'female'


a = Person()		# instance of Person
a.getGender()
c = Male()		# instance of Male     
c.getGender()
d= Female()		# instance of Female
d.getGender()          
