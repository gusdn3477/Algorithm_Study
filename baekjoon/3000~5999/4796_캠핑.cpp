#include <iostream>
#include <string>
#include <map>
using namespace std;

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);

	int L, P, V;
	int a, b;
	int count = 1;

	while (1) {
		cin >> L >> P >> V;
		if (L == 0 && P == 0 && V == 0)
			break;

		a = V / P;
		b = V - P * a;
		if(b >= L)
			cout << "Case " << count++ << ": " << L * a + L << "\n";
		
		else {
			cout << "Case " << count++ << ": " << L * a + b << "\n";
		}

	}

	return 0;
}