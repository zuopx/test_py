"""
有K种颜色的小球(K<=10)，每种小球有若干个，总数小于100个。
现在有一个小盒子，能放N个小球(N<=8)，现在要从这些小球里挑出N个小球，放满盒子。
想知道有哪些挑选方式。注：每种颜色的小球之间没有差别。

请按数字递增顺序输出挑选小球的所有方式。

如有3种颜色，每种颜色小球的个数分别为a:1,b:2,c:3，挑出3个小球的挑法有：
003,012,021,102,111,120
"""

results = []

def helper1(K, N, nums: list):
    ans = []
    helper2(K, N, nums, ans)


def helper2(K, N, nums, ans):
    s = sum(ans)
    if s == N:
        helper3(ans, K)
    elif s < N and len(ans) < K:
        for i in range(nums[len(ans)] + 1):
            ans.append(i)
            helper2(K, N, nums, ans)
            ans.pop()
            
def helper3(ans, K):
    s = ''
    for i in ans:
        s = s + str(i)
    s = s + '0' * (K - len(ans))
    results.append(s)

if __name__ == "__main__":
    K = 3
    N = 3
    nums = [1, 2, 3]
    helper1(K, N, nums)
    results.sort()
    print(results)