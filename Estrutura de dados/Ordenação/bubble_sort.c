#include <stdio.h>

void bubble_sort(int data[], int size){
    int swap;

    for(int v = 0; v < size - 1; v++){
        for(int i = 0; i < size - v - 1; i++){
            if(data[i] > data[i + 1]){
                swap = data[i];
                data[i] = data[i + 1];
                data[i + 1] = swap;
            }
        }
    }
    
    for(int i = 0; i < size; i++){
        printf("%d ", data[i]);
    }
}

int main(){
    int data[] = {5, 8, 3, 4, 1};
    int size = sizeof(data) / sizeof(data[0]);

    bubble_sort(data, size);

    return 0;
}
