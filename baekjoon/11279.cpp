#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;

int main(void) {

	cin.tie(NULL);
	cin.sync_with_stdio(false);
	priority_queue<int> pq;
	int N, x;

	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> x;

		if (x == 0) {
			if (pq.empty())
				cout << 0 << "\n";

			else {
				int a = pq.top();
				cout << a << "\n";
				pq.pop();
			}
		}
		else
			pq.push(x);
	}

	return 0;
}
