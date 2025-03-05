#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    // 1. Get current time
    time_t currentTime = time(NULL);

    // 2. Seed with current time
    srand((unsigned int) currentTime);

    // 3. Generate the same first random number
    unsigned int predictedRand = rand();

    // 4. Print it out
    printf(" %u\n",
           predictedRand);

    return 0;
}
