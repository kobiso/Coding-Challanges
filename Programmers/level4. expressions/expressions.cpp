#include<iostream>
using namespace std;
int expressions(int testCase)
{
  int answer = 0;  
  // Loop until half of the testCase, it is unnecessary after then
  for (int i=1; i<=testCase/2; ++i){
    int sum = 0;    
    for (int j=i; j<=testCase; ++j){
      sum += j;
      // If sum is equal to the testCase
      if (sum == testCase){ 
        answer += 1;
        break;
      }
      // Break if sum is bigger than the testCase
      else if (sum > testCase){ 
        break;
      }
    }
  }
  // Plus one to include the testCase itself
  return ++answer;
}

int main()
{
  int testNo = 15;
  int testAnswer = expressions(testNo);

  cout<<testAnswer;
}
