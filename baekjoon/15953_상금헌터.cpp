#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <queue>

using namespace std;

long long int result_A(int a);
long long int result_B(int b);

int main(void) {

	cin.tie(NULL);
	cin.sync_with_stdio(false);

	int N;
	int a, b;
	long long int total = 0;
	
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> a >> b;
		total = result_A(a) + result_B(b);
		cout << total << "\n";
	}
	return 0;
}

long long int result_A(int a) {

	if (a == 0)
		return 0;

	else if (a == 1)
		return 5000000;

	else if (a >= 2 && a <= 3)
		return 3000000;

	else if (a >= 4 && a <= 6)
		return 2000000;

	else if (a >= 7 && a <= 10)
		return 500000;

	else if (a >= 11 && a <= 15)
		return 300000;

	else if (a >= 16 && a <= 21)
		return 100000;

	else
		return 0;

}

long long int result_B(int a) {

	if (a == 0)
		return 0;

	else if (a == 1)
		return 5120000;

	else if (a >= 2 && a <= 3)
		return 2560000;

	else if (a >= 4 && a <= 7)
		return 1280000;

	else if (a >= 8 && a <= 15)
		return 640000;

	else if (a >= 16 && a <= 31)
		return 320000;

	else
		return 0;

}