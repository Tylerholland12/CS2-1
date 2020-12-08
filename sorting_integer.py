#!python
from sorting_recursive import merge, merge_sort, quick_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    # Use a hashtable to store counts of numbers 
    hashTable = {}
    # New variable for empty array
    sorted_list = []

    # Loop through numbers and add them to hashtable
    for num in numbers:
        if num in hashTable:
            hashTable[num] += 1 
        else:
            hashTable[num] = 1 
    # Loop through hashtbale and sort the keys then add the number to new sorted list
    for k,v in sorted(hashTable.items()):
        # Loop though values and add appropriate key
        for i in range(v):
            sorted_list.append(k)

    # Return sorted list 
    return sorted_list

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)

    # TODO: Create list of buckets to store numbers in subranges of input range

    # TODO: Loop over given numbers and place each item in appropriate bucket

    # TODO: Sort each bucket using any sorting algorithm (recursive or another)

    # TODO: Loop over buckets and append each bucket's numbers into output list

    # FIXME: Improve this to mutate input instead of creating new output list

    # create new empty array
    new_buckets = []
    # loop over list and put them in the empty array
    for i in range (len(numbers)):
        new_buckets.append([])

    # loop through numbers and corectly index them
    for num in numbers:
        bucketIndex = num * len(numbers) // (100 + 1)
        new_buckets[bucketIndex].append(num)

    # sort each number in order
    for i in range(len(new_buckets)):
        new_buckets[i] = sorted(new_buckets[i])

    # set original index to zero
    k = 0
    #loop through new bucket and put each number back into original bucket
    for i in range(len(numbers)):
        for j in range(len(new_buckets[i])):
            numbers[k] = new_buckets[i][j]
            k += 1

    # return original bucket
    return numbers