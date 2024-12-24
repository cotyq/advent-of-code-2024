network = {}
processed = set()


with open("input23") as file:
    for line in file:
        a, b = line.strip().split("-")
        network.setdefault(a, [])
        network.setdefault(b, [])
        network[a].append(b)
        network[b].append(a)


t_solutions = 0
max_lan_size = 0
password = ""

for node, connections in network.items():
    lan = {node}
    for i, a in enumerate(connections[:-1]):
        for b in connections[i + 1 :]:
            if a not in processed and b not in processed and a in network[b]:
                if any(n.startswith("t") for n in [node, a, b]):
                    t_solutions += 1
    processed.add(node)
    for a in connections:
        if all(a in network[b] for b in lan):
            lan.add(a)
    if len(lan) > max_lan_size:
        max_lan_size = len(lan)
        password = ",".join(sorted(lan))


print(t_solutions)
print(password)
