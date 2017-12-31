#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

// Great Common Divisor between two by using Euclidean algorithm
long long gcd(long long A, long long B)
{
  return (A%B == 0 ? B : gcd(B, A%B));
}

long long lcm(long long A, long long B) // Least Common Multiple between two
{
  return A * B / gcd(A,B);
}

long long nlcm(vector<int> num)
{
  long long answer;
  sort (num.begin(), num.end()); // Sort it in ascending order

  answer = num[0];
  for (vector<int>::size_type i = 1; i<num.size(); ++i){
    answer = lcm(num[i], answer);
  }

    return answer;
}

int main()
{
    vector<int> test{2,6,8,14};

    cout << nlcm(test);
}