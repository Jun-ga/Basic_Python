class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here

    def __init__(self, elements):
        self.elements = elements
    def computeDifference(self):
        self.maximumDifference = max(self.elements)-min(self.elements)


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
