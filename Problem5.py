#Problem 5: Complete the complex class definition to support -,*, and / ( sub , mul , and div ). 
# Recall that a/b = a*conj(b)/(b*conj(b)). 
# Show from a few sample cases that your functions work. (10)

import numpy
from numpy.fft import fft,ifft
from matplotlib import pyplot as plt

#create a class and in it put definitions for subtract, mulitply and divide
class Complex:
    
    def __init__(self,r=0,i=0):
        self.r = r
        self.i = i
    def copy(self):
        return Complex(self.r,self.i)


#call definitions of conovlutions and conjuctions
#define a correlation function => corrfun
    def corrfun(x,y):
        assert(x.size==y.size)      #if the vectors are different sizes
        fft1 = fft(x)                 #fft of x
        fft2 = fft(y)                 #fft of y
    
        #f*g =integral of f(x)g(x+y)dx AND}
        #f*g=ifft(fft1*conj(fft2))        }these are correlations
        fft2conj = numpy.conj(fft2)   #numpy provides a conj operator of fft2

        return numpy.real(ifft(fft1*fft2conj)) #returning a real vaule of the correlation

    #convolution
    def convolution(x,y):
        fft1 = fft(x)
        fft2 = fft(y)
        return real(ifft(fft1*fft2))

    def conjunction(x,y):
        fft1 = fft(x)
        fft2 = fft(y)
        fft1conj = numpy.conj(fft1)
        fft2conj = numpy.conj(fft2)
        return numpy.real(fft1conj,fft2conj)

    def subtraction(self,val):
        ans=self.copy()
        if isinstance(val,Complex):
            ans.r = ans.r-val.r
            ans.i = ans.i+val.i
        else:
            ans.r = ans.r-val
        return ans

    def multiplication(self,val):
        ans=self.copy()
        if isinstance(val,Complex):
            ans.r = ans.r*val.r
            ans.i = ans.i*val.i
        else:
            ans.r = ans.r*val
        return ans

    def division (a,b):
        ans=self.copy()
        a=a
        b=b
        aconj = conjunction (a,0)
        bconj = conjunction (0,b)

        aDivb=a*aconj/b*bconj
        if isinstance(aDivb,Complex):
            ans.r=ans.r/aDivb.r
            ans.i=ans.i/aDivb.i
        else:
            ans.r = ans.r/aDivb
        return ans 


#let b=some number and x = some number
b = 20
c = 10

#subtraction
bminusc=b-c
print (str(bminusc))

bcdiff=Complex.subtraction(b,c)
print (str(bcdiff))

if (bminusc==bcdiff):
    print ("b ("+str(b)+") subtract c ("+str(c)+") is "+str(bminucc))
else:
    print ("An error occurred")

#multiplication
bmultc=b*c
print (str(bmultc))

bctimes=Complex.multiplication(b,c)
print (str(bctimes))

if (bmultc==bctimes):
    print ("b ("+str(b)+") multiplied by c ("+str(c)+") is "+str(bmultc))
else:
    print ("An error occurred")

#division
bdivc=b/c
print (str(bdivc))

bcdiv=Complex.division(b,c)
print (str(bcdiv))

if (bdivc==bcdiv):
    print ("b ("+str(b)+") divided by c ("+str(c)+") is "+str(bdivc))
else:
    print ("An error occurred")






