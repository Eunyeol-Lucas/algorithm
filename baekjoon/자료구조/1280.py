N = map(int, input()) #정수 배열의 길이 
N_list = list(map(int, input().split())) #주어진 정수 배열 
M = map(int, input()) #찾을 수 개수 
M_list = list(map(int, input().split())) #찾고자 하는 수 배열 #N_list 안에 존재하는지 
N_list.sort() #이진 탐색을 위한 정렬 

#case 1: 없을 때 
#case 2: 발견 
#case 3: 범위 조정 

def bin_search(m, st, ed, N_list): 
    mid = (st+ed)//2 
    if st>ed: #범위 오류, 이 배열 안에 없다. 0출력 
        print(0) 
    elif m == N_list[mid]: #숫자 발견 1출력 
        print(1) 
    elif m > N_list[mid]: #중앙값보다 크다, 범위 조정 후 재개 
        bin_search(m, mid+1, ed, N_list) 
    elif m < N_list[mid]: #중앙값보다 작다, 범위 조정 후 재개 
        bin_search(m, st, mid-1, N_list) 

for m in M_list: 
    bin_search(m, 0, len(N_list)-1, N_list)
