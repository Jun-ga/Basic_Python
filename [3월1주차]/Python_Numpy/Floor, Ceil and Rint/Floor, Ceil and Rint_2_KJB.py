import numpy

numpy.set_printoptions(sign=' ') #리스트?들 사이 간격 띄어주는거 이거말고 방법없나, 처음 보는 방식이라 생소함

a = numpy.array(input().split(),float)

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))
