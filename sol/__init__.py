"""
`sol` provides implementation of [self-organizing](https://en.wikipedia.org/wiki/Self-organizing_list) linked lists.

## What is a *self-organizing* list?

A standard linked list is a data structure that is highly *efficient* at inserting new elements but also the one that is extremely *inefficient* at accessing random elements. Retrieving *n*-th element requires a linear traversal of the list which is an *O(n)* operation.

Self-organization methods are aimed at improving *average* access time by rearranging elements of the list so that the most frequently accessed ones are located at the start of the list.

Currently `sol` supports two self-organizing techniques.

### Move to front

After each successful search operation, the found element is being to the head of the list.

### Transpose

After each successful search operation, the found element is being swapped with its predecessor (if it is not already in the front of the list).
"""


from .doubly_linked_list import List
from .move_to_front_list import MoveToFrontList
from .transpose_list import TransposeList
