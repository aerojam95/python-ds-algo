# This function takes the argument of a n x n 2D matrix representing an image,
# rotate the image by 90 degrees (clockwise). It rotates the image 
# in-place, which means that is had to modify the input 2D matrix directly.
# This does not allocate another 2D matrix and do the rotation.

# Written by JAM
# 21-08-2023

# Arguments:
# matrix: nxn 2D array


def rotateMatrix(matrix: list):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
             # transpose matrix by element swapping
             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Correct row elments but in reverse order
    for row in matrix:
        row.reverse()

    print(matrix)
    


rotateMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]])