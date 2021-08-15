n = int(input())
arr = map(int, input().split())
runnerup = sorted(set(arr))[-2]
print(runnerup)