#include <stdio.h>

int main(void) {

	int A, B;
	int N, P, Q, R, S, W;

	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		scanf("%d %d %d %d %d", &P, &Q, &R, &S, &W);
		A = W * P;

		if (W - R > 0) {
			B = Q + S * (W - R);
		}
		else {
			B = Q;
		}

		printf("#%d ", i + 1);
		if (A < B)
			printf("%d\n", A);
		else
			printf("%d\n", B);
	}

	return 0;
}