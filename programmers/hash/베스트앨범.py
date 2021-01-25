def solution(genres, plays):
    answer = []
    music = list(zip(genres, plays))
    dic = {}
    for i in range(len(music)):
        dic[i+1] = list[i]

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
