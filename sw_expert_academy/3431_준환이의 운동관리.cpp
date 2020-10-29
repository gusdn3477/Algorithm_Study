#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;
int main(void) {

	int N, x, y, z;
	vector<int> v;
	scanf("%d", &N);

	for (int i = 1; i <= N; i++) {
		scanf("%d %d %d", &x, &y, &z);
		v.push_back(x);
		v.push_back(y);
		v.push_back(z);

		if (v[2] < v[0])
			printf("#%d %d\n", i, v[0] - v[2]);
		else if (v[2] > v[0] && v[2] < v[1])
			printf("#%d %d\n", i, 0);
		else if (v[2] > v[1])
			printf("#%d %d\n", i, -1);

		v.clear();
	}

	return 0;
}