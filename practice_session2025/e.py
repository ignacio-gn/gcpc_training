from itertools import combinations_with_replacement


def solve():
    def eval_pair(t1, t2):
        max_dimension = t1[1] if t1[1] > t2[1] else t2[1]
        min_dimension = t1[0] if t1[0] < t2[0] else t2[0]
        return max_dimension * min_dimension ** 2

    out = 0
    for t1, t2 in combinations_with_replacement(c, 2):
        out = max(out, eval_pair(t1, t2))
    return out


def solve_v2(c):
    max_area = 0

    for i in range(len(c)):
        for j in range(i, len(c)):
            out = max(
                max_area,
                c[i][1] * min(c[i][0], c[j][0]) ** 2
            )

    return out


n = int(input())
c = list(map(
    lambda x: ((x[0], x[1]) if x[1] > x[0] else (x[1], x[0])),
    [list(map(
        int,
        input().split(" "))) for _ in range(n)
    ])
)

print(solve_v2(c))
