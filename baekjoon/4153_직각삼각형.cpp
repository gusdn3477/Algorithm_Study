#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);
	vector<int> v;
	int a, b, c;
	
	cin >> a >> b >> c;

	while (a != 0 || b != 0 || c != 0) {
		
		v.push_back(a);
		v.push_back(b);
		v.push_back(c);
		sort(v.begin(), v.end());

		if (v[2] * v[2] == v[0] * v[0] + v[1] * v[1]) {
			cout << "right\n";
		}
		else
			cout << "wrong\n";
		v.clear();
		cin >> a >> b >> c;
	}

	return 0;
}