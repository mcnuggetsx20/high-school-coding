#include <bits/stdc++.h>
using namespace std;

typedef signed long long sll;
typedef unsigned long long ll;

const int E = 1e5 + 7;
const int INF = 1e9;


void solve(){
    sll n, m, a, ans=0; cin >> n >> m;
    vector<vector<sll>>mat(n+1, vector<sll>(m+2));
    vector<vector<pair<sll,sll>>> pref(n+4, vector<pair<sll,sll>>(m+2, {1,1}));
    for(int i = 1; i < n+3; ++i){
        for(int j = 1; j < m+1; ++j){
            if(i<n+1){
                cin >> a;
                mat[i][j]= a;
            }
            else{
                a = mat[i%3][j];
            }
            pref[i][j].first = a*pref[i-1][j-1].first;
            pref[i][j].second = a*pref[i-1][j+1].second;
            if(i>=3){
                if(j==1){
                    ans -= pref[i][j].second;
                }
                else if(j==3){
                    ans += pref[i][j].first;
                }
            }
        }
    }
    cout << ans << '\n';
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int t = 1;
    //cin >> t;
    while(t--){
        solve();
    }
}

