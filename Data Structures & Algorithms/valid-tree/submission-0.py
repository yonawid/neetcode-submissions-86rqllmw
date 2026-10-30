class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj=defaultdict(list)
        queue=deque([0])
        visited={0}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        while queue:
            node=queue.popleft()
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

        return len(visited)==n
        