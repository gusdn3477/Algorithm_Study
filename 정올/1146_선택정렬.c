#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int N;
	int arr[100] = { 0 };
	int temp, flag;
	int index, min;

	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}

	for (int i = 0; i < N - 1; i++) {
		min = arr[i];
		flag = 0;
		for (int j = i+1; j < N; j++) {
			if (arr[j] < min) {
				flag = 1;
				min = arr[j];
				index = j;
			}
		}

		if (flag == 1) {
			temp = arr[i];
			arr[i] = arr[index];
			arr[index] = temp;
		}

		for (int k = 0; k < N; k++) {
			printf("%d ", arr[k]);
		}
		printf("\n");
	}

	return 0;
}