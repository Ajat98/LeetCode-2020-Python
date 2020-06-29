class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        res = []
        for i in arr2:
            for j in range(arr1.count(i)):
                res.append(i)
                arr1.remove(i)
        
        return res + sorted(arr1)
