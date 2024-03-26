from typing import Sequence

def sequences_equal(s1: Sequence, s2: Sequence) -> bool:
    if len(s1) != len(s2):
        return False
    
    for item in s1:
        if item not in s2:
            return False
    return True