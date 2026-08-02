class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                topi, topT = stack.pop()
                temps[topi] = i - topi
            stack.append((i, temp))
        return temps
        