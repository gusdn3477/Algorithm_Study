#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <cstdio>
#include <stack>

using namespace std;

int main(void) {

	stack<char> st;
	string s;
	int N;
	int check = 0;
	char c;

	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		cin >> s;
		check = 0;
		for (int j = 0; j < s.size(); j++) {
			if (s[j] == '(')
				st.push(s[j]);
			else if (s[j] == ')') {
				if (st.empty() == 1) {
					check = 1;
					break;
				}
				else
					st.pop();
			}
		}

		if (check == 1)
			printf("NO\n");

		else {
			if (st.empty() == 1)
				printf("YES\n");
			else
				printf("NO\n");
		}
		while (st.empty() != 1)
			st.pop();
	}
	return 0;
}
