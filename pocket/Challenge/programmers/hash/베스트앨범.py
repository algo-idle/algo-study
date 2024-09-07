def solution(genres, plays):
    musics = {}

    for i in range(len(genres)):
        if genres[i] not in musics:
            musics[genres[i]] = []
        musics[genres[i]].append((plays[i], i))

    for genre in list(set(genres)):
        musics[genre].sort(key=lambda x: (-x[0], x[1]))

    musics = list(sorted(musics.items(), key=lambda x: sum(p[0] for p in x[1]), reverse=True))

    answer = []

    for _, pl in musics:
        for p in pl[:2]:
            answer.append(p[1])

    return answer