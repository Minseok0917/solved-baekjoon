input()
n = list(input())
answer = 0
for i in range(len(n)):
    answer += (ord(n[i])-96) * 31 ** i
print(answer%1234567891)