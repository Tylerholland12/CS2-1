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


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    for numbers in range(len(bucket_sort)):
        numbers[0]+=1
    # TODO: Create list of buckets to store numbers in subranges of input range
    new_bucket = []
    # TODO: Loop over given numbers and place each item in appropriate bucket
    for item in range(len(numbers)):
        item[0] + new_bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    if item == 0 or item == 1:
        return item
    elif item > 1:
        return quick_sort(item)
    else:
        return "Something went wrong"
    # TODO: Loop over buckets and append each bucket's numbers into output list
    for buckets in range(len(new_bucket)):
        pass
    # FIXME: Improve this to mutate input instead of creating new output list