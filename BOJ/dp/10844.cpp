#include<iostream>
using namespace std;

int main(void){
    int n;cin>>n;
    int dp[n+1];
    dp[1]=9;
    for(int i=2;i<=n;i++)
        dp[i]=(dp[i-1]+dp[i-1]-i+1)%1000000000;
    cout<<dp[n]<<endl;
}