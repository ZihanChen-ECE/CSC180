#! /usr/bin/env python 
#-*- coidng:uft-8 -*-

import math
import sys
import copy

class Lab3():
    def __init__(self):
        self.pi = math.pi
        
        self.days= {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    def problem1(self):
        n_max = 1000
        sum = 0
        for n in range(n_max+1):
            sum += 4*pow(-1,n)/(2*n+1)
        print ('pi in problem1 is calculated as: ', sum)
        return sum
    
    def problem2(self,n,m):
        new_n, new_m, times = self.simplify_fractions(n,m)
        if new_n % new_m == 0:
            print (int(new_n / new_m))
        else:
            print(new_n, '/', new_m)
        print ('take', times,'loops')
        
        
    def problem3(self, n):
        n_max = sys.maxsize
        sum_value = 0
        for ii in range(n_max):
            sum_value += 4*pow(-1,ii)/(2*ii+1)
            error = abs(int(sum_value*(10**n))-int(self.pi*(10**n)))
            if error < 10:
                return sum_value, ii
        raise ValueError('reach maximum integer of the system')
        
    def simplify_fractions(self, n, m):
        min_value = min(m,n)
        GCD = 1
        count = 0
        for ii in range(2,min_value+1):
            count+=1
            if m % ii == 0 and n % ii == 0:
                if GCD < ii:
                    GCD = ii
        return int(n/GCD), int(m/GCD), count
        
    
    def problem4a(self, y, m, d):
        days = copy.deepcopy(self.days)
        new_y = 0
        new_m = 0
        new_d = 0
        
        if self.is_leap(y):
            days[2] = 30
            
        if d == days[m]:
            if m == 12:
                new_y = y+1
                new_m = 1
                new_d = 1
            else:
                new_y = y
                new_m = m+1
                new_d = 1
        else:
            new_y = y
            new_m = m
            new_d = d+1
            
        return new_y, new_m, new_d
        
        
            
    def is_leap(self,y):
        if y%4 !=0:
            return False
        else:
            if y % 100 ==0:
                if y%400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        
        
    def problem4b(self, fy, fm, fd, ty, tm, td):
        if not self.is_later(fy, fm, fd, ty, tm, td):
            raise SyntaxError('input sequence error')
        diff_days = 0
        days = copy.deepcopy(self.days)
        if fy == ty:
            if self.is_leap(fy):
                days[2] = 30

            for ii in range(fm, tm):
                diff_days += days[ii]
            diff_days = diff_days + td - fd
        else:
            if self.is_leap(ty):
                day[2] = 30
            for ii in range(1,tm):
                diff_days += days[ii]
            
            for ii in range(fy+1,ty):
                if self.is_leap(ii):
                    years_day = 366
                else:
                    years_day = 365
                diff_days += years_day
            
            if self.is_leap(fy):
                days[2] = 30
            for ii in range(fm,13):
                diff_days += days[ii]
            diff_days = diff_days + td - fd
            
            
        return diff_days
            
            
    def problem4b_easy(self, fy, fm, fd, ty, tm, td):
        if not self.is_later(fy, fm, fd, ty, tm, td):
            raise SyntaxError('input sequence error')
        count = 0
        y,m,d = fy,fm,fd
        while True:
            y,m,d = self.problem4a(y,m,d)
            count+=1
            if y == ty and m == tm and d == td:
                return count
            else:
                continue
                
            
        
        
    def is_later(self, fy, fm, fd, ty, tm, td):
        if ty < fy:
            return False
        elif ty == fy:
            if tm < fm:
                return False
            elif tm == fm:
                if td <= fd:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True
                
            
        
    def problem5(self,n,m):
        a = max(n,m)
        b = min(n,m)
        gcd, times = self.euclid_gcd(a,b)
        new_n,new_m = n/gcd,m/gcd
        if new_n % new_m == 0:
            print (int(new_n / new_m))
        else:
            print(int(new_n), '/', int(new_m))
        print ('take ', times, 'loops')
        
    def euclid_gcd(self,a,b,count = 0):
        if b==0:
            return a, count
        else:
            count+=1
            return self.euclid_gcd(b, a % b, count)
        
        
        
        
if __name__ == '__main__':
    p = Lab3()
    print('problem1: ')
    pi1 = p.problem1()
    print('problem2: ')
    p.problem2(220,135)
    print('problem3: ')
    pi3, n3 = p.problem3(5)
    print('by using ', n3, 'loops calculation pi reaches to: ', pi3)
    print('problem4a: ')
    y,m,d = p.problem4a(1900,12,31)
    print(y,'/',m,'/',d)
    print('problem4b: ')
    d1 = p.problem4b(1992,12,31,1993,3,17)
    d2 = p.problem4b_easy(1992,12,31,1993,3,17)
    print('traditional way: ', d1)
    print('easy way: ', d2)
    print('problem5: ')
    p.problem5(220,135)
    
    
    
    
    
    
    
    
    
    
    
    