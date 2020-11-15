#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int arr[40] = { 0 };
	int a, b;
	int sum = 0;
	int sum2 = 0;

	scanf("%d", &a);

	for (int i = 0; i < a; i++)
		scanf("%d", &arr[i]);

	scanf("%d", &b);

	for (int i = 0; i < a; i++) {
		if (b % arr[i] == 0)
			sum += arr[i];

		if (arr[i] % b == 0)
			sum2 += arr[i];
	}

	printf("%d\n%d", sum, sum2);



	return 0;
}
