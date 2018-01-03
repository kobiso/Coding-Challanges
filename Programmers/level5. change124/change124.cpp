#include<iostream>
#include<vector>
#include<string>
using namespace std;

// Think of it as 'chage123' and change 3 to 4 on the 'answer'
string change124(int no)
{
    string answer = "";

  while (no > 0){
    if (no % 3 == 0){
      answer.insert(0, to_string(4)); // Insert the head of string
      no = no/3 - 1; // Special case
    }
    else{
      int rem = no % 3;
      answer.insert(0, to_string(rem)); // Insert the head of string
      no = no/3;
    }
  }

    return answer;
}
int main()
{
    int testNo = 10;
    string testAnswer = change124(testNo);

    cout<<testAnswer;
}