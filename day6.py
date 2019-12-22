
def parse_system(maps):
    orbs = {}
    for line in maps:
        s, o = line.strip().split(')')
        if s in orbs:
            orbs[s].append(o)
        else:
            orbs[s] = [o]
    return orbs

def count_orbs(orbs, depth, cur):
    if not cur in orbs:
        return depth
    else:
        suborbs = sum([count_orbs(orbs, depth+1, o) for o in orbs[cur]])
        return depth + suborbs

def abs_path(orbs, route, cur, dest):
    if cur == dest:
        return route
    if not cur in orbs:
        return []
    else:
        for o in orbs[cur]:
            r = [n for n in route] # memory memes
            r.append(cur)
            res = abs_path(orbs, r, o, dest)
            if len(res) > 0:
                return res
        return []

def shortest_path(orbs, source, dest):
    p1 = abs_path(orbs, [], 'COM', source)
    p2 = abs_path(orbs, [], 'COM', dest)

    min_p = min(len(p1), len(p2))
    for n in range(min_p):
        if p1[n] != p2[n]:
            path = p1[:n-1:-1] + p2[n-1:-1]
            return len(path)
    else:
        path = p1[n-1:] + p2[n-1:]
        return len(path)

with open('input/day6.txt') as f:
    solar_map = f.readlines()

orbs = parse_system(solar_map)
print(len(orbs))
total_orbs = count_orbs(orbs, 0, 'COM')
print(total_orbs)
print(shortest_path(orbs, 'YOU', 'SAN'))
