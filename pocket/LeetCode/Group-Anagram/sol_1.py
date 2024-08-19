class Solution:
    def groupAnagrams(self, strs):
        res = {}
        for _str in strs:
            key = ''.join(list(sorted(_str)))
            try:
                res[key].append(_str)
            except:
                res[key] = [_str]
        return list(res.values())