#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <map>

using namespace std;

int main(void) {

	//cin.tie(0);
	//cin.sync_with_stdio(false);

	map<int, int> m;
	map<int, int>::iterator iter;
	vector<pair<int, int>> v;

	int K, L, num;
	int min_ = 0;
	int size;
	cin >> K >> L;

	min_ = K;
	for (int i = 0; i < L; i++) {
		cin >> num;
		m[num] = i + 1;
	}

	for (iter = m.begin(); iter != m.end(); iter++) {
		v.push_back(make_pair(iter->second, iter->first));
	}

	sort(v.begin(), v.end());

	size = v.size();

	min_ = min(K, size);
	for (int i = 0; i < min_; i++)
		printf("%08d\n", v[i].second);
	//cout << v[i].second << "\n";

	return 0;
}