#! /usr/bin/env python
#-*- coding:uft-8 -*-

#This script is for solving the knapsack problem (np problem) via recursion

class KnapsackSolver():
    def __init__(self, weight, wlist,n):
        self.weight = weight
        self.wlist = wlist
        self.n = n
        
    def knap_rec(self, weight, wlist, n):        
        if weight == 0:
            return True
        elif weight < 0 or (weight>0 and n<1):
            return False
        elif self.knap_rec(weight - wlist[n-1], wlist, n-1):
            print('item'+str(n)+':', wlist[n-1])
            return True
        elif self.knap_rec(weight, wlist, n-1):
            return True
        else:
            return False


if __name__ == '__main__':
    weight = 4
    wlist = [1,2,3]
    n = 3
    kp = KnapsackSolver(weight, wlist, n)
    print(kp.knap_rec(weight, wlist, n))
    
    
        