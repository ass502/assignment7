import numpy as np
from mandelbrot import mandelbrot

print("Question 1\n")

a=np.arange(1,16).reshape(3,5).transpose()
print a

print("\npart a:")
b=a[[1,3],:]
print b

print("\npart b:")
c=a[:,1:2]
print c

print("\npart c:")
d=a[1:4,:]
print d

print("\npart d:")
e=np.empty(shape=0)
for x in np.nditer(a): #iterate over elements of array a
	if x>=3 and x<=11:
		e=np.append(e,x)
print e	


print("\nQuestion 2\n")
	
a = np.arange(25).reshape(5, 5)
b = np.array([1., 5, 10, 15, 20])

c = np.zeros((5,5))

for col in range(0,a.shape[1]): #iterate over columns
	#divide current column in a by b element-wise, and put it in our final array
	c[:,col] = np.divide(a[:,col], b)

print c


print("\nQuestion 3\n")

print("Original 10x3 array:")
a=np.random.rand(10,3)
print a

b=abs(a-.5)
c=np.empty(10)

rowIndex=0 
for row in b: #iterate over rows, where each row contains the absolute values of differences from 0.5
	#use argsort[0] to find the smallest difference in the current row, place the corresponding initial element in our final array
	c[rowIndex]=a[rowIndex][np.argsort(row)[0]]
	rowIndex+=1

print("\nArray of values closest to 0.5:")
print c


"""Question 4"""

N_max = 50
some_threshold = 50

currIteration=mandelbrot([-2,1],[-1.5,1.5],500,500)
c=currIteration.grid
z=c

z=currIteration.iteration(z,c,N_max)

mask = currIteration.createMask(z,some_threshold)

currIteration.plotMask(mask)

