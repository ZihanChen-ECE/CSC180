#! /usr/bin/env python
from calculator import *


def count_evens(L):
    even_list =[]
    for x in L:
        if x % 2 == 0:
            even_list.append(x)
    return len(even_list)
    
    
def list_to_str(lis):
    s = ''
    for ii in lis:
        s+= str(ii)
    return s
    
def lists_are_the_same(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    if len1 != len2:
        return False
    else:
        for ii in range(len1):
            if list1[ii] != list2[ii]:
                return False
        return True
        
        
if __name__ == '__main__':
    cmd = ['initialize','add','subtract']
    for ii in cmd:
        s = ''
        if ii == 'initialize':
            s += ii +'()'
        else:
            value = input('input a number:')
            s += ii +'('+value+')'
            eval(s)
            test = 0
    
    print(get_current_value())
        
    
    """
    L1 = [1,3,5,7,9]
    L2 = [1,3,5,7,9]
    print(count_evens(L1))
    print(list_to_str(L1))
    print(lists_are_the_same(L1, L2))
    """
    
    