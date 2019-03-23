import sys

inputGraphFile = sys.argv[1]
graph = {}

with open(inputGraphFile) as graph_input:
    for line in graph_input:
        nodes = [int(x) for x in line.split()]
        if len(nodes) != 2:
            continue
        if nodes[0] not in graph:
            graph[nodes[0]] = []
        if nodes[1] not in graph:
            graph[nodes[1]] = []
        graph[nodes[0]].append(nodes[1])
        graph[nodes[1]].append(nodes[0])

def create_pq():
    return []*len(graph)

def create_list():
    return []*len(graph)

def add_last(pq, c):
    pq.append(c)

def root(pq):
    return 0

def set_root(pq, c):
    if len(pq) != 0:
        pq[0] = c

def get_data(pq, p):
    return pq[p]

def children(pq, p):
    if 2*p + 2 < len(pq):
        return [2*p + 1, 2*p + 2]
    else:
        return [2*p + 1]

def parent(p):
    return (p - 1) // 2

def exchange(pq, p1, p2):
    pq[p1], pq[p2] = pq[p2], pq[p1]


def insert_in_pq(pq, c):
    add_last(pq, c)
    i = len(pq) - 1
    while i != root(pq) and get_data(pq, i) < get_data(pq, parent(i)):
        p = parent(i)
        exchange(pq, i, p)
        i = p
def extract_last_from_pq(pq):
    return pq.pop()

def has_children(pq, p):
    return 2*p + 1 < len(pq)

def extract_min_from_pq(pq):
    c = pq[root(pq)]
    set_root(pq, extract_last_from_pq(pq))
    i = root(pq)
    while has_children(pq, i):
        j = min(children(pq, i), key=lambda x: get_data(pq, x))
        if get_data(pq, i) < get_data(pq, j):
            return c
        exchange(pq, i, j)
        i = j
    return c

def update_pq(pq, x, y):
    index = 0
    for item in range(len(pq)):
        if pq[item][1] == x[1]:
            pq[item] = y
            index = item
            break
    while get_data(pq, index) < get_data(pq, parent(index)) and index != root(pq):
        p = parent(index)
        exchange(pq, index, p)
        index = p

min_pq = create_pq()
degree = create_list()
potential = create_list()
core = create_list()
for node in range(0, len(graph)):
    degree.insert(node, len(graph[node]))
    potential.insert(node, len(graph[node]))
    pn = [len(graph[node]), node]
    insert_in_pq(min_pq, pn)
    core.append(0)

while min_pq.__len__() > 0:
    t = extract_min_from_pq(min_pq)
    core[t[1]] = t[0]
    if min_pq.__len__() != 0:
        for v in graph[t[1]]:
            degree[v] = degree[v] - 1
            opn = [potential[v], v]
            potential[v] = max(t[0], degree[v])
            npv = [potential[v], v]
            update_pq(min_pq, opn, npv)
for i in range(len(degree)):
    print(i, core[i])