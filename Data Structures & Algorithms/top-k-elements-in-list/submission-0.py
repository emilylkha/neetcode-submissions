class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] -= 1
        countList = [(count[num], num) for num in count.keys()]
        heapq.heapify(countList)
        freq = []
        for _ in range(k):
            freq.append(heapq.heappop(countList)[1])
        return freq