#include<iostream>
#include<vector>
using namespace std;

string change124(int no){
    string answer = "";
    int a;
    while(no > 0){
        a = no % 3;
        no = no / 3;
        if (a == 0){
            no -= 1;
        }
        // Interesting way to append
        answer = "412"[a] + answer;
    }

    return answer;
}

int main(){    
    int testNo = 10;
    string testAnswer = change124(testNo);

    cout<<testAnswer;
}