#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int gcd(int a, int b);

int main(void) {

	int N, M;
	int a;

	scanf("%d %d", &N, &M);
	a = gcd(N, M);

	printf("%d\n%d", a, N*M/a);
	return 0;
}

int gcd(int a, int b) {

	if (b == 0)
		return a;

	else {
		gcd(b, a%b);
	}
}