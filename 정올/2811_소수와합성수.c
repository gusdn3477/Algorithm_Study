#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int isPrime(int n);
int isComposite(int n);

int main(void) {

	int arr[5] = { 0 };
	
	for (int i = 0; i < 5; i++)
		scanf("%d", &arr[i]);

	for (int i = 0; i < 5; i++) {

		if (isPrime(arr[i])) {
			printf("prime number\n");
		}

		else if (isComposite(arr[i])) {
			printf("composite number\n");
		}

		else {
			printf("number one\n");
		}

	}

	return 0;
}

int isPrime(int n) {

	if (n < 2)
		return 0;

	for (int i = 2; i*i <= n; i++) {
		if (n % i == 0)
			return 0;
	}

	return 1;
}

int isComposite(int n) {

	int count = 0;

	for (int i = 1; i*i <= n; i++) {
		if (n% i == 0) {
			count++;
			if (n / i != i)
				count++;
		}
	}

	if (count >= 3)
		return 1;
	else
		return 0;
}