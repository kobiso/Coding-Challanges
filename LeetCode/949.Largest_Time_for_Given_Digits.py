class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        for f in range(2, -1, -1):
            first, second, third, fourth = -1, -1, -1, -1
            temp = A.copy()
            
            # find first cand
            if f in temp:
                first = f
                temp.remove(f)
            else:
                continue

            # find second cand
            if f == 2:
                start = 3
            else:
                start = 9
            for i in range(start, -1, -1):
                if i in temp:
                    temp.remove(i)
                    second = i
                    break
            if second == -1:
                continue

            # find third cand
            for i in range(5, -1, -1):
                if i in temp:
                    temp.remove(i)
                    third = i
                    fourth = temp[0]
                    break
            if third == -1 or fourth == -1:
                continue
                
            if -1 not in [first, second, third, fourth]:
                break

        if -1 in [first, second, third, fourth]:
            return ""
        
        time_format = map(str, [first, second, ":", third, fourth])
        
        return ''.join(time_format)
