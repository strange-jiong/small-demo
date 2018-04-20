"""
dtw python朴素实现
"""
import sys
def distance(x,y):
    return abs(x-y)

def dtw():
    X = [1, 2, 3, 4]
    Y = [1, 2, 7, 4, 5]
    M = [[distance(X[i], Y[i]) for i in range(len(X))] for j in range(len(Y))]
    # print(M)
    l1 = len(X)
    l2 = len(Y)
    D = [[0 for i in range(l1 + 1)] for i in range(l2 + 1)]
    # D[0][0] = 0
    for i in range(1, l1 + 1):
        D[0][i] = sys.maxsize
    for j in range(1, l2 + 1):
        D[j][0] = sys.maxsize
    for j in range(1, l2 + 1):
        for i in range(1, l1 + 1):
            D[j][i] = distance(X[i -1],Y[j-1 ])+ \
                min(D[j - 1][i], D[j][i - 1], D[j - 1][i - 1])
            print(j,i,D[j][i])
    print(D)

if __name__ == '__main__':
    dtw()
