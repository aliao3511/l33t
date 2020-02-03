class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        
        def make_combination(target, start, combination):
            if target == 0:
                results.append(combination)
                return
            
            for i in range(start, len(candidates)):
                current = candidates[i]
                
                if current > target:
                    break
                
                remaining = target - current
                if remaining and remaining < candidates[0]:
                    continue
                
                make_combination(remaining, i, combination + [current])
                
        make_combination(target, 0, [])
        return results
