class ListCounter:
    def __init__(self, elements):
        self.counts = {}
        for el in elements:
            if el in self.counts:
                self.counts[el] += 1
            else:
                self.counts[el] = 1

    def most_common_x(self, n):
        ranked_counts = [(el, self.counts[el]) for el
                         in sorted(self.counts,
                                   key=lambda x: (self.counts[x], x),
                                   reverse=True)]
        return ranked_counts[:n]


def find_x_sums_1(nums: list[int], k: int, x: int) -> list[int]:
    ans = []

    for i in range(len(nums)-k+1):
        if k <= x:
            ans.append(sum(nums[i:i+k]))
        else:
            c = ListCounter(nums[i:i+k])
            ans.append(sum([el * n for el, n in c.most_common_x(x)]))

    return ans
