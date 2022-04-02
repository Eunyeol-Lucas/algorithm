import sys
input = sys.stdin.readline

# 전위 순회
def preorder(v):
    if v != ".":
        print(v, end="")
        preorder(dict[v][0])
        preorder(dict[v][1])

# 중위 순회
def inorder(v):
    if v != ".":
        inorder(dict[v][0])
        print(v, end="")
        inorder(dict[v][1])

# 후위 순회
def postorder(v):
    if v != ".":
        postorder(dict[v][0])
        postorder(dict[v][1])
        print(v, end="")


N = int(input())
dict = {}
for i in range(N):
    A, B, C = input().strip().split()
    dict[A] = [B, C]

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
