while True:
    a, b, c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    side = [a,b,c]
    side.sort()
    if side[2]**2 == side[0]**2 + side[1]**2:
        print("right")
    else:
        print("wrong")
