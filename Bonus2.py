#Bonus 2: Extend the complex class to also support arbitrary (i.e. non-integer) powers (key-
#word is pow ). +3 if the routine works if ab works for complex a and real b, +5 if it works for
#complex a and complex b. (you may ignore branch cuts).

import numpy
from numpy import pyplot as plt
import matplotlib
import math


class cc:

    def __init__(self,r=0,c=0):
        self.r=r
        self.i=c
    def copy(self):
        return cc(self.r,self.i)

#addition
    def __add__(self,val):
        ans=self.copy()
        if isinstance(val,cc):
            ans.r=ans.r+val.r
            ans.c=ans.i+val.i
        else:
            ans.r=ans.r+val
        return ans

# multiplication
    def __mul__(self,val):
        ans=self.copy()
        if isinstance(val,cc):
            ans.r=self.r*val.r-self.i*val.i
            ans.i=self.r*val.i+self.i*val.r
        else:
            ans.r=ans.r*val
            ans.i=ans.i*val
        return ans

#subtraction
    def __sub__(self,val):
        ans=self.copy()
        if isinstance(val,cc):
            ans.r=ans.r+val.r
            ans.c=ans.i-val.i
        else:
            ans.r=ans.r-val
        return ans

#division
    def __div__(self,val):
        if isinstance(val,cc):
            val=val.copy()
            val.i=-1*val.i
            ans=self*val
            myabs=val.r**2+val.i**2
            ans=ans*(1.0/myabs)
        else:
            ans=self*(1.0/val)
        return ans
#power simple
    def __pow_simple__(self,val):
        ang=math.atan2(self.i,self.r)
        abs=math.sqrt(self.i*self.i+self.r*self.r)
        ans=self.copy()
        newabs=abs**val
        newang=ang*val
        ans.r=newabs*math.cos(newang)
        ans.i=newabs*math.sin(newang)
        return ans

#power 
    def __pow__(self,val):
        if isinstance(val,cc):
            ang=math.atan2(self.i,self.r)
            myabs=math.sqrt(self.i*self.i+self.r*self.r)
            myexp=cc(math.log(myabs),ang)
            totexp=myexp*val
            newabs=math.exp(totexp.r)
            newang=cc(math.cos(totexp.i),math.sin(totexp.i))
            return newang*newabs
        else:
            return self.__pow_simples__(val)

    def __repr__(self):
        if (self.i<0):
            return repr(self.r)+' - '+repr(-1*self.i) +'i'
        else:
            return repr(self.r)+' + '+repr(self.i) +'i'
    def __lshift__(self,crud):
        self.i=-1*self.i

        

