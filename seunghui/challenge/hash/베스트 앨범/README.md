# 베스트 앨범

## 문제 설명

스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

## 제한 사항

- genres[i]는 고유번호가 i인 노래의 장르입니다.
- plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
- genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
- 장르 종류는 100개 미만입니다.
- 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
- 모든 장르는 재생된 횟수가 다릅니다.

## 예시

### Example 1:

![스크린샷 2024-09-26 051012](https://github.com/user-attachments/assets/70cf184f-0be7-4df9-867e-b84f3dc0d7c2)

# 코드

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

//value값 비교 함수 (재생횟수가 많으면 우선, 재생횟수가 같으면 고유번호가 작은 순)
bool cmp(pair<int, int>& a, pair<int, int>& b) {
    if (a.second == b.second) 
        return a.first < b.first;
    return a.second > b.second;
}

bool cmp2(pair<string, int>& a, pair<string, int>& b) {
    if (a.second == b.second) 
        return a.first < b.first;
    return a.second > b.second;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    // 장르별 재생 횟수를 저장하는 맵
    unordered_map<string, int> genre_play_count;
    // 장르별 곡 목록 (곡 번호와 재생 횟수)
    unordered_map<string, vector<pair<int, int>>> genre_songs;

    // 데이터를 한 번 순회하면서 필요한 정보들을 저장
    for (int i = 0; i < genres.size(); i++) {
        genre_play_count[genres[i]] += plays[i]; // 장르별 총 재생 횟수
        genre_songs[genres[i]].push_back({i, plays[i]}); // 장르별 (곡 번호, 재생 횟수)
    }
    
    for (auto it: genre_songs){
        for (auto it2: it.second){
            std::cout << it.first << " " << it2.first << " " << it2.second << "\n";
        }
    }

    // 장르별로 가장 많이 재생된 순서대로 정렬
    vector<pair<string, int>> sorted_genres(genre_play_count.begin(), genre_play_count.end());
    sort(sorted_genres.begin(), sorted_genres.end(), cmp2);

    vector<int> answer;

    // 장르별로 처리
    for (auto genre : sorted_genres) {
        string genre_name = genre.first;

        // 해당 장르의 노래들을 재생 횟수 순으로 정렬
        vector<pair<int, int>> songs = genre_songs[genre_name];
        sort(songs.begin(), songs.end(), cmp); // 재생 횟수 많고, 같으면 고유번호 작은 순

        // 최대 2개의 곡을 수록
        for (int i = 0; i < songs.size() && i < 2; i++) {
            answer.push_back(songs[i].first); // 곡 번호 추가
        }
    }

    return answer;
}
```

## 채점 결과

![스크린샷 2024-09-26 051035](https://github.com/user-attachments/assets/425dec91-79d2-4df0-88b9-3b88f5c5ec52)


## 어떻게 풀었는지..

처음에 문제 잘못 이해하고 재생 횟수를 더한 값이 아닌 장르의 개수 값으로 생각하고 풀고 틀렸음

그래서 다시 문제를 보고 이해한 뒤 매핑을 어떻게 하면 좋을지 생각하며 풀었음

1. 매핑을 key, value 이렇게 2개의 값으로만 했었는데 다시 풀 때 value에 배열을 추가해서 
장르, 곡 번호, 재생 횟수 이렇게 3개의 값을 같이 묶도록 하였음
2. 그리고 여러 요건 사항과 제한 사항을 고려하여 조건문과 반복문을 이용하여 풀었음
3. 내림차순 정렬 시 value값으로 내림차순 정렬을 하려면 value값 비교 함수가 필요하다는 것을 알고 이용하여 풀었으며, value값을 중심으로 내림차순 정렬을 하기 위해서는 벡터로 변환을 해줘야 했음

++ 테스트 케이스에 뭘 넣어야할지 다른 문제들은 안보였는데 이 문제에서는 보여서 다른 것들도 추가하면서 풀었음 (약간 뿌듯함 증가)
