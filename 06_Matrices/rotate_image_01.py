# # Approarch
# "90 degree" is consist of two operations
# - transpose
# - reverse rows

from typing import List


def rotate_image(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix:
        return [[]]
    
    m = len(matrix)
    n = len(matrix[0])

    # transpose the matrix
    for i in range(m):
        for j in range(n):
            if i < j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # reverse rows
    for i in range(m):
        left, right = 0, n - 1
        while left < right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left] 
            left += 1
            right -= 1
    
    return matrix


def main():
    matrix = [
        [1, 2],
        [3, 4]
    ]
    print("before: ")
    print(matrix)

    result = rotate_image(matrix)
    print("after: ")
    print(result)


if __name__ == "__main__":
    main()