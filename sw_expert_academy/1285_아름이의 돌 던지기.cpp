#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {

	vector<int> v;
	vector<int>::iterator iter;

	int N, M, K;
	int min_;
	int count = 0;

	scanf("%d", &N);
	for (int i = 0; i < N; i++) {

		scanf("%d", &M);
		count = 0;
		v.clear();

		for (int j = 0; j < M; j++) {
			scanf("%d", &K);
			v.push_back(K);
		}

		for (iter = v.begin(); iter != v.end(); iter++) {
			if (*iter < 0) {
				*iter = abs(*iter);
			}
		}
		min_ = v[0];
		for (iter = v.begin(); iter != v.end(); iter++) {
			min_ = min(min_, *iter);
		}

		for (iter = v.begin(); iter != v.end(); iter++) {
			if (min_ == *iter)
				count++;
		}
		printf("#%d ", i + 1);
		printf("%d %d\n", min_, count);
	}

	return 0;
}