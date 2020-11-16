#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void change_2(int n);
void change_8(int n);
void change_16(int n);

int main(void) {

	int N, K;

	scanf("%d %d", &N, &K);

	if (K == 2)
		change_2(N);

	else if (K == 8)
		change_8(N);

	else if (K == 16)
		change_16(N);
	
	return 0;
}

void change_2(int n) {

	if (n == 0)
		return;

	else {
		change_2(n / 2);
		printf("%d", n % 2);
	}
}

void change_8(int n) {
	printf("%o", n);
}

void change_16(int n) {
	printf("%X", n);
}