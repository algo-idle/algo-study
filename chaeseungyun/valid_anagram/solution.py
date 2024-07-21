class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dictOfS= {}
        dictOfT = {}

        if (len(s) != len(t)): return False

        for item in s:
            if (item in dictOfS): dictOfS[item] += 1
            else: dictOfS[item] = 1

        for item in t:
            if (dictOfS.get(item) == None): return False
            if (item in dictOfT): dictOfT[item] += 1
            else: dictOfT[item] = 1

        keyOfT = list(dictOfT.keys())

        for item in keyOfT:
            if (dictOfS.get(item) == None): return False
            if (dictOfS[item] != dictOfT[item]): return False

        
        return True