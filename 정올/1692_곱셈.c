#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int N, M;
	int a, b, c, total;
	scanf("%d", &N);
	scanf("%d", &M);

	a = N * (M % 10);
	M /= 10;
	b = N * (M % 10);
	M /= 10;
	c = N * (M % 10);

	total = a + b * 10 + c * 100;
	printf("%d\n%d\n%d\n%d", a, b, c, total);
	
	return 0;
}