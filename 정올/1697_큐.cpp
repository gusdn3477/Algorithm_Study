#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);
	
	int N,b;
	queue<int> s;
	char a;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> a;
		if (a == 'i') {
			cin >> b;
			s.push(b);
		}

		else if (a == 'c') {
			cout << s.size() << "\n";
		}

		else if (a == 'o') {

			if (s.empty()) {
				cout << "empty\n";
			}

			else {
				b = s.front();
				s.pop();
				cout << b << "\n";
			}
		}
	}


	return 0;
}