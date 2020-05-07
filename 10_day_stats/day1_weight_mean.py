n = int(input())
freq = list(map(int, input().split()))
weight = list(map(int, input().split()))

total = 0

for i in range(n):
    total += freq[i] * weight[i]
print(round(total/sum(weight), 1))
