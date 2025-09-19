def play_sudoku():
    board = generate_sudoku()  # 스도쿠 퍼즐을 생성
    print("스도쿠 게임을 시작합니다!")
    print_board(board)

    while True:
        # 사용자가 입력한 값으로 행, 열, 숫자를 받음
        try:
            row = int(input("행을 입력하세요 (1-9): ")) - 1
            col = int(input("열을 입력하세요 (1-9): ")) - 1
            num = int(input("숫자를 입력하세요 (1-9): "))

            # 유효한 입력인지 확인
            if not (0 <= row <= 8 and 0 <= col <= 8 and 1 <= num <= 9):
                print("잘못된 입력입니다. 1에서 9 사이의 숫자를 입력하세요.")
                continue

            if board[row][col] != 0:
                print("이미 값이 입력된 칸입니다.")
                continue

            # 숫자가 해당 위치에 올바르게 입력될 수 있는지 확인 (검증)
            if is_valid(board, row, col, num):
                board[row][col] = num  # 입력한 숫자를 보드에 반영
                print_board(board)

                # 스도쿠가 완성되었는지 확인
                if not find_empty_location(board): # 빈 곳을 못 찾으면!
                    print("축하합니다! 스도쿠를 완성했습니다.")
                    break
            else:
                print("잘못된 이동입니다. 게임을 종료합니다.")
                break
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")

# 프로그램 실행
play_sudoku()