def get_max_edges(employee_nodes, employee_from, employee_to, special_employees):
    n = employee_nodes
    m = len(employee_from)
    x = min(100000000000, (n*(n-1))/2)
    adj = [[] for _ in range(n)]
    s1 = set()
    for i in range(m):
        u = employee_from[i]-1
        v = employee_to[i]-1

        adj[u].append(v)
        adj[v].append(u)

        if u > v:
            u, v = v, u

        s1.add((u, v))

    k = len(special_employees)
    is_special = [0]*n

    for i in range(k):
        is_special[special_employees[i]-1] = 1

    vis = [False] * n
    compo_sizes = []
    rem = 0

    for i in range(n):
        if vis[i]:
            continue

        cnt = 0
        tot = 0
        q1 = []
        q1.append(i)
        vis[i] = True

        while q1:
            it = q1.pop(0)
            cnt += is_special[it]
            tot += 1
            for x in adj[it]:
                if vis[x]:
                    continue

                q1.append(x)
                vis[x] = True
        
        if cnt == 1:
            compo_sizes.append(tot)
        else:
            rem += tot
        

    ans = -m 
    compo_sizes.sort()
    cur = max_connections
    tot = rem

    while len(compo_sizes) > 0:
        if cur == 0:
            ans += (tot * (tot-1))//2
            cur = max_connections
            tot = 0 
        else:
            tot += compo_sizes[-1]
            cur -= 1
            compo_sizes.pop()

    if tot > 0:
        ans += (tot * (tot-1))//2
    
    return ans