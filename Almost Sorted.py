#!/bin/python3


# Complete the almostSorted function below.
def almostSorted(arr):
    sorted_arr = sorted(arr)
    n = len(arr)
    i = 0
    j = n-1

    if arr==sorted_arr:
        print('yes')
    else:
        while (arr[i]==sorted_arr[i] or arr[j]==sorted_arr[j]):
            if arr[i]!=sorted_arr[i]:
                j-=1
            else:
                i+=1
        #print("portion out",arr[i:j+1])
        #print("portion out r ",list(reversed(arr[i:j+1])))
        if arr[i]==sorted_arr[j] and arr[j]==sorted_arr[i]:
            if arr[i+1:j] == sorted_arr[i+1:j]:
                print('yes')
                print('swap' , i+1,j+1)
            elif arr[i+1:j] == list(reversed(sorted_arr[i+1:j])):
                print('yes')
                print('reverse' , i+1,j+1)

        else:print('no')



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
