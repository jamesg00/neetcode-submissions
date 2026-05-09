class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #brute force solution using i and j to iterate thru matrix and finding if its target 
        #o(n*m) time (m length of rows, n length of cols) || O(1) space (we dont create a lst or anyting)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target: 
                    return True
        return False 


        
