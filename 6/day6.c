#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int race(long unsigned time, long unsigned distance) {
    int ways = 0;
    long unsigned reach;
    for (long unsigned hold = 1; hold < time; hold++) {
        reach = (time - hold) * hold;
        if (reach > distance) ways++;
        else if(ways > 0) break;
    }

    return ways;
}


int main(void) {
    FILE* fp = fopen("input", "r");
    if (!fp) {
        perror("Error reading input");
        exit(1);
    }

    fscanf(fp, "Time: "); 
    int times[10] = {0};
    int idx = 0;
    while (fscanf(fp, "%d", &times[idx]) == 1) idx++;

    fscanf(fp, "Distance: "); 
    int distances[10] = {0};
    idx = 0;
    while (fscanf(fp, "%d", &distances[idx]) == 1) idx++;
    
    int total = 1;
    for (int i = 0; i < idx; i++) {
        total *= race(times[i], distances[i]);
    }
    printf("Part 1: %d\n", total);

    long unsigned megatime = 0, megadist = 0;
    for (int i = 0; i < idx; i++) {
        megatime = (megatime * (pow(10, ceil(log10(times[i]))))) + times[i];
        megadist = (megadist * (pow(10, ceil(log10(distances[i]))))) + distances[i];
    }

    printf("Part 2: %d\n", race(megatime, megadist));

    fclose(fp);
    return 0;
}
