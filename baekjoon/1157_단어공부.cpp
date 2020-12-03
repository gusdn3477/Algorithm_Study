#include <iostream>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int main(void) {

	cin.tie(NULL);
	ios::sync_with_stdio(false);
	
	map<char, int> m;
	map<char, int>::iterator iter;
	string s;
	char c;
	int check = 0;
	int max_ = 0;
	cin >> s;
	
	for (int i = 0; i < s.size(); i++) {
		if (s[i] >= 'a' && s[i] <= 'z')
			s[i] += 'A' - 'a';
	}

	for (int i = 0; i < s.size(); i++) {
		m[s[i]]++;
	}

	for (iter = m.begin(); iter != m.end(); iter++) {
		max_ = max(max_, iter->second);
	}

	for (iter = m.begin(); iter != m.end(); iter++) {
		if (max_ == iter->second) {
			check++;
			c = iter->first;
		}
	}

	if (check != 1)
		cout << "?" << "\n";

	else
		cout << c << "\n";

	return 0;
}
