#include <iostream>
#include <string>
#include <algorithm>
#include <deque>

using namespace std;


int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);

	int N, M;
	int count = 0;
	string s;
	deque<string> d, d2, d3;
	deque<string>::iterator iter;

	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		cin >> s;
		d.push_back(s);
	}

	for (int i = 0; i < M; i++) {
		cin >> s;
		d2.push_back(s);
	}

	sort(d.begin(), d.end());
	sort(d2.begin(), d2.end());

	if (N > M) {
		for (int i = 0; i < M; i++) {
			if (binary_search(d.begin(), d.end(), d2[i])) {
				d3.push_back(d2[i]);
				count++;
			}
		}
	}

	else {
		for (int i = 0; i < N; i++) {
			if (binary_search(d2.begin(), d2.end(), d[i])) {
				d3.push_back(d[i]);
				count++;
			}
		}
	}

	cout << count << "\n";
	for (int i = 0; i < d3.size(); i++) {
		cout << d3[i] << "\n";
	}
	return 0;
}