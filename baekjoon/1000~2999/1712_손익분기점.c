#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	long long int A, B, C;
	long long int count;

	scanf("%lld %lld %lld", &A, &B, &C);

	if (C > B) {
		count = A / (C - B);
		count++;
	}

	else {
		count = -1;
	}

	printf("%lld", count);

	return 0;
}