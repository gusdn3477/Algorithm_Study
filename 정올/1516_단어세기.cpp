#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
using namespace std;

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);
	
	string s;
	string str;
	string::iterator iter;
	map<string, int> m;
	map<string, int>::iterator iter2;
	vector<pair<string, int>> v;

	getline(cin, s);
	while (s != "END") {

		str = "";
		for (iter = s.begin(); iter != s.end(); iter++) {
			
			if (*iter == ' ') {
				m[str]++;
				str = "";
			}

			else if ((iter + 1) == s.end()) {
				str += *iter;
				m[str]++;
				str = "";
			}

			else {
				str += *iter;
			}
		}

		for (iter2 = m.begin(); iter2 != m.end(); iter2++) {
			v.push_back(make_pair(iter2->first, iter2->second));
		}

		sort(v.begin(), v.end());
		for (int i = 0; i < v.size(); i++) {
			cout << v[i].first << " : " << v[i].second << "\n";
		}

		m.clear();
		v.clear();
		getline(cin, s);
	}

	return 0;
}