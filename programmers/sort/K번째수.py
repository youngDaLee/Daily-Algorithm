def solution(array, commands):
    answer = [0] * len(commands)
    cnt = 0

    for c in commands:
        arr = [0] * (c[1]-c[0]+1)

        i_cnt = 0
        for i in range(c[0]-1, c[1]):
            arr[i_cnt] = array[i]
            i_cnt += 1

        arr.sort()

        answer[cnt] = arr[c[2]-1]
        cnt += 1

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

arr = solution(array, commands)
print(arr)
