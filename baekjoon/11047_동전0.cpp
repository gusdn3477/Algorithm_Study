#include <iostream>

using namespace std;

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);
	
	int N, M;
	int arr[10] = { 0 };
	int count = 0;
	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	for (int i = N - 1; i >= 0; i--) {
		if (M / arr[i]) {
			count = count + M / arr[i];
			M = M % arr[i];
		}
	}

	cout << count;
	return 0;
}
