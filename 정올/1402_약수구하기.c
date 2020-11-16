#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int N, K;
	int count = 0;
	int flag = 0;

	scanf("%d %d", &N, &K);

	for (int i = 1; i <= N; i++) {
		flag = 0;
		if (N % i == 0) {
			count++;
		}
		if (count == K) {
			printf("%d", i);
			break;
		}
	}

	if (count != K)
		printf("0");

	return 0;
}