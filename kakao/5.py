def shift(arr):
    return [arr[-1]] + arr[:-1]


def rotate(arr):
    x, y = 0, 0
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction = 0
    w = len(arr[0])
    h = len(arr)
    ans = arr[0][0]
    while True:
        nx = x + d[direction][0]
        ny = y + d[direction][1]
        if 0 <= nx < h and 0 <= ny < w:
            arr[x][y] = arr[nx][ny]
            x = nx
            y = ny
        else:
            nx -= d[direction][0]
            ny -= d[direction][1]
            direction += 1
            if direction == 4:
                break
    arr[0][1] = ans
    return arr


def solution(rc, operations):
    answer = rc
    for i in operations:
        if i == "Rotate":
            answer = rotate(answer)
        else:
            answer = shift(answer)

    return answer


# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# b = ["Rotate", "ShiftRow"]

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
b = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]
print(solution(a, b))
