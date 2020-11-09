#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);
	map<int, int> m;
	map<int, int>::iterator iter;
	vector<pair<int, int>> v;
	vector<int> save;
	int sum = 0;
	int tmp;

	for (int i = 1; i <= 8; i++) {
		cin >> tmp;
		m[i] = tmp;
	}

	for(iter = m.begin(); iter!=m.end(); iter++){

		v.push_back(make_pair(iter->second, iter->first));
	}

	sort(v.begin(), v.end());
	reverse(v.begin(), v.end());

	for (int i = 0; i < 5; i++) {
		sum += v[i].first;
		save.push_back(v[i].second);
	}

	cout << sum << "\n";

	sort(save.begin(), save.end());
	for (int i = 0; i < 5; i++) {
		cout << save[i] << " ";
	}

	return 0;
}