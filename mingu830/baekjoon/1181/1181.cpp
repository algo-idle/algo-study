#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  int n;
  cin >> n;

  vector<string> words(n);
  for (int i = 0; i < n; i++)
  {
    cin >> words[i];
  }

  sort(words.begin(), words.end(), [](const string &a, const string &b)
       {
    if (a.size() == b.size())
    {
      return a < b;
    }
    return a.size() < b.size(); });

  for (int i = 0; i < n; i++)
  {
    if (i > 0 && words[i] == words[i - 1])
    {
      continue;
    }
    cout << words[i] << '\n';
  }

  return 0;
}