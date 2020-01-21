

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
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

