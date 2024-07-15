#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
  int N;
  cin >> N;
  vector<int> num;
  int input;
  while (N--)
  {
    cin >> input;
    num.push_back(input);
  }
  sort(num.begin(), num.end());
  for (int i = 0; i < num.size(); i++)
  {
    cout << num[i] << '\n';
  }

  return 0;
}