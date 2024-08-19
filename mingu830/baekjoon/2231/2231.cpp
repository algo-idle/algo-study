#include <iostream>

using namespace std;

int main()
{
  int N;
  cin >> N;

  int sum = 0;
  for (int i = 1; i < N; i++)
  {
    int num = i;
    int temp = i;
    while (temp > 0)
    {
      num += temp % 10;
      temp /= 10;
    }
    if (num == N)
    {
      sum = i;
      break;
    }
  }
  cout << sum << '\n';

  return 0;
}