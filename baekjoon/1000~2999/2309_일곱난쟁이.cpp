#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {

	cin.sync_with_stdio(false);
	cin.tie(0);

	vector<int> v;
	vector<int> v2;
	int N;
	int save, save2;
	int sum = 0;

	for (int i = 0; i < 9; i++) {
		cin >> N;
		v.push_back(N);
	}

	for (int i = 0; i < 9; i++) {
		sum += v[i];
	}

	for (int i = 0; i < 8; i++) {
		for (int j = i + 1; j < 9; j++) {
			if (sum - (v[i] + v[j]) == 100) {
				save = i;
				save2 = j;
			}
		}
	}

	for (int i = 0; i < 9; i++) {
		if (v[i] != v[save] && v[i] != v[save2])
			v2.push_back(v[i]);
	}

	sort(v2.begin(), v2.end());
	
	for (int i = 0; i < v2.size(); i++) {
		cout << v2[i] << "\n";
	}
	
	return 0;
}