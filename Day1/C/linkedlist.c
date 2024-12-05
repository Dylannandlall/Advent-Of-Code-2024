#include "linkedlist.h"
#include <stdlib.h>

void initializeList(Node *node) {
    node->id = 0;
    node->next = NULL;
}

void appendNodeSorted(Node *list, int value) {
    Node *prev_node = NULL;
    Node *new_node = (Node *)malloc(sizeof(Node));
    new_node->id = value; 

    if (list->next == NULL) {
        list->next = new_node;
        return;
    }

    while (list != NULL) {
        if (list->id < new_node->id && prev_node == NULL) {
            new_node->next = list;
            list = new_node->next;
            return;
        }

        if (prev_node != NULL && prev_node->id < new_node->id) {
            if (list == NULL) {
                prev_node->next = new_node;
            }
            if (list != NULL && list->id > new_node->id) {
                prev_node->next = new_node;
                new_node->next = list;
                return;
            }
        }
        
        prev_node = list;
        list = list->next;
    }
}