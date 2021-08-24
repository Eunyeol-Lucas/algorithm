for _ in range(int(input())):
    floor = int(input())
    room = int(input())
    floor_zero = [j for j in range(1, room+1)]  
    for x in range(floor):  
        for y in range(1, room): 
            floor_zero[y] += floor_zero[y-1]
        
    print(floor_zero[-1])