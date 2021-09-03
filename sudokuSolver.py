board = [
    [4,0,0,0,0,6,0,0,8],
    [0,0,9,0,0,1,6,0,5],
    [0,0,2,5,9,0,0,0,4],
    [0,0,0,0,6,5,0,3,1],
    [6,0,4,2,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,2,0,0,3,0,0,0,0],
    [0,0,0,0,0,0,0,8,0],
    [8,0,0,0,0,7,9,4,0]
]

def solve(board):

    find = findEmpty(board)
    if not find:
        return True
    else:
        row,col = find

    for i in range(1,10):
        if valid(board,i,(row,col)):
            board[row][col]=i

            if solve(board):
                return True
            board[row][col]=0
    return False

def valid(board,num,pos):

    # check row
    for i in range(len(board[0])):
        if board[pos[0]][i]==num and pos[1]!=i:
            return False

    # check column
    for i in range(len(board)):
        if board[i][pos[1]]==num and pos[0]!=i:
            return False

    # check cube
    cubeX = pos[1] // 3
    cubeY = pos[0] // 3

    for i in range(cubeY*3,cubeY*3+3):
        for j in range(cubeX*3,cubeX*3+3):
            if board[i][j]==num and (i,j) !=pos:
                return False

    return True

def printBoard(board):
    for i in range(len(board)):
        if i % 3 ==0 and i!=0:
            print("- - - - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 ==0 and j!=0:
                print(" | ", end ="")

            if j==8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ",end ="")


def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) # row,col = i,j

    return None


printBoard(board)
print("\n")
solve(board)
printBoard(board)