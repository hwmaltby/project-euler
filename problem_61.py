#Henry Maltby 2017

def nums_1000_to_10000(a0, a1, a2):
    n, nums = a0, []
    while n < 10000:
        if n >= 1000:
            nums.append(n)
        n += a1
        a1 += a2
    return nums

def add_num(i, used_lsts, starters, dist):
    """
    Some sort of dfs, wherein I decide to create the graph in place??
    """
    stack = [(i, [i], used_lsts)]
    while stack:
        curr, hist, used = stack.pop()
        end = curr % 100
        if end in starters:
            for tup_next in starters[end]:
                if tup_next[0] not in used:
                    if len(hist) == dist - 1:
                        yield hist + [tup_next[1]]
                    else:
                        stack.append((tup_next[1], hist + [tup_next[1]], used\
                            + [tup_next[0]]))

def find_cycle(n):
    figurates = [nums_1000_to_10000(1, i + 1, i) for i in range(1, n + 1)]
    fig_starters = {}
    for i in range(n):
        for k in figurates[i]:
            start = k // 100
            if start not in fig_starters:
                fig_starters[start] = []
            fig_starters[start].append((i, k))
    for num in figurates[0]:
        attempts = list(add_num(num, [0], fig_starters, n))
        for attempt in attempts:
            if len(attempt) == n:
                if attempt[-1] % 100 == attempt[0] // 100:
                    return sum(attempt)

print(find_cycle(6))