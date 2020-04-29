#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted linked list.
 * @head: is a parameter
 * @number: is a value
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (head == NULL)
		return (NULL);
	while (current != NULL)
	{
		if (current->n <= number && number <= current->next->n)
		{
			new->n = number;
			new->next = current->next;
			current->next = new;
			return (new);
		}
		else if (current->n >= number)
		{
			new->n = number;
			new->next = *head;
			*head = new;

			return (new);
		}
		else if (current->n <= number && current->next->next == NULL)
		{
			new->n = number;
			new->next = NULL;
			current->next->next = new;
			return (new);
		}
		current = current->next;
	}
	return (NULL);
}
