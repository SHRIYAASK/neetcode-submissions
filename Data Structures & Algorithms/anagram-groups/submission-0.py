class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        visited = [False] * len(strs)
        sorted_words = [sorted(word) for word in strs]

        for i in range(len(strs)):
            if visited[i]:
                continue

            temp = [strs[i]]
            visited[i] = True

            for j in range(i + 1, len(strs)):
                if not visited[j] and sorted_words[i] == sorted_words[j]:
                    temp.append(strs[j])
                    visited[j] = True

            result.append(temp)

        return result