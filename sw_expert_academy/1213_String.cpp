#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {

	string s, ans;
	string::iterator iter;
	int N;
	int len;
	int count = 0;


	for (int tc = 0; tc < 10; tc++) {

		scanf("%d", &N);
		cin >> s;
		cin >> ans;
		count = 0;
		len = s.size();
		for (int i = 0; i < ans.size() - len + 1; i++) {
			if (ans.substr(i, len) == s)
				count++;
		}
		printf("#%d %d\n", tc + 1, count);
	}

	return 0;
}