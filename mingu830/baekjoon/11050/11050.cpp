#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  int n, k;
  cin >> n >> k;

  vector<int> factorial(n + 1, 1);
  for (int i = 2; i <= n; i++)
  {
    factorial[i] = factorial[i - 1] * i;
  }

  cout << factorial[n] / (factorial[k] * factorial[n - k]) << '\n';

  return 0;
}