# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 15:14:13 2017

@author: Nick
"""

#Fraction example
#http://interactivepython.org/runestone/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:

    def __init__(self,top,bottom):

        self.num = top
        self.den = bottom

    def show(self):

        print(self.num,'/',self.den)

        
    def __str__(self):
        """
        using print(f) shows the fraction as normal
>>> f=Fraction(3,5)
>>> print(f)
3/5
>>> f.__str__()
'3/5'
>>> str(f)
'3/5'
        """
        return str(self.num)+'/'+str(self.den)


    def __add__(self,otherfraction):

        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den*otherfraction.den

        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)