def combinationSum(candidates, target):
    res = []

    def backtrack(start, target, path):
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            backtrack(i, target - candidates[i], path + [candidates[i]])

    backtrack(0, target, [])
    return res

candidates = [2, 3, 6, 7]
target = 7
result = combinationSum(candidates, target)
print("Output combinations:", result)
