#include <stdio.h>

int fatorial(int number){
    if(number == 0 || number == 1){
        return number;
    }
    return number * fatorial(number - 1);
}

int main(){
    int number;
    int result;

    printf("Number: ");
    scanf("%d", &number);

    result = fatorial(number);

    printf("result: %i", result);

    return 0;
}
