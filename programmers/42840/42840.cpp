#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers)
{
  vector<int> result;

  int first[5] = {1, 2, 3, 4, 5};
  int second[8] = {2, 1, 2, 3, 2, 4, 2, 5};
  int third[10] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

  int count_1 = 0, count_2 = 0, count_3 = 0;

  for (int i = 0; i < answers.size(); i++)
  {
    if (first[i % 5] == answers[i])
      count_1++;
    if (second[i % 8] == answers[i])
      count_2++;
    if (third[i % 10] == answers[i])
      count_3++;
  }

  int maxCount = max({count_1, count_2, count_3});

  if (maxCount == count_1)
    result.push_back(1);
  if (maxCount == count_2)
    result.push_back(2);
  if (maxCount == count_3)
    result.push_back(3);

  return result;
}
