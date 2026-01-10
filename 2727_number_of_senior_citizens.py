class Solution:
    def countSeniors(self, s: List[str]) -> int:
        count=0
        for i in s:
            a=int(i[11:13])          
       
            if a>60:
                count+=1
        return count