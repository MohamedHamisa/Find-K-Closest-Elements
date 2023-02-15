class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = max(0, bisect.bisect(arr, x) - k)
        while idx+k<len(arr) and abs(x-arr[idx+k]) < abs(x-arr[idx]):
                idx +=1
        return arr[idx:idx+k]

        
