#include <stdio.h>
#define MAX_SIZE 100

typedef struct {
    int front;
    int back;
    int items[MAX_SIZE];
} Queue;

void init(Queue *q);
void items(const Queue *q);
int enqueue(Queue *q, int value);
int dequeue(Queue *q);
int first(const Queue *q);
int last(const Queue *q);
int isFull(const Queue *q);
int isEmpty(const Queue *q);

void init(Queue *q){
    q->front = -1;
    q->back = -1;
}

void items(const Queue *q){
    if(isEmpty(q)){
        printf("empty");
        return;
    }

    for (int i = q->front; i <= q->back; i++) {
        printf("%d | ", q->items[i]);
    }

    printf("\n");
}

int enqueue(Queue *q, int value){
    if(isFull(q)){
        printf("full");
        return -1;
    }
    
    if(q->front == -1){
        q->front = 0;
    }

    q->back++;
    q->items[q->back] = value;

    return value;
}

int dequeue(Queue *q){
    if(isEmpty(q)){
        printf("empty\n");
        return -1;
    }

    if(q->back < q->front){
        q->back = -1;
        q->front = -1;
    }

    int item = q->items[q->front];
    q->front++;

    return item;
}

int first(const Queue *q){
    int first = q->items[q->front];
    return first;
}

int last(const Queue *q){
    int last = q->items[q->back];
    return last;
}

int isFull(const Queue *q){
    return q->back == MAX_SIZE -1;
}

int isEmpty(const Queue *q){
    return q->front == -1; 
}

int main(){
    Queue queue;
    init(&queue);

    int choice, value;
    do {
        printf("MENU:\n");
        printf("1. ENQUEUE\n");
        printf("2. DEQUEUE\n");
        printf("3. ALL\n");
        printf("4. FIRST\n");
        printf("5. LAST\n");
        printf("6. EXIT\n");
        printf(">> ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                printf("enqueue: ");
                scanf("%d", &value);
                enqueue(&queue, value);
                break;
            case 2:
                value = dequeue(&queue);
                if (value != -1) {
                    printf("dequeue: %d\n", value);
                }
                break;
            case 3:
                items(&queue);
                break;
            case 4:
                printf("%d\n", first(&queue));
                break;
            case 5:
                printf("%d\n", last(&queue));
                break;
            case 6:
                printf("exiting...\n");
                break;
            default:
                printf("invalid\n");
        }
    } while(choice != 6);

    return 0;
}
