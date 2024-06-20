class Solution:   # similar to aggresive cows
    def can_we_place(self, min_dis, m, arr):
        count_cow = 1
        last = arr[0]
        for i in range(1, len(arr)):
            if arr[i] - last >= min_dis:
                count_cow += 1
                last = arr[i]
        if count_cow >= m:
            return True
        else:
            return False

    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        low = 1
        high = position[n-1]-position[0]

        while low <= high:
            mid = (low+high)//2
            if self.can_we_place(mid, m, position):
                low = mid+1
            else:
                high = mid-1
        return high
        # for min_dis in range(1, position[n-1]-position[0]+1):
        #     if self.can_we_place(min_dis, m, position):
        #         print(min_dis)
        #         continue
        #     else:
        #         return min_dis-1
        # return -1