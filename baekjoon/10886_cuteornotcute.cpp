#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);

	map<int, int> m;
	int N,x;

	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> x;
		m[x]++;
	}

	if (m[0] > m[1]) {
		cout << "Junhee is not cute!";
	}

	if (m[0] < m[1]) {
		cout << "Junhee is cute!";
	}



	return 0;
}
