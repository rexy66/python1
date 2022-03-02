

portfolio = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def sumColumn(matrix, column):
    total = 0
    for row in range(len(matrix)):
        total += m[row][column]
    return total

column = 1
print("Sum of the elements in column", column, "is", sumColumn(portfolio, column))
