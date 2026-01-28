class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        min_diff = float('inf')
        for i in range(n - 1):
            curr = arr[i + 1] - arr[i]
            if curr < min_diff:
                min_diff = curr
        res = []
        for i in range(n - 1):
            if (abs(arr[i] - arr[i + 1])) <= min_diff:
                res.append([arr[i], arr[i + 1]])
        return res