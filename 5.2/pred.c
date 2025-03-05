#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
	time_t currentTime = time(NULL);
	srand((unsigned int) currentTime);

	int arr[6] = {0x79, 0x12c97f, 0x135f0f8, 0x74acbc6, 0x56c614e, 0xffffffe2};
	for (int i = 0; i < 6; i++){
		int ivar = rand();
		arr[i] = arr[i] - (ivar%10-1);
	}

	int pred = 0;
	for (int i = 0; i < 6; i++){
		pred += arr[i];
	}

	printf("%d\n", pred);
	return 0;
}
