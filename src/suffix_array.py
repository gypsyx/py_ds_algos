from typing import Optional

class SuffixArray:
    def __init__(self, text: str) -> None:
        if not text:
            raise ValueError("text is required")
        self.text = text
        self.suffixes = []

        for i in range(len(self.text)):
            self.suffixes.append(self.text[i:])
        self.suffixes.sort()
        print(f"suffixes {self.suffixes}")


    def search(self, pattern: str):
        pass

    def find_shortest_substr(self, starts_with: str) -> str:
        """
        Find the shortest substring that starts with the given string

        NOTE: results are based on suffixes only. So searches for susbstring that don't have
        last character(s) won't be possible. For example searching for 'appl' in 'apple' returns
        'apple'.
        """
        if not starts_with:
            raise ValueError(f"starts_with is required")
        result = None

        for suffix in self.suffixes:
            if suffix.startswith(starts_with):
                if not result:
                    result = suffix
                elif len(result) > len(suffix):
                    result = suffix
        return result


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
