def solution(N, number):
    answer = 0

    dp = []
    dp.append([N])
    for i in range(1, 8):
        dp.append([dp[i-1][0]+N*10**i])

    for i in range(8):
        pass

    return answer


N = 5
number = 12
print(solution(N, number))
