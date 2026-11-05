class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        path, visit  = set(), set()
        output = []
        def dfs(course):
            if course in path:
                return False
            if course in visit:
                return True
            path.add(course)
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            path.remove(course)
            visit.add(course)
            output.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output