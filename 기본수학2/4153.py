while True:
    xyz = list(map(int, input().split()))
    max_ = max(xyz)
    if sum(xyz) == 0:
        break
    xyz.remove(max_)
    if max_**2 ==  xyz[0]**2 + xyz[1]**2:
        print("right")
    else:
        print("wrong")