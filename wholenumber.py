def whole(N):
    if N == 0:
        return 0
    else:
        return N + whole(N - 1)

N = int(input())
print(whole(N))