#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

int main(void) {

	int N, M;
	int i, j;
	int flag = 1;
	int arr[10000] = { 0 };

	scanf("%d %d", &N, &M);

	for (i = N; i <= M; i++) {
		flag = 0;

		if(i == 1)
			continue;
		for (j = 2; j <= sqrt(i); j++) {
			if (i%j == 0) {
				flag = 1;
				break;
			}
		}
		if (flag == 0) {
			printf("%d\n", i);
		}
	}


	return 0;
}