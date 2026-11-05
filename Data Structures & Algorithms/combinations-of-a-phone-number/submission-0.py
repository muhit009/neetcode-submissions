class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        char_mapping = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        def backtrack(idx, curStr): # curStr will contain "123" - 1 for example
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for char in char_mapping[digits[idx]]: #so i went to the map, loop through every char for 2
                backtrack(idx+1,curStr + char)
        if digits:
            backtrack(0, "")
        return res

