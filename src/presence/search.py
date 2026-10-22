def linear_search(
    items: list[str],
    target: str,
) -> int | None:
    for index, item in enumerate(items):
        if item == target:
            return index

    return None


def binary_search(
    items: list[str],
    target: str,
) -> int | None:
    high = len(items) - 1
    low = 0

    while low <= high:
        middle = (low + high) // 2

        if items[middle] == target:
            return middle

        if items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return None


def find_smallest_index(
    numbers: list[int],
    start_index: int,
) -> int:
    smallest_index = start_index

    for index in range(start_index + 1, len(numbers)):
        if numbers[index] < numbers[smallest_index]:
            smallest_index = index

    return smallest_index


def selection_sort(numbers: list[int]) -> list[int]:
    for index, number in enumerate(numbers):  # unused number variable
        smallest_index = find_smallest_index(numbers, start_index=index)

        numbers[index], numbers[smallest_index] = (
            numbers[smallest_index],
            number,
        )

    return numbers


def selection_sorted_copy(
    numbers: list[int],
) -> list[int]:
    numbers_copy = numbers.copy()

    selection_sort(numbers=numbers_copy)

    return numbers_copy
