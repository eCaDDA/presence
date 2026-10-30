from collections import deque


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


def breadth_first_search(
    graph: dict[str, list[str]],
    start: str,
) -> list[str]:
    queue = deque([start])  # double ended queue object
    visited = {start}  # initialise set with start element
    order = []

    while queue:  # while there are elements in queue
        node = queue.popleft()  # the current node is the leftmost element in queue, also remove this node from queue
        order.append(
            node
        )  # order variable to track search order, should be in breadth first manner

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return order


def depth_first_search(
    graph: dict[str, list[str]],
    start: str,
) -> list[str]:
    stack = [start]
    visited = {start}
    order = []

    while stack:
        node = stack.pop()
        order.append(node)

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)

    return order
