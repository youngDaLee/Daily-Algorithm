# 프로그래머스


### 문제 이해하기


### 문제 접근 방법


### 구현 배경 지식


### 접근 방법을 적용한 코드
```
def solution(array, commands):
    answer = [0] * len(commands)
    # an =[] 공간 설정을 할 필요 없어서 이렇게 해도 됨 -> 오류가 나는 이유는 할당을 해서. append를 해야 오류가 안남.
    # an = list() 이렇게 해도 됨
    cnt = 0

    for c in commands:  # comands 개수만큼 반복
        arr = [0] * (c[1]-c[0]+1)  # [i,j,k]에서 j-i+1길이의 배열새엇ㅇ

        i_cnt = 0
        for i in range(c[0]-1, c[1]):  # i~j까지 증가, arr에 넣음
            arr[i_cnt] = array[i]
            i_cnt += 1
            # .append() 사용

        arr.sort()  # arr 정렬

        answer[cnt] = arr[c[2]-1]  # 정답 배열(answer)에 k번째 수 넣기
        cnt += 1

    return answer

```
