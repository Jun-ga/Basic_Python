class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
        
    def calculate(self):
        sum = 0
        for x in range(0, len(scores)):
            sum = sum + scores[x]
            avg = sum / len(scores)
                
        if avg >= 90:
            return 'O'
                    
        elif avg >= 80:
            return 'E'
                    
        elif avg >= 70:
            return 'A'
                    
        elif avg >= 55:
            return 'P'
                    
        elif avg >= 40:
            return 'D'
                    
        else:
            return 'T'

line = input().split()
