#include <stdio.h>

int main(void) {

	int i, j, min, index, temp;
	int array[10] = { 1,10,5,8,7, 6,4,3,2,9 };
	for (int i = 0; i < 10; i++) {
		min = 9999; // ������ ū ���� �ξ����ϴ�.
		for (j = i; j < 10; j++) {
			// for���� ����, �ּڰ��� ã�� �ּڰ��� min��, �ּڰ��� �ε����� index�� �����մϴ�.
			if (min > array[j]) {
				min = array[j];
				index = j;
			}
		}
		//���� �տ� �ִ� ���� �ּڰ��� �ٲ��ش�.
		temp = array[i];
		array[i] = array[index];
		array[index] = temp;
	}

	//���� ������ ���, �ð����⵵�� O(N^2)���� ������ �ʽ��ϴ�. 
	for (int i = 0; i < 10; i++)
		printf("%d ", array[i]);

	return 0;
}