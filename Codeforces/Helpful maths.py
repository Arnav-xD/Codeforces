s=input()
arr = [i for i in s if i.isdigit()]
ans = "+".join(sorted(arr))
print(ans)

