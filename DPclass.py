#! /usr/bin/env python

def Coins(N):
    return _coins(N)
    
def _coins(ii):
    if ii == 0:
        return 0
    elif ii >=1 and ii < 3:
        return _coins(ii-1)+1
    elif ii>=3 and ii < 5:
        return min(_coins(ii-1)+1, _coins(ii-3)+1)
    else:
        return min(_coins(ii-1)+1, _coins(ii-3)+1, _coins(ii-5)+1)




if __name__=='__main__':
    for  ii in range(30):
        print (Coins(ii))
    
    
    