from collections import defaultdict, deque
import sys

def solve():
    input = sys.stdin.readline
    n = int(input().strip())

    g = defaultdict(list)
    for _ in range(n):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    q = deque([1])
    vis = {1}
    ans = 1

    while q:
        u = q.popleft()
        ans = max(ans, u)
        for v in g[u]:
            if v not in vis:
                vis.add(v)
                q.append(v)

    print(ans)

if __name__ == "__main__":
    solve()
