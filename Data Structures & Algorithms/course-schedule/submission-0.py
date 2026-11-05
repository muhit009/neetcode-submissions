class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Each course is a node
        Prereq is a directed edge
        Detect if cycle exist
        '''
        #adjaceny list
        pre = {i: [] for i in range(numCourses)}
        for c,p in prerequisites:
            pre[c].append(p)
        visit = set() # nodes that are processed
        path = set() #nodes in current path
        def dfs(course):
            if course in visit:
                return True
            if course in path:
                return False
            path.add(course)
            for p in pre[course]:
                if not dfs(p):
                    return False
            path.remove(course)
            visit.add(course)
            return True
        
        for  c in range(numCourses):
            if not dfs(c):
                return False
        return True