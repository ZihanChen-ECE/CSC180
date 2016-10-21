#! /usr/bin/env python
#-*- coding:utf-8 -*-

# this is the py code for 2nd lab

class Pocket_Calculator():
    
    def __init__(self):
        pass
        
    
    def initialize(self):
        self.current_value = 0
        self.prev_value = 0
        self.mem_value = 0
        
        
    def welcome(self):
        print('Welcome to the calculator program')
        print("The current value: ", self.current_value)

    def display_current_value(self):
        print('Current value: ', self.current_value)
        
    def save_value(self):
        self.prev_value = self.current_value
        
    def add(self, to_add):
        self.save_value()
        print('add', to_add, 'to current value')
        self.current_value += to_add
        
    def mult(self, to_mult):
        self.save_value()
        print('multiply',to_mult,'to current value')
        self.current *= to_mult
        
    def div(self, to_div):
        self.save_value()
        if to_div is 0:
            raise ValueError('The denominator is 0');
        else:
            print('current value is divided by', to_div)
            self.current_value /= to_div
            
    def memory(self):
        self.mem_value = self.current_value
        
    def recall(self):
        self.current_value = self.mem_value
        
    
    def undo(self):
        self.current_value, self.prev_value = self.prev_value, self.current_value
    
    
if __name__=='__main__':
        PC = Pocket_Calculator()
        PC.initialize()
        PC.welcome()
        PC.display_current_value()
        PC.add(2)
        PC.display_current_value()
        print('undo the operation')
        PC.undo()
        PC.display_current_value()
        print('undo the operation')
        PC.undo()
        PC.display_current_value()
        