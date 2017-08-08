# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 15:37:28 2017

@author: Nick
"""

class Rectangle(object):
    def __init__(self,width=1, height=2):
        self.width = width
        self.height = height
        
#    def area(self):
#        area = self.width * self.height
#        return area
#    
#    def perimeter(self):
#        per = self.width * 2 + self.height * 2
#        return per

    def __str__(self):
        """returns the given dimentions in terms of #'s"""
        rect = ""
        
        for i in range(self.height):
            rect += 'x'
        

            for x in range(self.width):
               #print(x*rect)
                return print(x*rect)
