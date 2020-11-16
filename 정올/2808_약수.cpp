#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);

	long long int N;
	vector<long long int> v;
	vector<long long int>::iterator iter;

	cin >> N;

	for (long long int i = 1; i <= sqrt(N); i++) {
		
		if (N % i == 0) {
			v.push_back(i);
			if (N / i != i) {
				v.push_back(N / i);
			}
		}
	}

	sort(v.begin(), v.end());

	for (iter = v.begin(); iter != v.end(); iter++)
		cout << *iter << " ";

	return 0;
}
