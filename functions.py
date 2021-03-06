import numpy as np
import sys

#define a function that returns a value
def expo(x):
	return np.exp(x) 	#return the np e^x function
	
#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):			#i=[0,n-1]
		print(expo(float(i)))	#call the expo function e^float(i)

#define the main function
def main():
	n = 10 		#default value for n
	
	#check if a command line argument is provided
	if(len(sys.argv)>1):			#len gives length of array, passing array of sys.argv
		n = int(sys.argv[1])	    #if an argument is provided, use it for n
	
	show_expo(n)		#call the show_expo subroutine
	
#run the main function
if __name__ == "__main__":
	main()
