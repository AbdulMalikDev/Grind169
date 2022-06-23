class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites)==0:
            return True
        Indegree = [0] * 2000
        graph = defaultdict(list)
        nodes = set()
        for b,a in prerequisites:
            # if you take 'a' you can take 'b'
            # so a->b
            nodes.add(a)
            nodes.add(b)
            graph[a].append(b)
        
        for node,dependency in graph.items():
            for eachDependency in dependency:
                Indegree[eachDependency] += 1
                
        zeroIndegree = []
        for x,y in prerequisites:
            if Indegree[x] == 0 and x not in zeroIndegree:
                zeroIndegree.append(x)
            if Indegree[y] == 0 and y not in zeroIndegree:
                zeroIndegree.append(y)
        
        queue = deque(zeroIndegree)
        topSort = []
        while queue:
            node = queue.popleft()
            topSort.append(node)
            for dependency in graph[node]:
                Indegree[dependency] -= 1
                if Indegree[dependency] == 0:
                    queue.append(dependency)
                    
        return len(topSort)==len(nodes)
                
        