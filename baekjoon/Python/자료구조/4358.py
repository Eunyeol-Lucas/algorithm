import sys
from collections import defaultdict

int_dict = defaultdict(int)
lines = sys.stdin.readlines()
for line in lines:
    int_dict[line.rstrip()] += 1

for key, val in sorted(int_dict.items()):
    print(key, '{:.4f}'.format(val / len(lines) * 100))