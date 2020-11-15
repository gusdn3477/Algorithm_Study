#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void) {

	char str[31] = { '\0' };
	char *p = NULL;
	int start = 1;
	int len;
	int sum = 0;

	scanf("%s", str);
	len = strlen(str);
	
	for (p = str; p < str + len; p++) {
		sum = (sum * 2) + *p - '0';
	}

	printf("%d", sum);

	return 0;
}

