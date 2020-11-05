#include <stdio.h>

int main(void) {

	int i, j, min, index, temp;
	int array[10] = { 1,10,5,8,7, 6,4,3,2,9 };
	for (int i = 0; i < 10; i++) {
		min = 9999; // 임의의 큰 값을 두었습니다.
		for (j = i; j < 10; j++) {
			// for문을 돌며, 최솟값을 찾고 최솟값을 min에, 최솟값의 인덱스를 index에 저장합니다.
			if (min > array[j]) {
				min = array[j];
				index = j;
			}
		}
		//가장 앞에 있는 곳과 최솟값을 바꿔준다.
		temp = array[i];
		array[i] = array[index];
		array[index] = temp;
	}

	//선택 정렬의 경우, 시간복잡도는 O(N^2)으로 빠르지 않습니다. 
	for (int i = 0; i < 10; i++)
		printf("%d ", array[i]);

	return 0;
}