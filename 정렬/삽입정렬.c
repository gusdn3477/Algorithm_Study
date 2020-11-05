#include <stdio.h>

int main(void) {

	int i, j, temp;
	int arr[10] = { 1,10,5,8,7,6,4,3,2,9 };

	for (i = 0; i < 9; i++) {
		j = i;
		// 해당 요소가 다음 요소보다 크다면, 둘이 바꿔준다. 그 후, 인덱스를 감소시켜가며 같은 동작을 한다.
		// 만약 정렬이 되어 있다면 while문이 실행되지 않기 때문에 정렬되지 않은 경우 상당히 효율적이다.
		while (arr[j] > arr[j + 1]) {
			temp = arr[j];
			arr[j] = arr[j + 1];
			arr[j + 1] = temp;
			j--;
		}
	}
	//최악의 경우(정렬이 하나도 되어있지 않은 경우) 시간 복잡도는 O(N^2)가 된다.
	//실제로는 삽입정렬>선택정렬>버블정렬 순의 속도를 보여준다.
	for (i = 0; i < 10; i++)
		printf("%d ", arr[i]);

	return 0;
}