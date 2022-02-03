import sys

word = sys.stdin.readline().strip()
answer = []
for i in range(len(word)):
    answer.append(word[i:])
seq_word = sorted(answer)
print('\n'.join(seq_word))
