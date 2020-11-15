#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	long long int n,m;
	long long int sum = 0;
	int count_sum = 0;

	scanf("%lld", &n);

	while (n != 0) {
		sum = 0;
		count_sum = 0;
		m = n;
		while (m > 0) {
			sum = sum * 10 + m % 10;
			count_sum += m % 10;
			m = m / 10;
		}
		printf("%lld %d\n", sum, count_sum);
		scanf("%lld", &n);
	}

	return 0;
}