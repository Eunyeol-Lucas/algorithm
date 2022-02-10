import sys

def get_number_of_fills(n):
    arr = [0] * (n+1)
    # 2 * 1을 채우는 방법은 1가지
    arr[1] = 1
    # 2 *2를 채우는 방법 2가지
    arr[2] = 2
    # 3이상부터 다이나믹 프로그래밍 규칙에 따라 i는 i - 1의 방법의 수와 i - 2의 방법의 수의 합
    for i in range(3, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n] % 10007


n = int(sys.stdin.readline())
print(get_number_of_fills(n))
