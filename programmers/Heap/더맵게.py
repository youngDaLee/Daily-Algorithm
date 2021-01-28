import heapq


def solution(scoville, K):
    answer = 0
    scoville = sorted(scoville)

    while scoville[0] < K:
        answer += 1
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        s = s1 + s2*2

        if s >= k:
            return answer

        heapq.heappush(scoville, s)

    answer = -1
    return answer


scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville, k))
