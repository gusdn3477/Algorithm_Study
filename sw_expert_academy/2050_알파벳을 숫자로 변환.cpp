#include<iostream>
#include <cstdio>
using namespace std;

int main(int argc, char** argv)
{
	char ch[201] = { '\0' };
	char *p = NULL;
	scanf("%s", ch);
	for (p = ch; *p != NULL; p++) {
		printf("%d ", *p - 'A' + 1);
	}

	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}