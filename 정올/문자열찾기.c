#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void) {

	char name[10001] = { '\0' };
	int len;
	int count = 0;
	int count2 = 0;

	scanf("%s", name);
	len = strlen(name);

	for (int i = 0; i < len - 2; i++) {
		if (name[i] == 'K' && name[i + 1] == 'O' && name[i+2] == 'I')
			count++;
		if (name[i] == 'I' && name[i + 1] == 'O' && name[i + 2] == 'I')
			count2++;
	}

	printf("%d\n%d", count, count2);
	return 0;
}

