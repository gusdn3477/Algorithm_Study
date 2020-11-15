#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void factorial(long long int n);
long long int result(long long int n);

int main(void) {

	long long int x;

	scanf("%lld", &x);
	factorial(x);
	
	printf("%lld", result(x));

	return 0;
}

void factorial(long long int n) {

	if (n == 1) {
		printf("%lld! = %lld\n", n, n);
	}

	else{
		printf("%lld! = %lld * %lld!\n", n, n, n - 1);
		factorial(n - 1);
	}

}

long long int result(long long int n) {

	if (n == 1)
		return 1;

	else
		return n * result(n - 1);
}