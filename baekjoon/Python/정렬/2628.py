import sys

input = sys.stdin.readline


def solution(x_list, y_list):
    max_area = 0
    sorted_x_list = sorted(x_list)
    sorted_y_list = sorted(y_list)
    for i in range(1, len(sorted_x_list)):
        for j in range(1, len(sorted_y_list)):
            width = sorted_x_list[i] - sorted_x_list[i-1]
            height = sorted_y_list[j] - sorted_y_list[j-1]
            max_area = max(max_area, width * height)

    return max_area


x, y = map(int, input().split())
n = int(input())
x_list = [0, x]
y_list = [0, y]
for _ in range(n):
    a, b = map(int, input().split())
    if a:
        x_list.append(b)
    else:
        y_list.append(b)
print(solution(x_list, y_list))
