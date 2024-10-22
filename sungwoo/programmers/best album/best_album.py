

def solution(genres, plays):
    answer = []
    info_dict = {}
    sum_dict = {}

    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        if genre not in info_dict:
            info_dict[genre] = [(i, play)]
        else:
            info_dict[genre].append((i, play))
        if genre not in sum_dict:
            sum_dict[genre] = play
        else:
            sum_dict[genre] += play

    for (g, t) in sorted(sum_dict.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(info_dict[g], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))
