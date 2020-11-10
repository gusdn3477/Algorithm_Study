#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

bool compare(pair<int, string> s, pair<int, string> s2);

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);

	int N;
	string s;
	map<string, int> m;
	map<string, int>::iterator iter;
	vector<pair<int, string>> v;
	vector<pair<int, string>>::iterator iter2;

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> s;
		m[s] = s.size();
	}

	for (iter = m.begin(); iter != m.end(); iter++) {
		v.push_back(make_pair(iter->second, iter->first));
	}

	sort(v.begin(), v.end());

	for (iter2 = v.begin(); iter2 != v.end(); iter2++) {
		cout << iter2->second << "\n";
	}

	return 0;
}

bool compare(pair<int, string> s, pair<int, string> s2) {

	if (s.first < s2.first)
		return true;

	else if (s.second < s2.second) {
		return true;
	}

	return false;
}