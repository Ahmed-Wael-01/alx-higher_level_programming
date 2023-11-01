#include "lists.h"

/**
 * insert_node - inserts a node in a location
 * @head: the head of the list
 * @number: the value number
 *
 * Description: it insertss nodes
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *curr = *head;

	if (head == NULL)
		return (NULL);
	node = malloc(sizeof(listint_t));
	node->n = number;
	if (*head == NULL || curr->n > number)
	{
		node->next = curr;
		*head = node;
		return (node);
	}
	while (curr != NULL)
	{
		if (curr->next == NULL || number < curr->next->n)
		{
			node->next = curr->next;
			curr->next = node;
			return (node);
		}
		curr = curr->next;
	}
	return (NULL);
}
