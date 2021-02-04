#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	char name[81] = { '\0' };
	char *p = NULL;
	int len = 0;

	scanf("%s", name);
	for (p = name; *p != '\0'; p++)
		len++;

	printf("%d", len);

	return 0;
}