# 베스트앨범

## 문제
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다. 

노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

## 제한사항
- genres[i]는 고유번호가 i인 노래의 장르입니다. 
- plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다. 
- genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다. 
- 장르 종류는 100개 미만입니다. 
- 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다. 
- 모든 장르는 재생된 횟수가 다릅니다.

## 예제 입력 1
```text
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
```
## 예제 출력 1
```text
[4, 1, 3, 0]
```

## 코드
```python
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
```
### 코드 설명

- 장르를 키로 한 딕셔너리에 (고유번호, 재생된 횟수) 저장 
- 새로운 딕셔너리에 각 장르별 총 재생된 횟수 저장 
- 각 딕셔너리를 내림차순으로 정렬 후 최대 2개까지 수록 


## 채점 결과
![image](result_img.png)
