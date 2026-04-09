class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorts= ["".join(sorted(s)) for s in strs]
        output={}
        for i in range(len(sorts)):
            output.setdefault(sorts[i], []).append(strs[i])
        
        return list(output.values())
