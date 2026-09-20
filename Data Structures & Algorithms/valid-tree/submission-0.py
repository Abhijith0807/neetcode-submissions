class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList={i:[] for i in range(n)}
        for n1,n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        visit=set()
        def bfs(node,prev):
            if node in visit:
                 return(False)
            visit.add(node)
            for i in adjList[node]:
                if i==prev:
                    continue
                if not bfs(i,node):
                    return(False)
            return(True)
        return bfs(0,-1) and len(visit)==n

        
        
        