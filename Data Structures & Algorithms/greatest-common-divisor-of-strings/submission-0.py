class Solution:
    def getGcd(self, n1, n2):
        a = n1
        b = n2

        while True:
            if a == 0:
                return b
            
            if b == 0:
                return a
            
            a, b = b, a%b
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        gcd = self.getGcd(len(str1), len(str2))
        return str1[:gcd]
        