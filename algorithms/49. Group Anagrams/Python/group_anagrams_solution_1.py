from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = defaultdict(list)
    for s in strs:
        result["".join(sorted(s))].append(s)
    return result.values()
