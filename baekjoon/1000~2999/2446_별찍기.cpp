#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);
	
	int N;
	string str;

	cin >> N;

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j < i; j++) {
			cout << " ";
		}

		for (int j = 1; j <= 2*(N-i) + 1; j++) {
			cout << "*";
		}
		cout << "\n";
	}

	for (int i = 1; i < N; i++) {
		for (int j = 1; j <= N - i - 1; j++) {
			cout << " ";
		}

		for (int j = 1; j <= 2 * i + 1; j++) {
			cout << "*";
		}
		cout << "\n";
	}


	return 0;
}