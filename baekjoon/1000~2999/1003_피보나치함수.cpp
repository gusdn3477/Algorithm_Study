#include <iostream>

using namespace std;

int arr[42] = { 0 };
int arr2[42] = { 0 };

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);

	int T,N,M,K;
	cin >> T;

	arr[0] = 1;
	arr[1] = 0;
	arr2[0] = 0;
	arr2[1] = 1;

	for (int i = 0; i < T; i++) {
		cin >> M;
		for (int j = 0; j < M; j++) {
			arr[j + 2] = arr[j + 1] + arr[j];
			arr2[j + 2] = arr2[j + 1] + arr2[j];
		}
		cout << arr[M] << " " << arr2[M] << "\n";
	}
	
	return 0;
}