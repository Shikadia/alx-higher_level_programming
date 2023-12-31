#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list
 * @head: A pointer the head of the linked list
 * @num: The number to insert
 *
 * Return: returns the new mnode
 */
listint_t *insert_node(listint_t **head, int num)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = num;

	if (!node || node->n >= num)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node && node->next && node->next->n < num)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
