import time
import random

# function 1
def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    elapsed = time.time() - start
    return found, elapsed

# function 2
def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1

    elapsed = time.time() - start
    return found, elapsed

# function 3
def binary_search_iterative(a_list, item):
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    elapsed = time.time() - start
    return found, elapsed

# function 4
def binary_search_recursive(a_list, item):
    start = time.time()

    def _binary_recursive(lst, item):
        if len(lst) == 0:
            return False
        midpoint = len(lst) // 2
        if lst[midpoint] == item:
            return True
        else:
            if item < lst[midpoint]:
                return _binary_recursive(lst[:midpoint], item)
            else:
                return _binary_recursive(lst[midpoint+1:], item)

    found = _binary_recursive(a_list, item)
    elapsed = time.time() - start
    return found, elapsed


def run_test(search_fn, lists, needs_sorted=False):
    target = 99999999
    total = 0.0

    for lst in lists:
        if needs_sorted:
            lst = sorted(lst)
        _, elapsed = search_fn(lst, target)
        total += elapsed

    return total / len(lists)

# main function that determines the size
def main():
    sizes = [500, 1000, 5000]

    for size in sizes:
        # generate 100 random lists for each size
        lists = []
        for _ in range(100):
            lists.append([random.randint(1, 1000000) for _ in range(size)])

        print(f"\nLIST SIZE = {size}")

        avg_seq = run_test(sequential_search, lists, needs_sorted=False)
        print(f"Sequential Search took {avg_seq:10.7f} seconds to run, on average")

        avg_ord = run_test(ordered_sequential_search, lists, needs_sorted=True)
        print(f"Ordered Sequential Search took {avg_ord:10.7f} seconds to run, on average")

        avg_bin_it = run_test(binary_search_iterative, lists, needs_sorted=True)
        print(f"Binary Search Iterative took {avg_bin_it:10.7f} seconds to run, on average")

        avg_bin_rec = run_test(binary_search_recursive, lists, needs_sorted=True)
        print(f"Binary Search Recursive took {avg_bin_rec:10.7f} seconds to run, on average")


if __name__ == "__main__":
    main()