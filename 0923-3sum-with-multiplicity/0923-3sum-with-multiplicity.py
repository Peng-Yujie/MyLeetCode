class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        n = len(arr)
        count = 0
        for i in range(n):
            t = target - arr[i]
            m = defaultdict(int)
            for j in range(i + 1, n):
                if arr[j] in m:
                    count += m[arr[j]]
                m[t - arr[j]] += 1

        return count
