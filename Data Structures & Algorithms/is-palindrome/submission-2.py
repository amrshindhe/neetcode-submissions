class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return True
            
        filtered_list = []
        
        for c in s:
            if "a" <= c <= "z":
                filtered_list.append(c)
            elif "A" <= c <= "Z":
                filtered_list.append(c.lower())
            elif "0" <= c <= "9":
                filtered_list.append(c)
        
        i = 0
        j = len(filtered_list)-1
        while i<=j:
            if filtered_list[i] != filtered_list[j]:
                return False
            i += 1
            j -= 1
        return True