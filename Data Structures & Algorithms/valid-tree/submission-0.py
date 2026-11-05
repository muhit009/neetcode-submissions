class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #valid tree means no cycle and all nodes are connected
        adj = {i: [] for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visit = set()
        
        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for neighbors in adj[node]:
                if neighbors == prev:
                    continue
                if not dfs(neighbors, node):
                    return False
            return True
        
        return dfs(0, -1 ) and len(visit) == n

        