#! /usr/bin/env python
#-*- coding:uft-8 -*-

#this code is for the queue class

import StackClass as SC

class LQueue():
    def __init__(self):
        self.head = None
        self.rear = self.head
    
    def find_head(self):
        return self.head.elem
        
    def find_rear(self):
        return self.rear.elem
    
    def is_empty(self):
        return self.head is None
    
    def enqueue(self, elm, next = None):
        if self.head == None and self.rear == None:
            self.head = SC.LNode(elm,next)
            self.rear = self.head
        else:
            p = self.rear
            self.rear = SC.LNode(elm, next)
            p.next = self.rear
        
    def dequeue(self):
        if self.is_empty():
            raise ValueError('The queue is empty')
        p = self.head.next
        value = self.head.elem
        self.head = p
        return value
        
    def length(self):
        p = self.head
        count = 0
        while p!=self.rear:
            count+=1
            p = p.next
        return count
        
    def display_queue(self):
        if self.is_empty():
            raise ValueError('The queue is empty')
        p = self.head
        if p == self.rear:
            print(p.elem)
        else:
            while p!=None:
                print(p.elem, end = " ")
                p = p.next
            print('')
            return 0
            
        
class PrioQue():
    def __init__(self, lst = []):
        self.elems = sorted(lst)
        
    def enqueue(self,e):
        i = len(self.elems)-1
        while i >= 0:
            if self.elems[i] <=e: #the list is sorted from large to small, the smallest one stays at the end, so every time it can be popped first
                i-=1
            else:
                break
        self.elems.insert(i+1,e)
        
    def is_empty(self):
        return self.elems == []
            
    def checkPos(self,e):
        if self.is_empty() or e not in a:
            return None
        else:
            return self.elems.index(e)
    
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.elems.pop()
            
    def display(self):
        for ii in self.elems:
            print(ii, end = ' ')
        
        
        
if __name__=='__main__':
    
    '''
    q1 = LQueue()
    for ii in range(5):
        q1.enqueue(ii)

    q1.display_queue()

    print('dequeue it')
    for ii in range(3):
        q1.dequeue()
        q1.display_queue()
    '''
    
    q2 = PrioQue()
    for ii in range(5):
        q2.enqueue(ii)
    q2.display()
    print(' ')
    for ii in range(5):
        print(q2.dequeue(), end = " ")
    print(' ')
    
    
    
            
            
        
    