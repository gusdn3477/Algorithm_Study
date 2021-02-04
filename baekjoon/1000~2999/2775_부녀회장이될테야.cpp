#include <iostream>
#include <stack>
using namespace std;

int arr[15][15];

int stair(int x, int y);

int main(void) {

	cin.tie(NULL);
	ios::sync_with_stdio(false);

	for (int i = 1; i <= 14; i++)
		arr[0][i] = i;

	int T, k, n;
	int p;
	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> k >> n;
		p = stair(k,n);
		cout << p << "\n";
	}

	return 0;
}

int stair(int x, int y) {

	if (x == 0)
		return y;

	if (arr[x][y] != 0)
		return arr[x][y];

	else {
		for (int i = 1; i <= y; i++)
			arr[x][y] += stair(x-1, i);

		return arr[x][y];
	}
}