class Solution:

    def romanToInt(self, s:str) -> int:
        s = s.upper()
        
        longitud = len(s)
        num:int  = self.romanValue(s[0]) if longitud > 0 else 0
        
        for indice in range(1,longitud ):
            num1 = self.romanValue(s[indice - 1])
            num2 = self.romanValue(s[indice])
            
            if num2 > num1:
                num += num2 - 2 * num1 
            else:
                num += num2         
           
        return num
    
    def romanValue(self,roman):
        return {
            'I': 1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
            }.get(roman,0)