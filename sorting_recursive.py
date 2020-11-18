#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # create new empty array
    new_sorted_list = []
    # create a new variable to store the length of each list
    len_items1 = len(items1)
    len_items2 = len(items2)
    # set a variable for each list index and set to 0
    i = j = 0

    # check if index is less than items
    while i < len_items1 and j < len_items2:
        # write a conditional to check if one index is less than the other
        if items1[i] <= items2[j]:
            new_sorted_list.append(items1[i])
            i+=1
        # do the opposite of the first conditional 
        else:
            new_sorted_list.append(items2[j])
            j+=1

    # append the items to the new list
    while i < len_items1:
        new_sorted_list.append(items1[i])
        i+=1
    # append the items to the new list
    while j < len_items2:
        new_sorted_list.append(items2[j])
        j+=1
    
    # return new list
    return new_sorted_list

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # base case
    if len(items) <= 1:
        return items

    # divide array into two parts
    mid = len(items) // 2
    # slice first half of list
    left = items[:mid]
    # slice second half of list
    right = items[mid:]

    # recursive call on left
    left = merge_sort(left)
    # recursive call on right
    right = merge_sort(right)

    # merge two together
    return merge(left, right)

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # base case
    length = len(items)
    if length <= 1:
        return items
    else:
        pivot = items.pop()
    
    # create new empty arrays
    low = []
    high = []

    # loop through and see if the items are greater than pivot
    # append items to high
    for item in items:
        if item > pivot:
            high.append(item)
    
    # append items low
        else:
            low.append(item)
    return quick_sort(low) + [pivot] + quick_sort(high)

if __name__ == "__main__":
    items = [12, 23, 5, 2, 1, 43, 6, 34, 9]
    print(quick_sort(items))
    print(merge_sort(items))