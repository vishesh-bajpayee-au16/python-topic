# QUESTION - 1 https://www.codechef.com/problems/FLOW001

T = int(input())
arr = []
sumFinal = []

def sumArr(elementCount):
    for i in range(elementCount):
        input_ = list(map(int,input().split()))
        arr.append(input_)
    return arr


def finalArr(arr):
    for i in arr:
        total = i[0] + i[1]
        sumFinal.append(total)
    return sumFinal


def ans(finalArr):
    for i in finalArr:
        print(i)


arr1 = sumArr(T)
arr2 = finalArr(arr1)
ans(arr2)   

