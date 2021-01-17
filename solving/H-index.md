# 프로그래머스


### 문제 이해하기


### 문제 접근 방법


### 구현 배경 지식


### 접근 방법을 적용한 코드
```
def solution(citations):
    answer = 0
    citations.sort()  # 정렬
    for i in range(0, len(citations)):
        if(citations[i] >= len(citations) - i):  # i번째 citation 이상의 논문 개수와 지금 논문의 인용 수 비교
            answer = max(answer, len(citations) - i)  # answer에 저장(max값)

    return answer

```
