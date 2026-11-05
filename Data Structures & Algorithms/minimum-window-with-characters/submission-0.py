class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT = {}
        windows = {}
        for char in t:
            countT[char] = 1+ countT.get(char, 0)
        
        have,need = 0, len(countT)
        res,resLen = [-1,-1], float("infinity") 
        l = 0
        for  r in range(len(s)):
            cur = s[r]
            windows[cur] = 1+ windows.get(cur, 0)
            if cur in countT and windows[cur] == countT[cur]:
                have = have + 1
            while have == need:
                # we need to update the result
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                # pop from the left
                windows [s[l]] -= 1
                # check if we need to change from have
                if s[l] in countT and windows[s[l]] < countT[s[l]]:
                    have -=  1
                l = l+1
        l,r = res
        return s[l:r+1] if resLen != float('infinity') else ""
