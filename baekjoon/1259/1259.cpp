#include <iostream>
#include <string>

using namespace std;

int main()
{
  while (true)
  {
    string input;
    cin >> input;

    if (input == "0")
    {
      break;
    }

    int length = input.length();
    int count = length / 2;
    bool isPalindrome = true;

    for (int i = 0; i < count; i++)
    {
      if (input[i] != input[length - i - 1])
      {
        isPalindrome = false;
        break;
      }
    }

    if (isPalindrome)
    {
      cout << "yes" << '\n';
    }
    else
    {
      cout << "no" << '\n';
    }
  }
  return 0;
}
