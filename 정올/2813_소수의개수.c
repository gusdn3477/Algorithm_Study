#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

int arr[2000000];

int main(void) {

	int M, N;
	int count = 0;

	scanf("%d %d", &M, &N);
	arr[0] = 1;
	arr[1] = 1;

	for (int i = 2; i <= sqrt(N); i++) {
		for (int j = i + i; j <= N; j += i) {
			if (arr[j] == 0) {
				arr[j] = 1;
			}
		}
	}
	for (int i = M; i <= N; i++) {
		if (arr[i] == 0)
			count++;
	}

	printf("%d", count);

	return 0;
}
