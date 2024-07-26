from typing import Tuple

class SuffixArray:
    def __init__(self, text: str) -> None:
        if not text:
            raise ValueError("text is required")
        self.text = text
        self.suffixes = []

        for i in range(len(self.text)):
            self.suffixes.append((self.text[i:], i))
        self.suffixes.sort()
        print(f"suffixes {self.suffixes}")


    def search(self, pattern: str) -> Tuple[int, int]:
        """
        Perform a binary search and return the (i , j) where i is is index in the suffix
        array and j is the index in the original string or (-1, -1) if not found.
        """
        start = 0
        end = len(self.suffixes) - 1
 
        while start <= end:
            m = (start + end) // 2
            mid_val, starts_at = self.suffixes[m]

            if mid_val > pattern:
                end = m - 1
            elif mid_val < pattern:
                start = m + 1
            else:
                return m, starts_at
        return -1, -1


    def find_shortest_substr(self, pattern: str) -> str:
        """
        Find the shortest substring that starts with the given pattern

        We find the exact match which is the shortest.
        TODO: We don't address the case where there is no exact match.
        """
        if not pattern:
            raise ValueError(f"starts_with is required")
        
        _, i = self.search(pattern)
        return i


    def find_longest_substr(self, starts_with: str) -> str:
        """
        Find the longest substring that starts with the given string
        """
        if not starts_with:
            raise ValueError(f"starts_with is required")
        
        result = None
        for suffix in self.suffixes:
            if suffix.startswith(starts_with):
                if not result:
                    result = suffix
                elif len(result) < len(suffix):
                    result = suffix
        return result


    def find_all_substrs(self, starts_with: str) -> list[str]:
        """
        Find all the substrings that start with the given string
        """
        if not starts_with:
            raise ValueError(f"starts_with is required")
        
        result = set()
        for suffix in self.suffixes:
            if suffix.startswith(starts_with):
                result.add(suffix)
        return list(result)
