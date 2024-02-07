
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
from itertools import combinations, product
import bisect


def solution(dice):
    answer = []
    max_win_count = 0

    dice_set = {i for i in range(len(dice))}
    for a_choice in combinations([i for i in range(len(dice))], len(dice) // 2):
        a_sum_list = make_sum_list(a_choice, dice)
        b_choice = list(dice_set.difference(a_choice))
        b_sum_list = make_sum_list(b_choice, dice)

        win_count = 0
        for i in range(len(a_sum_list)):
            win_count += bisect.bisect_left(b_sum_list, a_sum_list[i])

        if win_count > max_win_count:
            max_win_count = win_count
            answer = sorted(list(a_choice))

    return [i + 1 for i in answer]


def make_sum_list(choice, dice):
    # choice [1,2,3,4,5]
    sum_list = []
    for pr in product([i for i in range(6)], repeat=len(choice)):  # 각 주사위의 idx 순열
        sum = 0
        for select_dice, idx in zip(choice, pr):
            sum += dice[select_dice][idx]
        sum_list.append(sum)

    return sorted(sum_list)

if __name__ == '__main__':
    solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]])

"""
A와 B가 N개의 주사위를 가지고 승부한다.
각 면이 나올 확률 동일. 단 , 주사위의 면에 적힌수는 임의의 수이다.

A가먼저 n/2개 그다음 B가 가져간다.
각자 주사위를 굴려 나온 수들을 모두 합해 점수계산하고
점수가 더 큰쪽이 승리한다.
점수가 같다면 무승부이다.

A는 자신이 승리할 확률이 가장 높아지도록 주사위를 가져가려한다.

주사위의 총개수는 2n 개이며 최대 10개이다.

즉 가장 최악의 경우 A가 주사위 5개를 선택한다.
10C5 = 252

문제는 시간초과
총 주사위수가 10개면
한번의 조합당 6**10 6천만번 연산이 소모.

[1,2,3,4,5,6]

A : 5 6 7 9 13

4 7 19 44 22
[]



"""

