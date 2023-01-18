'''


'''

#my solution
class Solution(object):
    def plusOne(self, digits):
        result=''.join([str(i) for i in digits])
        addition=int(result)+1 
        results=list(map(int,[x for x in str(addition)]))
        
        return results
      
      
#best timing
class Solution(object):
    def plusOne(self, digits):
        result=''.join([str(i) for i in digits])
        addition=int(result)+1 
        results=list(map(int,[x for x in str(addition)]))
        
        return results
      
      
#best memory management
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
    #    [1,2,3,9] = [1,2,4,0]
    #    [9,9,9] = [1,0,0,0]
    #    [9]
        tail = len(digits)-1
        while tail>=0:
            if digits[tail]==9:
                digits[tail]=0
                tail-=1
            else:
                digits[tail]+=1
                break
        if tail==-1:
            return [1]+digits
        else:
            return digits
