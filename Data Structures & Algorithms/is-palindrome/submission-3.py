class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return True
            
        filtered_list = []
        
        for c in s:
            if ord(c)>=ord('a') and ord(c)<=ord('z'):
                filtered_list.append("c"+str(ord(c)))
            if ord(c)>=ord('A') and ord(c)<=ord('Z'):
                filtered_list.append("c"+str(ord(c.lower())))
            if ord(c)>=ord('0') and ord(c)<=ord('9'):
                filtered_list.append("n"+str(ord(c)))
        
        i = 0
        j = len(filtered_list)-1
        while i<=j:
            if filtered_list[i] != filtered_list[j]:
                return False
            i += 1
            j -= 1
        return True