import sys
input = sys.stdin.readline

def myInput(_list, k):
    return [-1 if idx < k-1 else sorted(_list[:idx + 1])[k-1] for idx in range(len(_list))]


def main():
    n, k = map(int, input().split())
    _list = list(map(int, input().split()))
    print(*myInput(_list, k))

if __name__ == "__main__":
    main()