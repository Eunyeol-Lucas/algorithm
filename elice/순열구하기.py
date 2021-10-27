from itertools import permutations
from string import ascii_lowercase

def getPermutations(n, r):
    comb = permutations(ascii_lowercase[:n], r)
    result = []
    for data in comb:
        result.append(''.join(data))
    
    return result

def main():
    n, r = map(int, input().split())
    print(*getPermutations(n, r), sep="\n")

if __name__ == "__main__":
    main()