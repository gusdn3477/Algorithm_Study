#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

int main(void) {

	int N, M;
	int i, j;
	int flag = 1;
	int arr[10000] = { 0 };
	int count = 0;
	int sum = 0;

	scanf("%d", &N);
	scanf("%d", &M);


	for (i = N; i <= M; i++) {
		flag = 0;

		if (i == 1)
			continue;
		for (j = 2; j <= sqrt(i); j++) {
			if (i%j == 0) {
				flag = 1;
				break;
			}
		}
		if (flag == 0) {
			arr[count++] = i;
		}
	}

	if (count == 0)
		printf("-1");

	else {
		for (int i = 0; i < count; i++)
			sum += arr[i];

		printf("%d %d", sum, arr[0]);
	}
	return 0;
}