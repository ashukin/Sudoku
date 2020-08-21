#!/usr/bin/env python
# coding: utf-8

# In[57]:


import random
#checks the box 
def checkbox(r,c,var,a):
     for i in range (3):
        for j in range (3):
             if (a[r+i][c+j]==var): 
                return False
     return True
#checks row     
def checkr(row,num,a):
    for i in range(9):
        if (a[row][i] == num):
            return False
    return True
#checks column
def checkc(col,num,a):
    for i in range (9):
        if (a[i][col]==num):
            return False
    return True

#generates a solved sudoku board
def make_board():
    board = [[0 for _ in range(9)] for _ in range(9)]

    def search(c=0):
        i, j = divmod(c, 9)
        n=[1,2,3,4,5,6,7,8,9]
        random.shuffle(n)
        for x in n:
            if checkbox(i-(i%3),j-(j%3),x,board) and checkr(i,x,board)and checkc(j,x,board):
                board[i][j]=x
                if c + 1 >= 81 or search(c + 1):
                    return board
        else:
            # No number is valid in this cell: backtrack and try again.
            board[i][j] = None
            return None
    
    return search()
#checks empty cell locations
def empty(mat, row, col):
    for i in range(9):
        for j in range (9):
            if (mat[row][col] == 0):
                return True
    return False

# checking the possibilities of a no in a particular location by calling check_row(),check_col(),check_box() functions
def pos(mat, row, col, num):
    return checkr(row,num,mat) and checkc(col,num,mat) and checkbox(row-(row%3),col-(col%3),num,mat)and empty(mat, row, col)

#backtraces if the grid is solvable or not
def checkgrid(copy):
    d=solver(copy)
    for i in range(9):
        for j in range (9):
            if copy[i][j]==0:
                return False
    return True
#generates puzzle
def sudoku(level):
    mat=make_board()
    if level=='a':
        k=25
    if level=='b':
        k=35
    if level=='c':
        k=40
    if level=='d':
        k=50
    while k!=0:
        celll=random.randint(0,80)
        i = (celll//9); 
        j = celll%9; 
        if (j != 0): 
            j = j - 1; 
        if (mat[i][j] != 0):
            val=mat[i][j]
            mat[i][j] = 0
            k=k-1
            copy = []
            for r in range(0,9):
                copy.append([])
                for c in range(0,9):
                    copy[r].append(mat[r][c])
            if checkgrid(copy)is False:
                mat[i][j] = val
                k=k+1
    return mat
#SOLVER
def solver(board):
    a=0
    while (a!=10):
        for row in range(9):
            for col in range(9):
                for num in range(1, 10):
                    if (pos(board, row, col, num) and empty(board, row, col)):
                        c = 0
                        for i in range(9):
                            if i!=col:
                                if (pos(board, row, i, num)):
                                    c=1

                        if c == 0:
                            board[row][col]=num
        row = 0
        col = 0
        a+=1
    return board

#prints the grid
def printboard(mat):
    for i in range (0,9):
        print (mat[i])



print('CHALLENGE YOUR BRAIN CELLS!')  
level=input("ENTER DIFFICULTY LEVEL\na)EASY b)MEDIUM c)HARD d)EVIL")
board=sudoku(level)
print('PUZZLE:')
printboard(board)
x=input('DO YOU WANT THE SOLUTION? \n yes or no?')
if x=='yes':
    sol=solver(board)
    print('SOLUTION:')
    printboard(sol)



# In[ ]:





# In[ ]:




