#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(void) {

	cin.tie(0);
	cin.sync_with_stdio(false);
	string str;

	for (int i = 0; i < 100; i++) {
		getline(cin, str);
		cout << str << "\n";
	}
	return 0;
}