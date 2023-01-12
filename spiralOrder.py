'''

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:



'''
class Solution(object):
    def spiralOrder(self, matrix):
        results=[]
        while matrix:
            #pop(0) is use to subtract the first value values and append them to temporary created store
            
            #adding content of row1 the delete them completely
            results+=matrix.pop(0)
            
            #iterating and popping the last digit on the remaining rows
            if matrix and matrix[0]:
                for l in matrix:
                    results.append(l.pop())
                    
            ##adding the last diit in reverse order        
            if matrix:
                results+=matrix.pop()[::-1]
                
                #popping the first line
            if matrix and matrix[0]:
                for l in matrix[::-1]:
                    results.append(l.pop(0))
                    
        return results
                
            
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
