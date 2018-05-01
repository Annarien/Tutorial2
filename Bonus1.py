#Bonus 1: You have a sample code that calculates an FFT of an array whose length is a power
#of 2. Using that routine as a guideline, write an FFT routine that works on an array whose length
#is a power of 3 (e.g. 9, 27, 81). Verify that it gives the same answer as numpy.fft.fft (10)


from numpy import concatenate,exp,pi,arange,complex
import numpy

#sample code for FFT
def myfft(vec):
    n=vec.size
    
    if n==1:
        return vec
   
    myeven=vec[0::2]
    myodd=vec[1::2]

    nn=n/2;
    j=complex(0,1)    
    #get the phase factors
    twid=exp(-2*pi*j*arange(0,nn)/n)

    #get the dfts of the even and odd parts    
    eft=myfft(myeven)
    oft=myfft(myodd)

    #Now that we have the partial dfts, combine them with 
    #the phase factors to get the full DFT
    myans=concatenate((eft+twid*oft,eft-twid*oft))
    return myans

#Coding for base 3 numbers
def myfft3(vec):
    n=vec.size
    if n <= 1: 
        return vec
    mya=vec[0::3]
    myb=vec[1::3]
    myc=vec[2::3]
    
    nn=n/3
    j=complex(0,1)     
    twid1=exp(-2*pi*j*arange(0,nn)/n)
    twid2=exp(-4*pi*j*arange(0,nn)/n)

    f1=exp(-2*pi*j/3) #n/3<=k/2n/3
    f2=exp(-4*pi*j/3)
    f1b=f2;          # 2n/3<=k<n
    f2b=f1; 

    aft=mya
    bft=myb*twid1
    cft=myc*twid2
    
    print("1:" + str(aft))
    print("2:" + str(bft))
    print("3:" + str(cft))

  
    ft1=aft+bft+cft
    ft2=aft+bft*f1+cft*f2
    ft3=aft+bft*f1b+cft*f2b
    
    ft=concatenate((ft1,ft2,ft3))

    return ft
x = numpy.random.randn(3)
#x1 = myfft(x)
x2 = myfft3(x)

#print (x1)
print (x2)