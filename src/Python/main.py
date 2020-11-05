from src.Python.sorting_algorithms.merge_sort import merge_sort


def main():
    sequence = [11, 10, 9, 8, 7, 6]
    # insertion_sort(sequence)
    merge_sort(sequence, 0, len(sequence) - 1)


if __name__ == '__main__':
    main()
