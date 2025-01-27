#include "lists.h"
#include  <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *p;

	new = malloc(sizeof(listint_t));
	if (new == NULL) return (NULL);

	new->n = number;

	if (*head == NULL || (*head)->n >= new->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	p = *head;
	for (; p != NULL && p->next->n < new->n; p = p->next)
		;
	new->next = p->next;
	p->next = new;
	return (new);
}
