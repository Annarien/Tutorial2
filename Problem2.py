#Problem 2: The correlation function f ?g is R f(x)g(x + y)dx. 
# Through a similar proof, one can show f?g=ift(dft(f)*conj(dft(g))). 
# Write a routine to take the correlation function of two arrays. 
# Plot the correlation function of a Gaussian with itself. (10)
#__________________________________________________________________________________
import numpy
from numpy.fft import fft,ifft
from matplotlib import pyplot as plt

#define a correlation function => corrfun
def corrfun(x,y):
    assert(x.size==y.size)      #if the vectors are different sizes
    fft1=fft(x)                 #fft of x
    fft2=fft(y)                 #fft of y
    
    #f*g =integral of f(x)g(x+y)dx AND}
    #f*g=ifft(fft1*conj(fft2))        }these are correlations
    fft2conj=numpy.conj(fft2)   #numpy provides a conj operator of fft2

    return numpy.real(ifft(fft1*fft2conj)) #returning a real vaule of the correlation

start = -10
end = 10
interval = 0.1
sigma=0.5

if __name__=='__main__':
    
        x=numpy.arange(start,end,interval)
        y=numpy.exp(-0.5*x**2/sigma**2)
        ycorr=corrfun(y,y)
        plt.plot(x,ycorr)
        plt.show()