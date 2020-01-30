class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        combinations = []
        return self.letterCombination(digits, combinations, mapping) 
                
    def letterCombination(self, digits, combinations, mapping):
        if not digits:
            return combinations
        
        letters = mapping[digits[0]]
        if len(combinations) == 0:
            new_combinations = [letter for letter in letters]
        else:
            new_combinations = [combo + letter for letter in letters for combo in combinations]
        return self.letterCombination(digits[1:], new_combinations, mapping)
