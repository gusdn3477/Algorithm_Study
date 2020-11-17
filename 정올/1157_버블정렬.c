#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int N;
	int arr[100] = { 0 };
	int temp;

	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}


	for (int i = 0; i < N - 1; i++) {
		for (int j = 0; j < N - i - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}

		for (int k = 0; k < N; k++) {
			printf("%d ", arr[k]);
		}
		printf("\n");
	}

	return 0;
}