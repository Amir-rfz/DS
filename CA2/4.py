class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.left = list(range(n))
        self.right = list(range(n))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
                self.left[root_u] = min(self.left[root_u], self.left[root_v])
                self.right[root_u] = max(self.right[root_u], self.right[root_v])
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
                self.left[root_v] = min(self.left[root_u], self.left[root_v])
                self.right[root_v] = max(self.right[root_u], self.right[root_v])
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
                self.left[root_u] = min(self.left[root_u], self.left[root_v])
                self.right[root_u] = max(self.right[root_u], self.right[root_v])
            return True
        return False

def largest_rectangle_area(heights):
    n = len(heights)
    if n == 0:
        return 0
    
    # Sort buildings by height in descending order
    sorted_buildings = sorted(range(n), key=lambda i: -heights[i])

    # Initialize Union-Find for n elements
    uf = UnionFind(n)
    status = [False] * n
    max_area = 0

    for i in sorted_buildings:
        status[i] = True
        if i > 0 and status[i - 1]:
            uf.union(i, i - 1)
        if i < n - 1 and status[i + 1]:
            uf.union(i, i + 1)
        
        # Find root of current element to get correct bounds
        root = uf.find(i)
        current_area = heights[i] * (uf.right[root] - uf.left[root] + 1)
        max_area = max(max_area, current_area)

    return max_area

# Example usage
_ = input()
building_heights = list(map(int, input().split()))
print(largest_rectangle_area(building_heights))
