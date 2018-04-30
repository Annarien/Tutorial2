#Problem 1: Write a function that will shift an array by an arbitrary amount using a convolution 
# (yes, I know there are easier ways to do this). 
# The function should take 2 arguments - an array, and an amount by which to shift the array. 
#  Plot a gaussian that started in the centre of the array shifted by half the array length. (10)

import numpy
from numpy import arange, exp, real
from numpy.fft import fft, ifft
from matplotlib import pyplot as plt

# shift(y,n): shifts an array y by an amount n 
#shift is the convolution of y and n
def shift (y,n):
    vec=0*y        #make a vector of zeros the same length as the input vector
    vec[n]=1
    print (vec)
    fft1=fft(vec)
    fft2=fft(y)
    return real(ifft(fft1*fft2))

#variables that can change
start=-20
end=20
interval=0.1
sigma=0.5

if __name__=='__main__':
    #x=arrange from start to finish with the respective interval.
    x=numpy.arange(start,end,interval)
    y=numpy.exp(-0.5*x**2/sigma**2)
    yby2=(y.size)/2
    yshift=shift(y,yby2) #Divide by 2 such that the centre is in the middle of the guassian

    #plotting on graph
    plt.ion()
    plt.plot(x,y)
    plt.plot(x,yshift)




    