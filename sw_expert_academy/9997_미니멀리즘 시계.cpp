#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>

using namespace std;

int main(void) {

	int N, M;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &M);
		printf("#%d %d %d\n", i + 1, (M * 2) / 60, (M * 2) % 60);
	}
	return 0;
}