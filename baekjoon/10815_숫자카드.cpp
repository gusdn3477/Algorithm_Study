#include <iostream>
#include <deque>
#include <algorithm>

using namespace std;


int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);

	deque<long long int> v, v2;
	deque<long long int>::iterator iter;

	int T, N;
	int len;
	long long int M;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> M;
		v.push_back(M);
	}

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> M;
		v2.push_back(M);
	}

	sort(v.begin(), v.end());
	
	for (int i = 0; i < v2.size(); i++) {

		if (binary_search(v.begin(), v.end(), v2[i]))
			cout << 1 << " ";
		else
			cout << 0 << " ";

	}

	return 0;
}