#! /usr/bin/env python
#-*- coding:utf-8 -*-

#p1
def list1_start_with_list2(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    if len1<len2:
        return False
    if list1[len2]==list2[0]:
        return True
    return False
    
#p2
def match_pattern(list1,list2):
    len1 = len(list1)
    len2 = len(list2)
    if len1<len2:
        return False
    ii = 0
    while ii < len1:
        if list1[ii] == list2[0]:
            if list1[ii:ii+len2] == list2[:]:
                return True
        ii+=1
    return False
    
    
#p3
def duplicate(List):
    len1 = len(List)
    ii = 0
    while ii < len1-1:
        if List[ii] == List[ii+1]:
            return True
        ii+=1
    return False
        

#p4
def print_matrix_dim(M):
    row = 0
    col = 0
    for ii in M:
        row+=1
    col = len(ii)
    print('%dx%d' % (row, col))
    return row, col
            

def mult_M_v(M,v):
    row, col = print_matrix_dim(M)
    l1 = len(v)
    newL = []
    if col != l1:
        raise ValueError('dimension dismatch')
        return None
    for ii in M:
        newL.append(sum([x*y for x,y in zip(ii,v)]))
    return newL    
            

#p5
class part5:
    def __init__(self):
        pass
    
    def input_M(self,M):
        self.M = M
    
    def part_a(self):
        for ii in self.M:
            print(ii)
            
    def part_b(self):
        for ii in self.M:
            print(ii[1])

    def part_c(self):
        return sum([ii[-1] for ii in self.M])

    def part_d(self):
        count = 0
        for ii in self.M:
            if ii[1] == 'dog':
                count+=1
        return count
        

if __name__ == '__main__':
    """
    l1 = [3,4,5]
    l2 = [4,5]
    print(match_pattern(l1,l2))
    """
    """
    l1 = [3,4,5,6]
    print(duplicate(l1))            
    """
    """
    M = [[1,2],[3,4],[5,6]]
    print_matrix_dim(M)
    """
    """
    M = [[1,2,3],[4,5,6]]
    v = [1,2,3]
    print(mult_M_v(M,v))
    """
    pets = [["Shoji", "cat", 18],
        ["Hanako", "dog", 15],
        ["Sir Toby", "cat", 10],
        ["Sachiko", "cat", 7],
        ["Sasha", "dog", 3],
        ["Lopez", "dog", 13]]
    p5 = part5()
    p5.input_M(pets)
    p5.part_a()
    p5.part_b()
    print(p5.part_c())
    print(p5.part_d())
    
    
    
    
    
    
    
    
    