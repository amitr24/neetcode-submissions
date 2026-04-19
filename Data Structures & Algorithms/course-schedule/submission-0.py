class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list) 
        for prereq in prerequisites:
            adjList[prereq[0]].append(prereq[1])

        visited = set() # Keeps track of visited nodes in a traversal
        def dfs(course):
            if course in visited:
                return False
            if adjList[course] == []:
                return True
            visited.add(course)
            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            adjList[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True