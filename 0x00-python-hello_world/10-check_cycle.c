#include "lists.h"
#include <stdio.h>

int check_cycle(listint_t *list) {
	listint_t *fast, *slow;

	fast = slow = list;

	while (slow && fast && fast->next) {
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast) return 1;
	}
	return (0);
}
