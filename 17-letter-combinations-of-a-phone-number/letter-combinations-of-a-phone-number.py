from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mappings = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        combinations = [""]

        for digit in digits:
            new_combinations = []
            for combo in combinations:
                for char in mappings[digit]:
                    new_combinations.append(combo + char)
            combinations = new_combinations
            
        return combinations