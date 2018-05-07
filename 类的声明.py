#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  5 15:59:19 2018

@author: mac
"""

class student:
    student_id=0
    student_name="NOT GIVEN"
    ##在这里出现的变量值将在这个类的所有实例之间共享，在内部类或外部类使用类名.变量名访问
    def __init__(self,s_id,s_name):
        self.s_id=s_id
        self.s_name=s_name
        print("Initializing completed.")
    def showInfo(self):
        ##self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
        print("ID is %d,and Name is %s"%(self.s_id,self.s_name))
    def __del__(self):
        print("student对象%s已被销毁"%(self.s_name))
        
class Position(student):
    def __init__(self,s_id,s_name,p_name):
        self.s_id=s_id
        self.s_name=s_name
        self.p_name=p_name
        print("adding a group to your class")
    def showInfo(self):
        print("ID is %d,and Name is %s,while position is %s"%(self.s_id,self.s_name,self.p_name))
    def __del__(self):
        print("position对象%s已被销毁"%(self.s_name))

if __name__=="__main__":
    ##student A(1625111019,"liao") c++与python混淆的结果
    A=Position(1625111019,"liao","monitor")
    A.showInfo()

