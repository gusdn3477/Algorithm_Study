#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void) {

	int T;
	int arr[10] = { 0 };
	int temp;

	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		for (int j = 0; j < 10; j++) {
			scanf("%d", &arr[j]);
		}

		for (int i = 0; i < 9; i++) {
			for (int j = i+1; j < 10; j++) {
				if (arr[i] < arr[j]) {
					temp = arr[j];
					arr[j] = arr[i];
					arr[i] = temp;
				}
			}
		}
		printf("%d\n", arr[2]);
	}
	return 0;
}