class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        def generate(s = '', opening = 0, closing = 0):
            if len(s) == 2 * n: # base case
                combinations.append(s)
                return
            
            if opening < n:
                generate(s + '(', opening + 1, closing)
            
            if closing < opening:
                generate(s + ')', opening, closing + 1)
                
        generate()
        return combinations
