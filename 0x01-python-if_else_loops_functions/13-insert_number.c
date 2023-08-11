#include "lists.h"
#include <stddef.h>
/**
 * insert_node - inserts number into sorted singyinkedlist
 * @head:pointer to list head
 * @number: number to insert
 * Return: the new node address
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *new_node = NULL;

	if (head == NULL)
		return (NULL);

	new_node = (listint_t *)malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	if (!prev)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		prev->next = new_node;
		new_node->next = current;
	}
	return (new_node);
}
