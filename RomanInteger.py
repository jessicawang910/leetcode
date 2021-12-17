class Solution:
    def romanToInt(self , s: str) -> int:
        map = {'I': 1 ,
               'V': 5 ,
               'X': 10 ,
               'L': 50 ,
               'C': 100 ,
               'D': 500 ,
               'M': 1000
               }

        Nums = [ map[ ele ] for ele in list(s) ]
        sum = 0
        pos = 0
        while pos < len(s):
            if pos == len(s)-1:
                sum += Nums[pos]
                return sum
            elif (Nums[ pos + 1 ] // Nums[ pos ] in [ 5 , 10 ]):
                sum += Nums[ pos + 1 ] - Nums[ pos ]
                pos += 2
            else:
                sum += Nums[ pos ]
                pos += 1

        return sum


obj = Solution()
print(obj.romanToInt('III'))