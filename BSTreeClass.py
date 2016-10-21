#! /usr/bin/env python
#-*- coidng:utf-8 -*-

import random
from collections import deque

class BiTNode():
    def __init__(self, elm, lchild, rchild,parent):
        self.elem = elm
        self.lchild = lchild
        self.rchild = rchild
        self.parent = parent


class BSTree():
    
    def __init__(self):
        self.root = None      

    def find_elem(self, elm):
        p =  self._find_elem(elm,self.root)
        if p == None:
            return False
        else:
            return True


    def _find_elem(self,elm,root):
        if root == None:
            return None
        if root.elem == elm:
            return root
        elif root.elem > elm:
            return self._find_elem(elm, root.lchild)
        else:
            return self._find_elem(elm,root.rchild)            
    
    def append(self,elm):
        if self.root == None:
            self.root = BiTNode(elm, None, None, None)
        else:
            self._append(elm, self.root)
    
    
    def _append(self,elm,root):
        if root == None:
            return False
        elif root.elem == elm:
            return False
        elif elm < root.elem:
            if root.lchild == None:
                root.lchild = BiTNode(elm, None, None, root)
            else:
                self._append(elm, root.lchild)
        else:
            if root.rchild == None:
                root.rchild = BiTNode(elm, None, None, root)
            else:
                self._append(elm, root.rchild)
                
    def count_Nodes(self):
        return self._count_BiTNodes(self.root)            
    
    def _count_BiTNodes(self, t):
        if t is None:
            return 0
        else:
            return 1 + self._count_BiTNodes(t.lchild) + self._count_BiTNodes(t.rchild) #DFS
    
    def sum_Nodes(self):
        return self._sum_BiTNodes(self.root)
    
    def _sum_BiTNodes(self, t):
        if t is None:
            return 0
        else:
            return t.elem + self._sum_BiTNodes(t.lchild) + self._sum_BiTNodes(t.rchild) #DFS
    def preOrder(self):
        self.preOrderTraverse(self.root)
        print('')
        
    def preOrderTraverse(self, t):
        if t is None:
            return None
        else:
            print(t.elem, end = " ")
            self.preOrderTraverse(t.lchild)
            self.preOrderTraverse(t.rchild)
    
    def inOrder(self):
        self.inOrderTraverse(self.root)
        print('')
        
    def inOrderTraverse(self, t):
        if t is None:
            return None
        else:
            self.inOrderTraverse(t.lchild)
            print(t.elem, end = " ")
            self.inOrderTraverse(t.rchild)
            
    def postOrder(self):
        self.postOrderTraverse(self.root)
        print('')
        
    
    def postOrderTraverse(self, t):
        if t is None:
            return None
        else:
            self.postOrderTraverse(t.lchild)
            self.postOrderTraverse(t.rchild)
            print(t.elem, end = " ")
            
    def find_root(self):
        if self.root == None:
            return None
        else:
            return self.root.elem    
      
                
    def delete(self,elm):
        p = self._find_elem(elm,self.root)
        if p == None:
            print('element not in the Tree')
            return None
        else:
            if p.lchild == None and p.rchild == None:
                if p == self.root:
                    self.root = None
                else:
                    if p == p.parent.lchild:
                        p.parent.lchild = None
                    else:
                        p.parent.rchild = None
                    p = None
            elif p.lchild == None or p.rchild == None:
                if p.lchild != None:
                    child = p.lchild
                else:
                    child = p.rchild
                if p == self.root:
                    self.root = child
                    p = None
                else:
                    t = p.parent
                    if t == None:
                        self.root = child
                        p = None
                    else:
                        if p == t.lchild:
                            t.lchild == child
                            child.parent = t
                            p = None
                        else:
                            t.rchild == child
                            child.parent = t
                            p = None
            else:
                Predessor = self._predecessor(p.elem)
                value = Predessor.elem
                self.delete(value)
                p.elem = value
            
            return True    
                
    
    def find_min(self):
        if self.root == None:
            return  None
        else:
            return self._find_min(self.root).elem
            
            
            
    def _find_min(self, root):
        if root == None:
            return None
        else:
            p = root
            while p.lchild!=None:
                p = p.lchild
            return p
    
    def find_max(self):
        if self.root == None:
            return None
        else:
            return self._find_max(self.root).elem
            
    def _find_max(self, root):
        if root == None:
            return None
        else:
            p = root
            while p.rchild!=None:
                p = p.rchild
            return p
    
    
    def predecessor(self,elm):
        p = self._predecessor(elm)
        if p!=None:
            return p.elem
        else:
            return None
            
    
    def _predecessor(self,elm):
        p = self._find_elem(elm,self.root)
        if p == None:
            return None
        else:
            if p.lchild!=None:
                return self._find_max(p.lchild)
            else:
                ST = deque()
                p = self.root
                if p.elem == elm:
                    return None
                else:
                    while True:
                        if elm < p.elem:
                            p = p.lchild
                        elif elm > p.elem:
                            ST.append(p)
                            p = p.rchild
                        else:
                            break
                if ST:
                    return ST.pop()
                else:
                    p = self.root
                    
    

if __name__ == '__main__':
    t = BSTree()    
    for ii in [10,4,7,5,9]:
        t.append(ii)
    print('node num:')
    print(t.count_Nodes())
    print('node sum:')
    print(t.sum_Nodes())
    print('preOrder: ')
    t.preOrder()
    print('inOrder:')
    t.inOrder()
    print('postOrder: ')
    t.postOrder()
    print('delete:')
    for ii in [10,4,7,5,9]:
        t.delete(ii)
        t.inOrder()

    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
        