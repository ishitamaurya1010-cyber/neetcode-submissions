class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       groups=defaultdict(list)

       for i in strs:
        key=''.join(sorted(i))
        groups[key].append(i)
       return list(groups.values())