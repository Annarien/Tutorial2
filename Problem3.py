#Problem 3: Using the results of part 1 and part 2, write 
# a routine to take the correlation function of a Gaussian 
# (shifted by an arbitrary amount) with itself. 
# How does the correlation function depend on the shift?
#  Does this surprise you? (10)

import numpy
from numpy.fft import fft,ifft
from matplotlib import pyplot as plt

#from question 1 and 2, get the definitions

def shift (y,n=0):
    vec=0*y        #make a vector of zeros the same length as the input vector
    vec[n]=1
    print (vec)
    fft1=fft(vec)
    fft2=fft(y)
    return real(ifft(fft1*fft2))

def corrfun(x,y):
    assert(x.size==y.size)      #if the vectors are different sizes
    fft1=fft(x)                 #fft of x
    fft2=fft(y)                 #fft of y
    
    #f*g =integral of f(x)g(x+y)dx AND}
    #f*g=ifft(fft1*conj(fft2))        }these are correlations
    fft2conj=numpy.conj(fft2)   #numpy provides a conj operator of fft2
    return numpy.real(ifft(fft1*fft2conj))


#paramter values
start = -10
end = 10
interval = 0.1
sigma= 0.5

if __name__=='__main__':
        x = numpy.arange(start,end,interval)
        y = numpy.exp(-0.5*x**2/sigma**2)

        #correlation by itself corrfun(y,y)
        ycorr = corrfun(y,y)

        yby4 = (y.size)/4
        yshift= shift(y,yby4)
        #shift correlation by itself
        yshiftcorr = corrfun(yshift,yshift)

        #error of correlation between the shift and the correlation of the y function is
        #the average of the absolute value of the difference between the two
        diffCorr = ycorr-yshiftcorr
        absDiffCorr = numpy.abs(diffCorr)
        errorOfCorr = numpy.mean(absDiffCorr)

        print ("The original function is "+str(y)+" and its correlated function is "+str(ycorr))
        print ("The shifted function is "+str(yshift)+" and its correlated function is "+ str(yshiftcorr))
        print("The difference between the correlation and the shift correlation function is "+str(diffCorr))
        print ("The average difference between the two correlated functions is "+str(errorOfCorr))
     
        plt.plot(x,ycorr)
        plt.plot(x,yshiftcorr)        
        plt.show()
        