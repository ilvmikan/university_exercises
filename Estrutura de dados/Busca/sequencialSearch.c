#include <stdio.h>

int sequentialSearch(const int numbers[], int size, int value) {
    for(int i = 0; i < size; i++) {
        if(numbers[i] == value) {
            return i + 1;            
        }
    }
    return -1;
}

int main() {
    int numbers[] = {10, 5, 3, 9, 12, 20};
    int size = sizeof(numbers) / sizeof(numbers[0]);
    int searchValue;

    for(int i = 0; i < size; i++){
        printf("[%i] ", numbers[i]);
    }

    printf("\nType a number to search: ");
    scanf("%d", &searchValue);

    int foundIndex = sequentialSearch(numbers, size, searchValue);

    if(foundIndex == -1) {
        printf("Value not found.\n");
        return 1;
    }

    printf("The value %d was found at position %d\n", searchValue, foundIndex);

    return 0;
}

