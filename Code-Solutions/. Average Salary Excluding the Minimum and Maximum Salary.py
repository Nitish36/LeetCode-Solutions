class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        s1 = salary.pop(0)
        s2 = salary.pop(len(salary)-1)
        res = sum(salary)
        aveg = res/(len(salary))
        return aveg
