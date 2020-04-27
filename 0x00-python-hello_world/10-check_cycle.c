#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to start of linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list, *cisfun = list;

	if (list == NULL)
		return (0);
	while (current != NULL && cisfun != NULL)
	{
		cisfun = cisfun->next;
		current->next = current->next;

		if (current == cisfun)
			return (1);
	}
	return (0);
}
