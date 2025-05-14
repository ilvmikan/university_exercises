#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
} Node ;

struct Node *insertFront(struct Node *head, int data){
    struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = head;
    return newNode;
}

void printList(struct Node* node) {
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
}

int main() {
    struct Node* head = NULL;

    head = insertFront(head, 1);
    head = insertFront(head, 2);
    head = insertFront(head, 3);

    printf("Linked list elements: ");
    printList(head);

    return 0;
}

