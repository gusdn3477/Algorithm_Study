#include <iostream>
#include <stack>
#include <algorithm>
using namespace std;

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);
	
	int N,b;
	stack<int> s;
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
				b = s.top();
				s.pop();
				cout << b << "\n";
			}
		}
	}


	return 0;
}