def share_bread(N, K):
    N = int(input(''))
    K = int(input(''))
    x = K//N
    y = K%N
    print('x=',K//N) 
    print('y=',K%N)
    return x, y
share_bread(N, K)

assert share_bread(N=3, K=14) == (4, 2)
