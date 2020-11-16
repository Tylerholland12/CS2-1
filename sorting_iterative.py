#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    # loop through list
    for i in range(len(items) - 1):
        # loop through values
        for j in range(i):
            # check if value is greater
            if items[i] > items[j]:
                # increment value
                j+=1
                # return boolean
                return True
            else:
                # return boolean
                return False


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    # items = [5, 3, 8, 12, 2, 1]
    # loop through items in reverse order and stop at 0
    for i in range(len(items) -1,0,-1):
        # loop through to swap or not swap values
        for j in range(i):
            # check if first value is greater than second value
            if items[j] > items[j+1]:
                # create temp value
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp
    return

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    i_length = range(0, len(items) - 1)

    for i in i_length:
        # default set to index
         minimum_value = i

        # loop through all items to the right of i
         for j in range(i + 1, len(items)):
            #  change minimum value if number smaller than minimum value is found
             if items[j] < items[minimum_value]:
                 minimum_value = j 
            
            # switch minimum value with new minimum value
             if minimum_value != i:
                items[minimum_value], items[i] = items[i], items[minimum_value]
    
    return items



def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    indexing_len = range(1, len(items))
    # loop through all values and sort them using the length
    for i in indexing_len:
        sort_value = items[i]

        # loop through to see if value is higher than current value
        # positive index
        while items[i-1] > sort_value and i>0:
            # swap the index
            items[i], items[i-1] = items[i-1], items[i]
            # look at the next item
            i = i -1

    # return list
    return items

if __name__ == "__main__":
    items = [1, 2, 3, 4, 5]
    # items = [5, 3, 8, 12, 2, 1]
    print(is_sorted(items))
    bubble_sort(items)
    print(items)
    print(selection_sort(items))
    print(insertion_sort(items))