#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

void quickSort(int *data, int start, int end) {

	if (start >= end) { // ���Ұ� 1���� ���
		return;
	}

	int key = start; // Ű�� ù ��° ����
	int i = start + 1;
	int j = end;
	int temp;

	while (i <= j) { //������ ������ �ݺ�
		while (data[i] <= data[key] && i <= end) { // Ű ������ ū ���� ���� �� ���� �̵�
			i++;
		}
		while (data[j] <= data[key] && j > start) { // Ű ������ ���� ���� ���� �� ���� �ݺ�
			j--;
		}
		if (i > j) { //���� ������ ���¸� Ű ���� ��ü
			temp = data[j];
			data[j] = data[key];
			data[key] = temp;
		}
		else {
			temp = data[j];
			data[j] = data[i];
			data[i] = temp;
		}
	}
	quickSort(data, start, j - 1);
	quickSort(data, j+1, end);

}


int main(void) {

	int N;
	int *data = NULL;
	
	scanf("%d", &N);
	data = (int *)malloc(sizeof(int) * N);

	for (int i = 0; i < N; i++) {
		scanf("%d", &data[i]);
	}

	quickSort(data, 0, N - 1);
	for (int i = 0; i < N; i++) {
		printf("%d ", data[i]);
	}

	free(data);
	return 0;
}