#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	char name[8][9] = { '\0' };
	char chess[9] = { '\0' };
	int count = 0;

	for (int i = 0; i < 8; i++) {
		scanf("%s", name[i]);
	}

	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			if (i % 2 == 0 && j % 2 == 0 && name[i][j] == 'F')
				count++;
			if (i % 2 == 1 && j % 2 == 1 && name[i][j] == 'F')
				count++;
		}
	}
	printf("%d", count);


	return 0;
}