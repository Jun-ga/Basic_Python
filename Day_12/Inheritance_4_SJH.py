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
        sum_scores = 0
        for i in range(0, len(scores)):
            sum_scores = sum_scores + scores[i]
        
        average = sum_scores / len(scores)
                
        if average >= 90:
            return 'O'
                    
        elif average >= 80:
            return 'E'
                    
        elif average >= 70:
            return 'A'
                    
        elif average >= 55:
            return 'P'
                    
        elif average >= 40:
            return 'D'
                    
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
