#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  int x, y;
  cin >> x >> y;
  vector<int> month = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  vector<string> day = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
  int today = 0;
  for (int i = 0; i < x - 1; i++)
  {
    today += month[i];
  }
  today += y;
  cout << day[today % 7] << '\n';
  return 0;
}