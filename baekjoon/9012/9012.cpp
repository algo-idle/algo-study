#include <iostream>

using namespace std;

int main()
{
  int T;
  cin >> T;
  while (T--)
  {
    string s;
    cin >> s;
    int count = 0;
    for (int i = 0; i < s.size(); i++)
    {
      if (s[i] == '(')
        count++;
      else
        count--;
      if (count < 0)
        break;
    }
    if (count == 0)
      cout << "YES\n";
    else
      cout << "NO\n";
  }
  return 0;
}