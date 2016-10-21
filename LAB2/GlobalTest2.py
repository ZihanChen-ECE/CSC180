#! /usr/bin/env python

def add(b):
    global a
    a = 2
    return a+b
    
def find_a():
    return a
    
def modify_a():
    a = 6
    
    
def modify_a1():
    global a
    a = 100
    
    
if __name__ == '__main__':
    print(add(3))
    print(find_a())
    modify_a()
    print(find_a())
    modify_a1()
    print(find_a())