#include <iostream>
#include <string>
#include <map>
using namespace std;

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);

	string s;
	map<char, int> m;
	for (int i = 0; i < 26; i++)
		m['a' + i] = 0;

	cin >> s;

	for (int i = 0; i < s.size(); i++) {
		m[s[i]]++;
	}

	for (char i = 'a'; i <= 'z'; i++)
		cout << m[i] << " ";
	
	return 0;
}