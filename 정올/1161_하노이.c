#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void hanoi(int n, int start, int mid, int end);

int main(void) {

	int N;

	scanf("%d", &N);
	hanoi(N,1,2,3);

	return 0;
}

void hanoi(int n, int start, int mid, int end) {

	if (n == 1)
		printf("%d : %d -> %d\n", n, start, end);

	else {
		hanoi(n - 1, start, end, mid);
		printf("%d : %d -> %d\n", n, start, end);
		hanoi(n - 1, mid, start, end);
	}

}