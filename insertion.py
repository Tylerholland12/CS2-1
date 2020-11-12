def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    indexing_len = range(1, len(items))
    for i in indexing_len:
        value_to_sort = items[i]

        while items[i-1] > value_to_sort and i>0:
            items[i], items[i-1] = items[i-1], items[i]
            i = i -1

    
    return items

items = [12, 42, 1, 3, 4, 9]
print(insertion_sort(items))

