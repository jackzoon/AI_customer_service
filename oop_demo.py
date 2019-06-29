#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 定义一个类，类名为Student
class Student(object):
    count = 0
    def __init__(self, sno, name):
        self.sno = sno
        self.name = name
        Student.count = Student.count + 1

    def show(self):
        print(self.sno, self.name)

s1 = Student(1001, "张三") 
s1.show()
s1.age = 33
s1.qq = '32432432'
print(s1.age, s1.qq)