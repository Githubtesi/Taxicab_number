# 1729=Ta(2)=1**2+12**3=9**3+10**3
# Input 1,2 [(1729,[(1,12),(9,10)])]
# Input 2,2 [(1729,[(1,12),(9,10)]) ,(4104,[(2,16),(9,15)])]
# Input 1,3 [(87539319,[(167,436),(228,423),(255,414)])]
from collections import defaultdict
from typing import List, Tuple


def taxi_cab_number(max_answer_num: int, match_answer_num: int = 2) -> List[Tuple[int, List[Tuple[int, int]]]]:
    result = []
    got_answer_count = 0
    while got_answer_count < max_answer_num:
        match_answer_count = 0
        memo = defaultdict(list)


if __name__ == '__main__':
    pass
