#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to start of linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *cisfuck;
	
	current = list;
	cisfuck = list;

	while (current != NULL && cisfuck != NULL && cisfuck->next != NULL)
	{
		cisfuck = cisfuck->next;
		current = current->next->next;
		if (current == cisfuck )
			return (1);
	}
	return (0);
}
