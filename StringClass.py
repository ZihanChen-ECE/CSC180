#! /usr/bin/env python
#coding: -*- utf-8 -*-

#this is the kmp code for string match
import time

class StringMatching():
    
    def __init__(self, origin, target):
        self.target = target
        self.origin = origin
        
    def naive_matching(self, origin = None, target = None):
        if origin is None:
            origin = self.origin
        if target is None:
            target = self.target
        j,i = 0,0
        n,m = len(origin), len(target)
        while j<n and i<m:
            if origin[j] == target[i]:
                j+=1
                i+=1
            else:
                j = j-i+1
                i = 0
        if i==m:
            return j-i
        else:
            return -1
               
    
    def KMP_matching(self, origin = None, target = None, pnext = None):
        if origin is None:
            origin = self.origin
        if target is None:
            target = self.target
        if pnext is None:
            pnext = self.KMP_matching(target)
        j, i = 0,0
        n, m = len(origin), len(target)
        while j < n and i < m:
            if i == -1 or origin[j] == target[i]:
                j+=1
                i+=1
            else:
                j = pnext[i]
        if i == m:
            return j-i
        else:
            return -1
            
            
    def KMP_next(self, target = None):
        if target == None:
            target = self.target
        #find the pre/postfix
        i,m = 0, len(target)
        while i < m-1-i:
            if target[i] == target[m-1-i]:
                i+=1
            else:
                break
        pnext = [0]*m
        pnext[0] = -1
        j = 0
        while i-2>=0:
            pnext[m-j] = i-2
            i-=1
            j+=1
        return pnext
        """
        i, k, m = 0, -1, len(target)
        pnext = [-1]*m
        while i<m-1: #generate pnext[i+1]
            while k>=0 and  p[i]!=p[k]:
                k = pnext[k]
            i, k = i+1, k+1
            pnext[i] = k #set the pnext entry
        return pnext
        """
            

if __name__ == "__main__":
    origin = 'abcd123esdsgy347stasvgaeceaceadssftjaecaedscdsdsdsaecf'
    target = 'aecae'
    ST = StringMatching(origin, target)
    print('naively matching the two strings')
    s1 = time.time()
    print(ST.naive_matching())
    e1 = time.time()
    print('KMP matching the two strings')
    s2 = time.time()
    print(ST.naive_matching())
    e2 = time.time()
    
    elapsed1 = e1 - s1
    elapsed2 = e2 - s2
    
    print('naived matching took: ', elapsed1, 's')
    print('KMP matching took: ', elapsed2, 's')    
        
