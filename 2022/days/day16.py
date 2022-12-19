"""
--- Day 16: Proboscidea Volcanium ---
https://adventofcode.com/2022/day/16

Note: I had to look at other peoples solutions 
to figure out how to get a speed improvement.

Inspiration from:
https://github.com/juanplopes/advent-of-code-2022/blob/main/day16.py
"""

from functools import lru_cache
from aoc import *

valves = []
flow = {}
adj = {}

inputs = puzzle_input(16, 2022, sample=False).split('\n')
for line in inputs:
    spl = line.split(' ')
    name = spl[1]
    if name not in valves:
        valves.append(name)
    
    name = valves.index(name)
    if int(spl[4][5:-1]) > 0:
        flow[name] = int(spl[4][5:-1])
    leads_raw = line.split('valve')[1]
    leads = (leads_raw[2:] if leads_raw[0] == 's' else leads_raw[1:]).split(', ')
    leads_num = []
    for l in leads:
        if l not in valves:
            valves.append(l)
        leads_num.append(valves.index(l))
    adj[name] = leads_num

v_len = len(valves)
D = {i: {j: 1 if j in adj[i] else float('+inf') for j in range(v_len)} for i in range(v_len)}
for k in range(v_len):
    for i in range(v_len):
        for j in range(v_len):
            D[i][j] = min(D[i][j], D[i][k]+D[k][j])

@timeit
def compute_flow_values(m):
    results = {}
    def compute_p(v, m, opened, f):
        results[opened] = max(results.get(opened, 0), f)
        for u in flow:
            new_m = m - D[v][u] - 1
            if opened & (1 << u) or new_m <= 0:
                continue
                
            compute_p(u, new_m, opened | (1 << u), f + new_m * flow[u])

    compute_p(valves.index('AA'), m, 0, 0)
    return results.items()
    

print(f'Part 1: {max(i[1] for i in compute_flow_values(m=30))}')

flow_vals_2 = compute_flow_values(m=26)
ans2 = max(v1+v2 for k1, v1 in flow_vals_2 for k2, v2 in flow_vals_2  if not (k1 & k2))
print(f'Part 2: {ans2}')

# naive solution
# @lru_cache(maxsize=1_000_000)
# def most_pressure(v=valves.index('AA'), m=1, total_m=30, opened=0, p1=True):
#     if m > total_m or not ~opened:
#         return 0 if p1 else most_pressure(total_m=total_m, opened=opened, p1=True)
    
#     max_p = max(most_pressure(t, m+1, total_m, opened, p1) for t in adj[v])


#     if not (opened & (1 << v)) and flow[v] != 0:
#         open_p = most_pressure(v, m+1, total_m, opened | (1 << v), p1) + flow[v] * (total_m-m)
#         max_p = max(max_p, open_p)
    
#     return max_p

# @timeit
# def ans1():
#     return most_pressure()

# print(f'Part 1: {ans1()}')

# @timeit
# def ans2():
#     return most_pressure(total_m=26, p1=False)

# print(f'Part 2: {ans2()}')
