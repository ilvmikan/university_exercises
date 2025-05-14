#include <stdio.h>
#define MAX_SIZE 255

typedef struct {
    int top;
    int items[MAX_SIZE];
} Stack;

void initialize(Stack *s);
void push(Stack *s, int value);
int pop(Stack *s);
int isEmpty(Stack *s);
int isFull(Stack *s);

void initialize(Stack *s){
   s->top = -1; 
}

int top(Stack *s){
    if(s->top == -1) {
        printf("Empty");
    } 
    
    return s->items[s->top];
}

void all_items(const Stack *s){
    for (int i = 0; i <= s->top; i++) {
        printf("%d -> ", s->items[i]); 
    }
    printf("\n");
}

void push(Stack *s, int value){
    if(isFull(s)){
        printf("pilha cheia");
    }

    s->top++;
    s->items[s->top] = value;
}

int pop(Stack *s){
    int poped;

    if(isEmpty(s)){
        printf("pilha vazia");
    }

    poped = s->items[s->top];
    s->top--;
    return poped;
}

int isEmpty(Stack *s){
    return s->top == -1;
}

int isFull(Stack *s){
    return s->top == MAX_SIZE - 1;
}

int main(){
    Stack stack;
    initialize(&stack);
    
    int data[] = {15, 24, 231, 2, 1, 90, 20};
    int data_size = sizeof(data) / sizeof(data[0]);
    int input;

    for (int i = 0; i < data_size; i++) {
        push(&stack, data[i]); 
    }

    while (input != 0) {
        printf("[1] POP | [2] PUSH | [3] ALL ITEMS\n[4] EMPTY? | [5] FULL? | [6] TOP\n");
        printf("enter your choice (0 to exit): ");
        scanf("%d", &input);

        switch (input) {
            case 1: {
                int value = pop(&stack);
                if (value != -1) {
                    printf("popped: %d\n", value);
                }
                break;
            }
            case 2: {
                int value;
                printf("enter value to push: ");
                scanf("%d", &value);
                push(&stack, value);
                break;
            }
            case 3: {
                all_items(&stack);
                break;
            }
            case 4: {
                if (isEmpty(&stack)) {
                    printf("stack empty\n");
                } else {
                    printf("stack is not empty\n");
                }
                break;
            }
            case 5: {
                if (isFull(&stack)) {
                    printf("stack full\n");
                } else {
                    printf("stack is not full\n");
                }
                break;
            }
            case 6: {
                int value = top(&stack);
                if (value != -1) {
                    printf("top element: %d\n", value);
                }
                break;
            }
            case 0: {
                printf("exiting...\n");
                break;
            }
            default: {
                printf("invalid choice, please try again\n");
            }
        }
    }

    return 0;
}
