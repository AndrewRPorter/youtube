# Linked Lists

A linked list is a data structure that allows you to iterate over a list of nodes where each node points to the next node in the list.

A key benefit to a linked list over other data structures, such as an array, is that nodes can be inserted or removed without re-organizing the entire structure.

In this example, we want to highlight the key advantage of using a linked list data structure by implementing our own `insert_at` and `delete_at` methods.

See source for list insert in Python to see how expensive it can be to re-organize every other element in a list upon insertion: https://github.com/python/cpython/blob/main/Objects/listobject.c#L266:L292

## Output

Running this program will output the following

```
[A B D]
[A B C D]  # insertion of Node("C") at index 2
[A B D]  # deletion of Node("C") at index 2
```
