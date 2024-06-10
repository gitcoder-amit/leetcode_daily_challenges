# Problem statement
# Given two arrays ‘ARR’ and ‘BRR’ of size ‘N’ and ‘M’ respectively. Your task is to sort the elements of ‘ARR’ in such a way that the relative order among the elements will be the same as those are in ‘BRR’. For the elements not present in ‘BRR’, append them in the last in sorted order.

# For example

# Consider the arrays as ARR = { 9, 5, 8, 4, 6, 5 } and BRR = { 8, 4, 5 }
# The output for the above example  is { 8, 4, 5, 5, 6, 9 }.
# Note:

# Elements of ‘BRR’ are non repeating.


import heapq
def relativeSorting(arr, brr, n,  m):
    # Write your code here
    # Return a list of integers
    map = {}
    for i in arr:
        map[i] = map.get(i, 0) + 1

    ans = []
    for i in brr:
        if i in map:
            ans.extend([i]*map[i])
            del map[i]
    pq = list(map.keys())
    heapq.heapify(pq)
    
    while map:
        key = pq[0] # or key = min(map)

        ans.append(key)
        map[key] -= 1
        if map[key] == 0:
            del map[key]
            heapq.heappop(pq)

    return ans

