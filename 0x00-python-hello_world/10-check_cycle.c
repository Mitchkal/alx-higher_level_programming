#include "lists.h"
/**
 * check_cycle- checks if a singly linked listhas cycle
 * @list: the linked list
 * Return: 0if no cycle,1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *quick = list;

	if (!list || list->next == NULL)
		return (0);
	/*create fast and sow pointer*/

	while (quick != NULL && quick->next != NULL)
	{
		quick = quick->next->next;
		slow = slow->next;
		if (slow == quick)
			return (1);
	}
	return (0);

}
