#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
	time_t currentTime = time(NULL);
	srand((unsigned int) currentTime);

	for (int i = 0; i < 0x32; i++){
		int ivar = rand() % 100;
		printf("%d\n", ivar);
	}


	return 0;
}
