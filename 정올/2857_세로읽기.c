#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void) {

	char str[5][16] = { '\0' };
	int max_len;

	for (int i = 0; i < 5; i++)
		scanf("%s", str[i]);

	max_len = strlen(str[0]);

	for (int i = 1; i < 5; i++) {
		if (max_len < strlen(str[i]))
			max_len = strlen(str[i]);
	}

	for (int i = 0; i < max_len; i++) {
		for (int j = 0; j < 5; j++) {
			if (str[j][i] == '\0') {
				continue;
			}

			else
				printf("%c", str[j][i]);
		}
	}
	
	return 0;
}