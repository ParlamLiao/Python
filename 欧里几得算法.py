#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 15:57:49 2018

@author: mac
"""
#欧里几德
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
def gcd(a,b):
    if a<b:
        a,b=swap(a,b)
    while b!=0:
        temp=a
        a=b
        b=temp%b
    return a
if __name__=="__main__":
    numberlist=input("please input two numbers:")
    numberlist=numberlist.split(' ')
    num1=int(numberlist[0])
    num2=int(numberlist[1])
    result=gcd(num1,num2)
    print(result)
        
        
        
        
