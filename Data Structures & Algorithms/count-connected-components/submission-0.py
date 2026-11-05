class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 0-1-2 connected and 3-4 connected (op:2)
        # create a adjacency list
        adj = {i: [] for i in range(n)}
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visit = set()
        count = 0
        def dfs(node):
            for nei in adj[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)
            

        for node in range(n):
            if node not in visit:
                visit.add(node)
                dfs(node)
                count = count+1
        return count
        
