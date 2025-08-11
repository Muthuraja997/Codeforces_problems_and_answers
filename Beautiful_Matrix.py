for i in range(5):
    l2 =list(map(int, input().split()))
    for j in range(5):
        if l2[j] == 1:
            print(abs(2-i) + abs(2-j))
            exit(0)
