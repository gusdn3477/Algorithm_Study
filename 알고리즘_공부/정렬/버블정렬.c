#include <stdio.h>

int main(void) {

	int i, j, temp;
	int array[10] = { 1,10,5,8,7,6,4,3,2,9 };

	for (i = 0; i < 10; i++) {
		for (j = 0; j < 9 - i; j++) {
			if (array[j] > array[j + 1]) {
				//값을 대입하는 3번의 연산 때문에 느려진다.
				temp = array[j];
				array[j] = array[j+1];
				array[j + 1] = temp;
			}
		}
	}

	//버블 정렬의 시간 복잡도는 O(N^2)이지만, 사실상 제일 느린 정렬이다.
	for (i = 0; i < 10; i++) {
		printf("%d ", array[i]);
	}

	return 0;
}