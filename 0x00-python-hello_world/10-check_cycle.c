#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to head of list.
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *rabbit = list;

	if (list == NULL)
		return (0);

	while (1)
	{
		turtle = turtle->next;
		if (turtle == NULL || rabbit->next == NULL)
			return (0);
		rabbit = rabbit->next->next;
		if (rabbit == NULL)
			return (0);

		if (turtle == rabbit)
			return (1);
	}
	return (0);
}
