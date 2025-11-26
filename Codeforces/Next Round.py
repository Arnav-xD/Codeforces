n , k = map(int,input().split())
arr = [int(i) for i in input().split()]
next_round = [i for i in arr if (i>0 and i >= arr[k-1])]
print(len(next_round))