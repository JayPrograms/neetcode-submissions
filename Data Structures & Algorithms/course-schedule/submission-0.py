class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #make a directed graph, and if there is a cycle, then it doesnt work

        #make the graph. initialize a node [] for each course
        preMap = {i: [] for i in range(numCourses)}

        #save the prerequisites as nodes being pointed to from the crs node
        for crs, pre, in prerequisites:
            preMap[crs].append(pre)


        #to store courses seen in the path so far when we traverse the graph
        visiting = set()


        def dfs(crs):
            if crs in visiting:
                #if there is a cycle
                return False

            #if course has no prerequisits, stand alone node, disconnected
            if preMap[crs] == []:
                return True
            
            #add the visited node to the list
            visiting.add(crs)

            #check if the prerequisits of the course dont have a cycle (arent in visited set)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)

            #clean up for the current course so we can reuse the visitng set and premap for next course
            preMap[crs] = []

            return True

        #if none of the courses fail the dfs cycles check, return true
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

            

        