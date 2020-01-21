
class Student(Person):    
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores        

    def calculate(self):
        letter=""
        s = sum(self.scores) / len(scores)
        if 90 <= s <= 100:
            letter = 'O'
        elif 80 <= s < 90:
            letter = 'E'
        elif 70 <= s < 80:
            letter = 'A'
        elif 55 <= s < 70:
            letter = 'P'
        elif 40 <= s < 55:
            letter = 'D'
        elif s < 40:
            letter = 'T'
        return letter
