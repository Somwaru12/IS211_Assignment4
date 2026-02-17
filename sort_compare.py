import random
import time

def insertion_sort(a_list):
    start = time.time()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position -= 1

        a_list[position] = current_value

    return time.time() - start


def shell_sort(a_list):
    start = time.time()

    gap = len(a_list) // 2

    while gap > 0:
        for start_pos in range(gap):
            for i in range(start_pos + gap, len(a_list), gap):
                current_value = a_list[i]
                j = i

                while j >= gap and a_list[j - gap] > current_value:
                    a_list[j] = a_list[j - gap]
                    j -= gap

                a_list[j] = current_value

        gap //= 2

    return time.time() - start


def python_sort(a_list):
    start = time.time()
    a_list.sort()
    return time.time() - start

def run_test(sort_fn, lists):
    total = 0.0

    for lst in lists:
        data = lst[:]  
        total += sort_fn(data)

    return total / len(lists)


def main():
    sizes = [500, 1000, 5000]

    for size in sizes:
        lists = []
        for _ in range(100):
            lists.append([random.randint(1, 1000000) for _ in range(size)])

        print(f"\nLIST SIZE = {size}")

        avg_insertion = run_test(insertion_sort, lists)
        print(f"Insertion Sort took {avg_insertion:10.7f} seconds to run, on average")

        avg_shell = run_test(shell_sort, lists)
        print(f"Shell Sort took     {avg_shell:10.7f} seconds to run, on average")

        avg_python = run_test(python_sort, lists)
        print(f"Python Sort took    {avg_python:10.7f} seconds to run, on average")


if __name__ == "__main__":
    main()