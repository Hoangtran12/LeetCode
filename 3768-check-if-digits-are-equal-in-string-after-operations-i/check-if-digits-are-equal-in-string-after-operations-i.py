class Solution:
    def hasSameDigits(self, s: str) -> bool:
        arr = [int(x) for x in s]
        
        while len(arr) > 2:
            new_arr = [(x+y) % 10 for x, y in zip (arr, arr[1:])]
            arr = new_arr
        return arr[0] == arr[1]