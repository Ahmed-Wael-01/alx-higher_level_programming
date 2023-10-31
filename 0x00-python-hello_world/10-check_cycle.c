#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to head of list.
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle;
	listint_t *rabbit;

	if (list == NULL)
		return (0);
	turtle = list;
	rabbit = list;

	while (1)
	{
		turtle = turtle->next;
		if (turtle == NULL)
			return (0);
		rabbit = rabbit->next->next;
		if (rabbit == NULL)
			return (0);

		if (turtle == rabbit)
			return (1);
	}
	return (0);
}
