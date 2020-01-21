 def computeDifference(self):
        sorted_array = sorted(self.__elements)
        self.maximumDifference = abs(sorted_array[-1] - sorted_array[0])

