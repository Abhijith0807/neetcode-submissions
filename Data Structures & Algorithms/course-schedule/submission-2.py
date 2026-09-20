class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap={i:[] for i in range(numCourses)}
        for cr,pr in prerequisites:
            prereqMap[cr].append(pr)
        visited_set=set()
        def dfs(course):
            visited_set.add(course)
            for crs in prereqMap[course]:
                if crs in visited_set:
                    return(False)
                if not dfs(crs):
                    return(False)
            visited_set.remove(course)
            prereqMap[course]=[]
            return(True)


        for course in range(numCourses):
            if not dfs(course):
                return(False)
        return(True)
        