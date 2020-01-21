    maximumDifference = 0
    def computeDifference(self):
        l = len(a)
        for i in range(l):
            for j in range(i + 1, l):
                difference = abs(a[i] - a[j])
                self.maximumDifference = max(difference, self.maximumDifference)

