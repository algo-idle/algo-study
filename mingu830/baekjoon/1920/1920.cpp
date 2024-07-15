#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
  int N, M;
  cin >> N;
  vector<int> A(N);
  for (int i = 0; i < N; i++)
  {
    cin >> A[i];
  }
  cin >> M;
  vector<int> B(M);
  for (int i = 0; i < M; i++)
  {
    cin >> B[i];
  }
  sort(A.begin(), A.end());
  for (int i = 0; i < M; i++)
  {
    cout << binary_search(A.begin(), A.end(), B[i]) << '\n';
  }
  return 0;
}