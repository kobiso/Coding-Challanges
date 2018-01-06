#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> setAlign(int n, long long cnt)
{
  vector<int> answer;
  for(int i=1;i<=n; i++) answer.push_back(i);

  long long i=1;
  do {
    if(cnt==i++) break;
  }while(next_permutation(answer.begin(),answer.end()));

  return answer;
}
int main()
{
  int testn = 4;
  long long testcnt = 6;
  vector<int> testAnswer = setAlign(testn,testcnt);
  
  for(int i=0; i< testAnswer.size(); i++)
  {
    cout << testAnswer[i] << " ";
  }
}