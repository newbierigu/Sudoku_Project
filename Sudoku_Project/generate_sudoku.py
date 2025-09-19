import random

def generate_sudoku():
    puzzle = []

    numbers = [0] * 9 + list(range(1,10))

    for _ in range(9): # 행 9개
        row = []
        for _ in range(9): # 열 9개

            rand_int = random.choice(numbers)
            row.append(rand_int)
        puzzle.append(row)
    return puzzle