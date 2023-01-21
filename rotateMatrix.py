'''

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''

class Solution(object):
    def rotate(self, matrix):
       #transpose the matrix then reverse
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
                
        #reverse each row simulteneously
        for row in matrix:
            row.reverse()
            
        return matrix
    
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        
#best time
# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)

        # anti-diagonal mirror
        for i in xrange(n):
            for j in xrange(n - i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]

        # horizontal mirror
        for i in xrange(n / 2):
            for j in xrange(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

        return matrix

# Time:  O(n^2)
# Space: O(n^2)
class Solution2(object):
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        return [list(reversed(x)) for x in zip(*matrix)]
      
      
      
 #least space solution
class Solution(object):
    def rotate(self, matrix):
        def conv_cart(i, j, l):
            return i-l/2, j-l/2

        def conv_ind(i, j, l):
            return int(i+l/2) - (i>0 and l%2==0), int(j+l/2) - (j>0 and l%2==0)
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for i in range(l//2):
            for j in range(l//2 + l%2):
                rot_i, rot_j = conv_cart(i, j, l)
                print(rot_i)
                print(rot_j)
                replacement = matrix[i][j]
                for n in range(5):
                    rot_i_ind, rot_j_ind = conv_ind(rot_i, rot_j, l)
                    print(rot_i_ind)
                    print(rot_j_ind)
                    saved = matrix[rot_i_ind][rot_j_ind]
                    matrix[rot_i_ind][rot_j_ind] = replacement
                    print(matrix)
                    replacement = saved
                    rot = -rot_i
                    rot_i = rot_j
                    rot_j = rot
        return matrix
