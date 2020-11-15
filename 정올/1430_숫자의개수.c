#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main(void) {

	long long int A, B, C,D;
	int arr[10] = { 0 };

	scanf("%lld", &A);
	scanf("%lld", &B);
	scanf("%lld", &C);

	D = A * B * C;

	while (D > 0) {
		arr[D % 10]++;
		D /= 10;
	}

	for (int i = 0; i < 10; i++) {
		printf("%d\n", arr[i]);
	}
	return 0;
}