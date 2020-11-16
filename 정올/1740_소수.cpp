#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isPrime(int n);

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);
	
	vector<int> v;
	vector<int>::iterator iter;
	int M, N;
	int sum = 0;

	cin >> M;
	cin >> N;

	for (int i = M; i <= N; i++) {
		if (isPrime(i)) {
			v.push_back(i);
		}
	}

	for (iter = v.begin(); iter != v.end(); iter++) {
		sum += *iter;
	}

	if (v.empty())
		cout << -1;

	else {
		cout << sum << "\n";
		cout << v[0];
	}
	return 0;
}

bool isPrime(int n) {

	if (n < 2)
		return false;

	for (int i = 2; i*i <= n; i++)
		if (n % i == 0)
			return false;

	return true;
}