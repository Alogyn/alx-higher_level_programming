#include "lists.h"

/* Task 10. Linked list cycle */

/**
  * check_cycle - checks if a singly linked list has a cycle in it
  *
  * @list: pointer to the head of the linked list
  *
  * Return: 0 if there is no cycle, 1 if there is a cycle
  */
int check_cycle(listint_t *list)
{
    listint_t *slow = list, *fast = list;

    /* Loop while 'slow', 'fast', and 'fast->next' are not NULL */
    while (slow && fast && fast->next)
    {
	/* Move 'slow' one step at a time */
        slow = slow->next;

	/* Move 'slow' one step at a time */
        fast = fast->next->next;

	/* If 'slow' and 'fast' meet at the same node, there is a cycle */
        if (slow == fast)
            return (1);
    }

    /* If the loop completes without finding a cycle, return 0 */
    return (0);
}
