from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        count=Counter(nums)
        items=list(count.items())
        items.sort(key=lambda x:x[1],reverse=True)
        for i in range(k):
            ans.append(items[i][0])
        return ans 

        