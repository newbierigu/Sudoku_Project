def print_board(board):
    for row in board:
        print(" ".join(map(str, row)), end="\n")

def is_valid(board, row, col, num): # 3가지 규칙 체크 함수
    # 1. 행에 중복된 숫자가 있는지
    if num in board[row]:
        return False

    # 2. 열에 중복된 숫자가 있는지
    if num in [board[i][col] for i in range(9)]:
        return False

    # 3. 3x3 박스에 중복된 숫자가 있는지
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for r in range(start_row, start_row+3):
        for c in range(start_col, start_col+3):
            if board[r][c] == num:
                return False
    return True

def find_empty_location(board): # 빈 칸을 찾는 함수
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None

def solve_sudoku(board):
    # 빈 위치 찾기
    empty_loc = find_empty_location(board)

    if not empty_loc:
        return True # 다 푼 경우
    
    row, col = empty_loc

    for num in range(1,10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            ##### 재귀(recursive) 함수 #####
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0 # 무르기 <- 풀 수 없는 스도쿠가 입력으로 들어올 수 있기 때문
        
        return False