class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        matrix.reverse()

        row = len(matrix)
        col = len(matrix[0])

        #transpose then swap matrixes indexes

        for i in range(row):
            for j in range(i, col):
                
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]





                

'''
  [1,2,3],
  [4,5,6],
  [7,8,9]


  [7,8,9],
  [4,5,6],
  [1,2,3]

  [7,4,1],
  [8,5,2],
  [9,6,3]


'''


        