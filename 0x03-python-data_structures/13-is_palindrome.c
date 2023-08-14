#include "lists.h"
/**
 * is_palindrome - checks if linked list is palindrome
 * @head: pointer to head of list
 * Return: true or false
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *prev = NULL;
	listint_t *temp = NULL;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	/*reverse second half*/
	while (slow != NULL)
	{
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}
	/*compare to check if content of reverses matches that of head*/
	while (prev != NULL)
	{
		if (prev->n != (*head)->n)
			return (0);
		prev = prev->next;
		*head = (*head)->next;
	}
	return (1);
}
