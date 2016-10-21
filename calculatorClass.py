#! /usr/bin/env python

#this script is for calculating the suffix expression

import StackClass as SS
    

class suffixExpression():
    def __init__(self):
        self.text = None
        
    def read_text(self, text):
        self.text = text
        if self.text == None:
            return False
        else:
            return True
            
    def calculate(self, text = None):
        if text == None:
            self.suffix_text = self.in_to_surffix()
            text = self.suffix_text
        length = len(text)
        ST = SS.SStack()
        operator = "+-*/"
        for ii in text:
            if ii not in operator:
                ST.push(ii)
                continue    #continue will neglect the following codes and jump to the next loop
            else:    
                if ST.depth()<2:
                    raise SyntaxError('short of operand(s)')
                
                a = int(ST.pop())
                b = int(ST.pop())
                c = 0.0
                if ii == '+':
                    c = b+a
                elif ii == '-':
                    c = b-a
                elif ii == '*':
                    c = b*a
                else:
                    c = b/a if a!=0 else print ('a can\'t be 0')
                ST.push(c)
        if ST.depth() == 1:
            return ST.pop()
        else:
            raise SyntaxError('extra operand(s)')
            
    def show_surffix(self, text = None):
        if text ==  None:
            text = self.text
        self.suffix_text = self.in_to_surffix(text)
        print(self.suffix_text)
            
    def in_to_surffix(self, text = None):
        if text == None:
            text = self.text
        exp = []
        operator = {'+':1, '-':1, '*':2, '/':2}
        parenthese = '([{}])'
        open_parenthese = '([{'
        ST = SS.SStack()
        for ii in text:

            if (ii not in operator) and (ii not in parenthese):
                exp.append(ii)
            elif ii in operator:
                if (ST.is_empty()) or (ST.top() not in open_parenthese and operator[ii] > operator[ST.top()]):
                    ST.push(ii)
                else:
                    while (not ST.is_empty()) and (ST.top() not in open_parenthese and operator[ii] <= operator[ST.top()]) and (ST.top() not in parenthese):
                        value = ST.pop()
                        exp.append(value)            
                    ST.push(ii)
            elif ii == '(':
                ST.push(ii)
            elif ii is ')':
                while not ST.is_empty() and ST.top() !='(':
                    value = ST.pop()
                    exp.append(value)
                if ST.is_empty():
                    raise SyntaxError('parenthese not match')
                else:
                    ST.pop() #pop the '('
            else:
                #raise SyntaxError ('operand or number: %s is illegal', ii)
                pass
        while not ST.is_empty():
            exp.append(ST.pop())
        
        return exp
        
                
        
        
            
if __name__=="__main__":
    row_text = " 4 + 5 * ( 3 + 1 ) / 2 - 3"
    text = row_text.split()
    calculator = suffixExpression()
    calculator.read_text(text)
    calculator.show_surffix()
    print(calculator.calculate())
                
            
    