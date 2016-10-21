#! /usr/bin/env python

def trunctation(string1, substring1, i, substring2):
    if string1.find(substring1, i) is -1:
        raise ValueError
    j = 0
    pos = 0
    subpos = 0
    while j<i:
        subpos = string1[pos:].find(substring1)
        pos +=subpos
        j+=1
        
    pos = string1.find(substring1,i)
    newpos = pos+len(substring1)
    
    newstring = string1[:newpos]+substring2
    return newstring


if __name__=='__main__':
    string1 = "today i will study and eat and sleep"
    substring1 = 'nd'
    i = 2
    substring2 = ' study some more'
    print (trunctation(string1, substring1, i, substring2))