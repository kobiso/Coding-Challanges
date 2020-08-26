class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
        cur_focus = [-1, -1]
        sole_list = []
        pair_list = []
        max_len = 0
        
        for idx, val in enumerate(tree):
            if idx == 0:
                cur_focus[0] = val
                sole_list.append(val)
                pair_list.append(val)
            else:
                pre_val = tree[idx-1]
                if val == pre_val:
                    sole_list.append(val)
                    pair_list.append(val)
                else:
                    if val not in cur_focus:
                        if len(pair_list) > max_len:
                            max_len = len(pair_list)
                        cur_focus[0], cur_focus[1] = pre_val, val
                        pair_list = sole_list.copy()
                    pair_list.append(val)
                    sole_list = [val]
                            
        if len(pair_list) > max_len:
            max_len = len(pair_list)

        return max_len
        