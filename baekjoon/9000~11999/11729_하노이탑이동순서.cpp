#include <iostream>

using namespace std;

void hanoi(int n, int start, int mid, int end);
int hanoi_sum(int n);

int main(void) {

	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int N;
	long long int s = 0;
	cin >> N;

	int a = hanoi_sum(N);
	cout << a << "\n";
	hanoi(N, 1, 2, 3);

	return 0;
}

void hanoi(int n, int start, int mid, int end) {

	if (n == 1)
		cout << start << " " << end << "\n";

	else {
		hanoi(n - 1, start, end, mid);
		cout << start << " " << end << "\n";
		hanoi(n - 1, mid, start, end);
	}
}

int hanoi_sum(int n) {

	int start = 1;
	for (int i = 0; i < n; i++)
		start *= 2;

	return start - 1;
}