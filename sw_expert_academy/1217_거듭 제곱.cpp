#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int func(int x, int y);

int main(void) {

	int N, x, y;

	for (int i = 1; i <= 10; i++) {
		scanf("%d", &N);
		scanf("%d %d", &x, &y);
		printf("#%d %d\n", i, func(x, y));
	}

	return 0;
}

int func(int x, int y) {

	if (y == 1)
		return x;
	else
		return x * func(x, y - 1);
}