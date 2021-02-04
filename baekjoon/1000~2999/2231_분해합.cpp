#include <iostream>

using namespace std;

int main(void) {

	int N;
	int a, b, c;
	int sum = 0;
	int flag = 0;
	cin >> N;

	for (int i = 1; i <= N; i++) {
		a = i;
		sum = 0;
		flag = 0;
		while (a > 0) {
			sum += a % 10;
			a = a / 10;
		}
		sum = sum + i;
		if (sum == N) {
			cout << i << "\n";
			flag = 1;
			break;
		}
	}

	if (flag == 0)
		cout << 0;
	return 0;
}
