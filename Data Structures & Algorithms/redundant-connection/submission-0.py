class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # so try to union both root
        # find both roots
        # same root? already connected so cylcle, return
        # diff root? safe to add, merge - continue
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1]*(n+1)
        def find(node):
            if node!= parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        def union(node1, node2):
            p1,p2 = find(node1), find(node2)
            if p1==p2: #cycle
                return False
            elif rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]