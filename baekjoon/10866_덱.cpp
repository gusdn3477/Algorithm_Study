#include <iostream>
#include <string>
#include <deque>
using namespace std;

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);

	deque<int> dq;
	int N,a;
	string s;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> s;
		if (s == "push_back") {
			cin >> a;
			dq.push_back(a);
		}

		else if (s == "push_front") {
			cin >> a;
			dq.push_front(a);
		}

		else if (s == "pop_front") {
			if (dq.empty())
				cout << -1 << "\n";

			else {
				a = dq.front();
				dq.pop_front();
				cout << a << "\n";
			}
		}

		else if (s == "pop_back") {
			if (dq.empty())
				cout << -1 << "\n";

			else {
				a = dq.back();
				dq.pop_back();
				cout << a << "\n";
			}
		}

		else if (s == "size") {
			cout << dq.size() << "\n";
		}

		else if (s == "empty") {
			cout << dq.empty() << "\n";
		}

		else if (s == "front") {
			if (dq.empty())
				cout << -1 << "\n";

			else {
				a = dq.front();
				cout << a << "\n";
			}
		}

		else if (s == "back") {
			if (dq.empty())
				cout << -1 << "\n";

			else {
				a = dq.back();
				cout << a << "\n";
			}
		}
	}
	

	return 0;
}