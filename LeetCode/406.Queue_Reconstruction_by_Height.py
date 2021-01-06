class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        res = [None] * len(people)
        people.sort()
        print (res)
        
        print (people)

        n_range = range(len(people))
        for pair in people:
            count = -1
            for i in n_range:
                if res[i] is None or res[i][0] >= pair[0]:
                    count += 1
                else:
                    continue
                if count == pair[1]:
                    res[i] = pair
                    break
        return res