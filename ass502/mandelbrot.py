"""contains the mandelbrot class"""

import numpy as np
import matplotlib.pyplot as plt

class mandelbrot:
	
	def __init__(self,xBounds,yBounds,xSteps,ySteps):
		"""creates an instance of a grid of points"""
	
		x,y = np.meshgrid(np.linspace(xBounds[0],xBounds[1],xSteps),np.linspace(yBounds[0],yBounds[1],ySteps))

		self.grid = x + 1j*y

	def iteration(self,z,c,N_max):
		"""computes the Mandelbrot iteration a specified number of times on our grid instance"""
	
		for v in range(N_max):
			with np.errstate(all='ignore'): #catches overflow and invalue value errors
        			z=z**2 + c
		return z

	def createMask(self,z,threshold):
		"""creates a mask of values that are still in the set i.e. have absolute value below the specified threshold"""

		with np.errstate(invalid='ignore'): #catches invalid value errors
			mask = np.abs(z) < threshold
			return mask

	def plotMask(self,mask):
		"""plots the mask"""	

		plt.imshow(mask,extent=[-2,1,-1.5,1.5])
		plt.gray()
		plt.savefig('mandelbrot.png')
		
		
