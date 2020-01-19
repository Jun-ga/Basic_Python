class Person:
    def __init__(self,initialAge):
        self.age = initialAge
        if age < 0:
            print('Age is not valid, setting age to 0.')
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if self.age<13:
            print('You are young.')
        elif 13 <= self.age < 18:
            print('You are a teenager.')
        elif 18 <= self.age:
            print('You are old.')
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        self.age = self.age + 1
        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")

