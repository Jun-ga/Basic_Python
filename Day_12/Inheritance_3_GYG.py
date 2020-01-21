![12](https://user-images.githubusercontent.com/56713634/72675501-77713700-3ac8-11ea-8676-2803d7e0fb72.jpg)
https://wikidocs.net/28
https://wikidocs.net/16073
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores 

    def calculate(self):
        grade = ''
        scores_avg = sum(self.scores) / len(scores)
        if 90 <= scores_avg <= 100:
            grade = 'O'
        elif 80 <= scores_avg < 90:
            grade = 'E'
        elif 70 <= scores_avg < 80:
            grade = 'A'
        elif 55 <= scores_avg < 70:
            grade = 'P'
        elif 40 <= scores_avg < 55:
            grade = 'D'
        elif scores_avg < 40:
            grade = 'T'
        return grade
    #   Class Constructor
