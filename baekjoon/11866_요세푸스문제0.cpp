#include <iostream>
#include <deque>

using namespace std;

int main(void) {

	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int N, M;
	deque<int> q;
	cin >> N >> M;

	for (int i = 1; i <= N; i++)
		q.push_back(i);

	cout << "<";

	while (!q.empty()) {
		for (int i = 0; i < M-1; i++) {
			int a = q.front();
			q.pop_front();
			q.push_back(a);
		}

		if (q.size() != 1) {
			cout << q.front() << ", ";
			q.pop_front();
		}

		else {
			cout << q.front();
			q.pop_front();
		}
	}

	cout << ">";
	return 0;
}