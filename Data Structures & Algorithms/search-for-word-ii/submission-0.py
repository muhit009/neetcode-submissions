class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur= cur.children[c]
        cur.isWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root  =  TrieNode()
        for word in words:
            root.addWord(word)
        
        R,C = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(row, col, node, word):
            if(row<0 or col<0 
                or row == R or col ==C or
                (row,col) in visit or board[row][col] not in node.children):
                return

            visit.add((row,col))
            node = node.children[board[row][col]]
            word+= board[row][col]
            if node.isWord:
                res.add(word)

            dfs(row+1, col, node, word)
            dfs(row-1, col, node, word)
            dfs(row, col+1, node, word)
            dfs(row, col-1, node, word)
            visit.remove((row,col))

        for r in range(R):
            for c in range(C):
                dfs(r,c,root, "")
        return list(res)