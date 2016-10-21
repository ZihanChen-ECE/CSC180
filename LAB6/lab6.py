#! /usr/bin/env python3
#-*- coding:utf-8 -*-

'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random

Marks = ['X','O']
    
def input_pos_for_1(ii):
    input_value = input('player %s, Enter your move: ' % str(ii%2+1))
    while ord(input_value)<49 or ord(input_value)>57:
        input_value = input('Invalid position, re-enter your move: ')
    square_num = int(input_value)
    return square_num

def input_pos_for_2(ii):
    input_value = input('player 1, Enter your move: ')
    while ord(input_value)<49 or ord(input_value)>57:
        input_value = input('Invalid position, re-enter your move: ')
    square_num = int(input_value)
    return square_num

def coord_pos(square_num):
    row = ((square_num - 1) // 3)
    col = ((square_num - 1) % 3)
    coord = [row, col]
    return coord

def put_in_board(board, mark, square_num):
    coord = coord_pos(square_num)
    if board[coord[0]][coord[1]] == ' ':
        board[coord[0]][coord[1]] = mark
        return board
    else:
        return False


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
    
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    
def full_board(board):
    for ii in board:
        for jj in ii:
            if jj == ' ':
                return False
    return True
                

def M_dim(M):
    row = len(M)
    col = len(M[0])
    return row, col

def check_row(board):
    for ii in board:
        if ii[0] in Marks and ii[0] == ii[1] and ii[0] == ii[2]:
            return ii[0]
    return -1

def check_col(board):
    T_board = zip(*board)
    for ii in T_board:
        if ii[0] in Marks and ii[0] == ii[1] and ii[0] == ii[2]:
            return ii[0]
    return -1
    
def check_diag(board):
    row, col = M_dim(board)
    
    piv1 = board[0][0]
    piv2 = board[0][2]
    flag1 = True
    flag2 = True
    if piv1 == ' ':
        flag1 = False
    else:
        for ii in range(1,3):
            if board[ii][ii] != piv1:
                flag1 = False
                break
    if piv2 == ' ':
        flag2 = False
    else:
        for ii in range(1,3):
            if board[ii][row-ii-1] != piv2:
                flag2 = False
                break
    
    if flag1 == False and flag2 == False:
        return -1
    
    elif flag1 == True:
        return piv1
        
    else:
        return piv2
    

def examine_condition(board):
    row = check_row(board)
    col = check_col(board)
    diag = check_diag(board)
    if row == -1 and col == -1 and diag == -1:
        return -1
    elif row != -1:
        return row
    elif col != -1:
        return col
    else:
        return diag

def problem1(board):
    print('welcome to the game!')
    print('\n let\'s play with friend!')
    board = make_empty_board()
    ii = 0

    player_dict = {'X':1,'O':2}
    print_board_and_legend(board)
    while True:
        square_num = input_pos_for_1(ii)
        while (put_in_board(board, Marks[ii%2],square_num)) == False:
            print('This position is already occupied, choose another place')
            square_num = input_pos_for_1(ii)
        #board = put_in_board(board, mark[ii%2],square_num)
        ii+=1
        print_board_and_legend(board)
        result = examine_condition(board)
        if result != -1:
            print ('playder %s wins! game over!' % str(player_dict[result]))
            break
        
        else:    
            if full_board(board):
                print('Draw, game over')
                break


def get_free_squares(board):
    row, col = M_dim(board)
    newList = []
    subList = []
    for ii in range(row):
        for jj in range(col):
            if board[ii][jj] == ' ':
                subList = [ii,jj]
                newList.append(subList)
    return newList

def make_random_move(board, posList):
    pos = int(len(posList) * random.random())
    coord = posList[pos]
    board[coord[0]][coord[1]] = 'O'
    return board
    

    
def problem2(board):
    print('welcome to the game!')
    print('\n let\'s play with computer!!')
    board = make_empty_board()
    ii = 0

    player_dict = {'X':1,'O':2}
    print_board_and_legend(board)
    while True:
        square_num = input_pos_for_2(ii)
        while (put_in_board(board, Marks[0],square_num)) == False:
            print('This position is already occupied, choose another place')
            square_num = input_pos_for_2(ii)
        #board = put_in_board(board, mark[ii%2],square_num)
        ii+=1
        print_board_and_legend(board)
        result = examine_condition(board)
        if result != -1:
            if result == 'O':
                print ('Computer wins! Game Over!')
            else:
                print ('You win! Congratulations!')
            break
        
        else:    
            if full_board(board):
                print('Draw, game over')
                break
        print('Computer\'s move')
        board = make_random_move(board, get_free_squares(board))
        print_board_and_legend(board)
        result = examine_condition(board)
        if result != -1:
            if result == 'O':
                print ('Computer wins! Game Over!')
            else:
                print ('You win! Congratulations!')
            break
        
        else:    
            if full_board(board):
                print('Draw, game over')
                break        
            
            

def make_move(board):
    newboard = board[:]
    newPos = get_free_squares(newboard)
    coord = [0,0]
    flag = False
    for ii in newPos:
        newboard[ii[0]][ii[1]] = 'O'
        result = examine_condition(board)
        if result == 'O':
            coord = ii
            flag = True
            break
        newboard[ii[0]][ii[1]] = ' '
    if flag == True:
        board[coord[0]][coord[1]] = 'O'
    else:
        board = make_random_move(board, get_free_squares(board))
    return board
            
def problem3(board):
    print('welcome to the game!')
    print('\n let\'s play with computer (medium)!!')
    board = make_empty_board()
    ii = 0

    player_dict = {'X':1,'O':2}
    print_board_and_legend(board)
    while True:
        square_num = input_pos_for_2(ii)
        while (put_in_board(board, Marks[0],square_num)) == False:
            print('This position is already occupied, choose another place')
            square_num = input_pos_for_2(ii)
        #board = put_in_board(board, mark[ii%2],square_num)
        ii+=1
        print_board_and_legend(board)
        result = examine_condition(board)
        if result != -1:
            if result == 'O':
                print ('Computer wins! Game Over!')
            else:
                print ('You win! Congratulations!')
            break
        
        else:    
            if full_board(board):
                print('Draw, game over')
                break
        print('Computer\'s move')
        board = make_move(board)
        print_board_and_legend(board)
        result = examine_condition(board)
        if result != -1:
            if result == 'O':
                print ('Computer wins! Game Over!')
            else:
                print ('You win! Congratulations!')
            break
        
        else:    
            if full_board(board):
                print('Draw, game over')
                break          

if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)    
    
    print("\n\n")
    
    board = [["O", "X", "X"],
             [" ", "X", " "],
             [" ", "O", " "]]
    
    print_board_and_legend(board)
    
    problem3(board)