#include<iostream>
#include<vector>
using namespace std;

vector<int> setAlign(int n, long long k)
{
  vector<int> answer;
  
  // Make factorial and sequential vectors
  vector<long long> fac(1,0);
  vector<int> seq(1,0);
  long long mul = 1;
    
  for (int i=1; i<=n; ++i){
    seq.push_back(i);
    mul *= i;
    fac.push_back(mul);
    //cout << seq[i] << '/' << fac[i] <<endl;
  }
  
  int num = n;
  long long ki = k, mod, rem;    
  while (num>1){
    --num;
    mod = ki / fac[num];
    rem = ki % fac[num];
    if (rem != 0){
      answer.push_back(*(seq.begin()+(mod+1)));
      seq.erase(seq.begin()+(mod+1));
      ki = rem;
    }
    else{
      answer.push_back(*(seq.begin()+mod));
      seq.erase(seq.begin()+mod);
      if(num==1){
        answer.push_back(*(seq.begin()+1));
      }
      ki = fac[num];
    }
  }
  return answer;
}

int main()
{
  int testn = 4;
  long long testcnt = 24;
  vector<int> testAnswer = setAlign(testn,testcnt);
  // 아래는 테스트로 출력해 보기 위한 코드입니다.

  for(int i=0; i< testAnswer.size(); i++)
  {
    cout << testAnswer[i] << " ";
  }
}