#! /usr/bin/env python
#-*- coding: utf-8 -*-

#this code is for implementing Stack class via list

#the error/exception case, inherits from class ValueError
class StackUnderflow(ValueError):
    pass

#creating the stack with continuous list
class SStack():
    
    def __init__(self):
        self.elems = []
        
    def is_empty(self):
        return self.elems == []
        
    def top(self):
        if self.is_empty():
            raise StackUnderflow
        return self.elems[len(self.elems)-1]
    
    def push(self, elem):
        self.elems.append(elem)
        
    def pop(self):
        if self.is_empty():
            raise StackUnderflow
        return self.elems.pop()
        
    def depth(self):
        return len(self.elems)
        
    def show_stack(self):
        print(self.elems)
    
#creating a stack via linked list
class LNode():
    def __init__(self, elm, next = None):
        self.elem = elm
        self.next = next
class LStack():
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top == None
        
    def top(self):
        if self.is_empty():
            raise StackUnderflow
        else:
            return self.top.elem
            
    def pop(self):
        if self.is_empty():
            raise StackUnderflow
        p.self.top
        self.top = p.next
        return p.elem
        
    def push(self, elm):
        self.top = LNode(elm,self.top)
            
            
if __name__ == '__main__':
    pass
            
            
            
            
        