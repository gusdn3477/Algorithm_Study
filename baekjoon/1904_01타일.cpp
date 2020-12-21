#include <iostream> 
using namespace std; 
int N, M; 
int dp[1000001];

int main(void) {

	ios::sync_with_stdio(false);
	cin.tie(0);
	cin >> N;
	
	dp[1] = 1;
	dp[2] = 2;

	for (int i = 3; i <= N; i++) {
		dp[i] = dp[i - 2] % 15746 + dp[i - 1] % 15746;
	}

	cout << dp[N] % 15746;
	return 0; 
}
