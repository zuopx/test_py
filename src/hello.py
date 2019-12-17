# N = int(input())
# ans = []
# for i in range(N):
#     n = int(input())
#     s = list(map(int, input().split()))
#     b = [[0 for i in range(n)] for j in range(n)]
    
#     for i in range(n):
#         b[i][i] = 1

#     for k in range(1, n - 1):
#         for i in range(n - k):
#             j = i + k
#             if b[i][j - 1] == 0 or s[j] <= s[j - 1]:
#                 continue
#             if b[i][j - 1] > 0 and sum(s[i : j]) <= s[j]:
#                 b[i][j] = b[i][j - 1] + 1
#     ans.append(max(sum(b, [])))

# for a in ans:
#     print(a)
