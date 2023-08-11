#include "lists.h"
/**
 * check_cycle- checks if a singly linked listhas cycle
 * @list: the linked list
 * Return: 0if no cycle,1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *quick = list->next;

	if (list == NULL || list->next == NULL)
		return (0);
	/*create fast and sow pointer*/

	while (quick != NULL && quick->next != NULL)
	{
		if (slow == quick)
			return (1);
		quick = quick->next->next;
		slow = slow->next;
	}
	return (0);

}
