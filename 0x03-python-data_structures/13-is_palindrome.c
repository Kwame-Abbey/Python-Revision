#include "lists.h"

listint_t reverse(listint_t *h);
int compare(listint_t *n1, listint_t *n2);

int is_palindrome(listint_t **head)
{
	int res;
	listint_t *p, *slow, *fast;

	slow = fast = *head;

	while (fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	p = reverse(slow->next);
	slow->next = NULL;
	res = compare(*head, p);
	p = reverse(p);
	slow->next = p;
	return (res);
}

listint_t reverse(listint_t *h)
{
	listint_t *prev, *next, *cur;

	prev = next = NULL;
	cur = h;

	while (cur != NULL)
	{
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}

	return (prev);
}

int compare(listint_t *n1, listint_t *n2)
{
	for (; n1 && n2; n1 = n1->next, n2 = n2->next)
	{
		if (n1->n != n2->n) return (0);
	}
	return (1);
}
