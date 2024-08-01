#include <bits/stdc++.h>
using namespace std;

int main(){
  int N;
  cin >> N;
    int a;
    cin >> a;
  for (int i = 1; i < N; i++){
    int b;
    cin >> b;
    if(a > b){
      cout <<  i << endl;
      break;
    }
    if(i == N-1){
      cout << -1<< endl;
    }
  }
}