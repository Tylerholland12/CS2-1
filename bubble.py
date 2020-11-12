def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    # items = [5, 3, 8, 12, 2, 1]
    for i in range(len(items) -1,0,-1):
        for j in range(i):
            if items[j] > items[j+1]:
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp

items = [5, 3, 8, 12, 2, 1]
bubble_sort(items)
print(items)