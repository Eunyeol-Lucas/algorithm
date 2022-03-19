from collections import deque


def solution(arr, processes):
    answer = []
    for i in range(len(processes)):
        processes[i] = processes[i].split()
    q = deque()
    idx = int(process[0][1])
    start, end = 0, 1000
    for i in processes:
        if i[0] == "read":
            q.append(i)
        else:
            if q:
                while q and int(q[0][1]) < int(i[1]) and end > start + int(q[0][1]):
                    a = q.popleft()
                    print(a)
                    start += (int(a[1])-start)
                    end = start + int(a[2])
                    print("s", "e", start, end)
                    tmp = arr[int(a[3]): int(a[4])+1]
                    answer.append(''.join(tmp))
            start = end
            end = start + int(i[2])
            print("w", "s", "e", start, end)
            for k in range(int(i[3]), int(i[4])+1):
                arr[k] = i[5]
    if q:
        for i in q:
            if end < start + int(i[2]):
                start = end
                end = start + int(i[2])
            tmp = arr[int(i[3]): int(i[4])+1]
            answer.append(''.join(tmp))
    answer.append(str(end-idx))
    return answer


# 읽기는 동시에 가능, 쓰기는 하나의 쓰기만 가능
# t1: 요청시각, t2: 요청 처리 시간, A, B: 데이터를 읽거나 쓸 구간(배열의 인덱스), C: 배열 구간에 쓸 한 자리 숫자
arr = ["1", "2", "4", "3", "3", "4", "1", "5"]
process = ["read 1 3 1 2", "read 2 6 4 7", "write 4 3 3 5 2",
           "read 5 2 2 5", "write 6 1 3 3 9", "read 9 1 0 7"]
# 결과 ["24","3415","4922","12492215","13"]

print(solution(arr, process))
