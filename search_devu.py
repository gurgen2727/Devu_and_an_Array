#!/usr/bin/env python
import sys

#sys.stdin = open('in.txt')
sys.stdin = open('in.txt')
N_Q = raw_input().split()
Q = int(N_Q[1])
array = map(int, raw_input().split())

max_array = 0
min_array = 1000000000
for el in array:
    if el < min_array:
        min_array = el
    if el > max_array:
        max_array = el

for _ in xrange(Q):
    if min_array <= input() <= max_array:
        sys.stdout.write('Yes\n')
    else:
        sys.stdout.write('No\n')

# for t in sys.stdin.readlines():
#     if min_array <= t.strip() <= max_array:
#         sys.stdout.write('Yes\n')
#     else:
#         sys.stdout.write('No\n')
