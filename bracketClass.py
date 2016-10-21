#! /usr/bin/env python

#this code is for examing the match of brackets pair

import StackClass as SC

class BracketPair():
    def __init__(self):
        self.text = []

    def check_brackets(self, text):
        self.text = text
        self.brackets = "{[()]}"
        self.open_brackets = "{[("
        self.opposite_brackets = {")":"(", "]":"[", "}":"{"}
        ST = SC.SStack()
        for pr in self.find_brackets(self.text):
            if pr in self.open_brackets:
                ST.push(pr)
            elif self.opposite_brackets[pr] != ST.pop():
                print('dismatch')
                return False
                
        print('matches perfectly')
        return True
        
        
        
    def find_brackets(self, text):
        text_brackets, pos = [], []
        for ii in text:
            if ii in self.brackets:
                text_brackets.append(ii)
                #pos.append(text.index(ii))
        return text_brackets
        
        
    
if __name__ == '__main__':
    text = "{5*(3+[13-5])}"
    BR = BracketPair()
    print(BR.check_brackets(text))
        
        
        
