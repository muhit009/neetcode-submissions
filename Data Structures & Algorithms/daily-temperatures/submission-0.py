class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]* len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: #find if the temp is greater than the temp of the top of the stack
                stack_temp, stack_idx = stack.pop()
                res[stack_idx] = (idx - stack_idx)

            stack.append([temp, idx])
        return res

