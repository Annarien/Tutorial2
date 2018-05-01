#The circulant (wrap-around) nature of the dft can sometimes be problematic. 
# Write a routine to take the convolution of two arrays
# without any danger of wrapping around. 
# You may wish to add zeros to the end of the input arrays. (10)

import numpy
from numpy.fft import fft,ifft
from matplotlib import pyplot as plt

#define a definition where two arrays are convolved without wrapping
def noWrapConvolution(x,y):
    assert(x.size==y.size)  
    #size of x must equal size of y, otherwise it wont work
    assert(x.size==y.size)  

    # make an array double the size of x vector, and put in zeros
    x1=numpy.zeros(2*x.size)
    y1=numpy.zeros(2*y.size)   

    #a value at the end of the first array is convolved with the end value of second array => endup at the end of new zero array
    x1[0:x.size]=x
    y1[0:y.size]=y

    #respective fourier transforms for x1 and y1
    x1fft=fft(x1)
    y1fft=fft(y1)
    yvector=numpy.real(ifft(x1fft*y1fft))
    return yvector[0:x.size]

#parameter values of array
start = -10
end = 10
interval = 0.1
sigma=0.5

if __name__=='__main__':
    x=numpy.arange(start,end,interval)
    y=numpy.exp(-0.5*x**2/sigma**2)
    sumy=y.sum()
    y2=y/sumy

#convolution of y is the convolution of y and y2 without wrapping
    yconv=noWrapConvolution(y,y2)
    plt.plot(x,y)
    plt.plot(x,yconv)
    plt.show()
