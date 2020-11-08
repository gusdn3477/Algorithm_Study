#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);

	long long int N, K, M;
	vector<long long int> v;

	cin >> N >> K;

	for (int i = 0; i < N; i++) {
		cin >> M;
		v.push_back(M);
	}

	sort(v.begin(), v.end());

	cout << v[K - 1];

	return 0;
}