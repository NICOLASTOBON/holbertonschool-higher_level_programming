#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: is a parameter
 * Return: if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int len, j, result, *array;

	if (*head == NULL)
		return (1);
	for (len = 0; current != NULL; len++)
		current = current->next;
	current = *head;
	array = malloc(sizeof(int) * len);
	if (array == NULL)
		return (EXIT_FAILURE);
	for (j = 0; current != NULL; j++)
	{
		array[j] = current->n;
		current = current->next;
	}
	result = check_palindrome(array, len);
	return (result);
}
/**
 * check_palindrome - is a palindrome.
 * @array: is a parameter
 * @len: is a length list
 * Return: if it is not a palindrome, 1 if it is a palindrome
 */
int check_palindrome(int *array, int len)
{
	int i = 0, j = len - 1;

	for (i = 0; i < j; i++, j--)
	{
		if (array[i] == array[j])
			continue;
			else if (array[i] != array[j])
            break;
    }
    if (array[i] != array[j])
    {
        free(array);
        return (0);
    }
    free(array);
    return (1);
}
