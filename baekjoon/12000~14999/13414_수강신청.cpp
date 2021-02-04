#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);

	map<string, int> m;
	map<string, int>::iterator iter;
	vector<pair<int, string>> v;

	int K, L;
	string s;
	int min_ = 0;
	int size;
	cin >> K >> L;

	min_ = K;
	for (int i = 0; i < L; i++) {
		cin >> s;
		m[s] = i + 1;
	}

	for (iter = m.begin(); iter != m.end(); iter++) {
		v.push_back(make_pair(iter->second, iter->first));
	}

	sort(v.begin(), v.end());
	
	size = v.size();

	min_ = min(K, size);
	for (int i = 0; i < min_; i++)
		cout << v[i].second << "\n";

	return 0;
}
