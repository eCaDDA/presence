from presence.search import binary_search, linear_search, selection_sort


def test_search_returns_index():
    items = ["Adam", "Ben", "Chris"]

    assert linear_search(items=items, target="Adam") == 0
    assert linear_search(items=items, target="Ben") == 1
    assert linear_search(items=items, target="Mariah") is None


def test_binary_search_finds_middle_item():
    items = ["Adam", "Ben", "Chris", "Mia", "Zoe"]

    assert binary_search(items, "Chris") == 2


def test_binary_search_finds_item_near_end():
    items = ["Adam", "Ben", "Chris", "Mia", "Zoe"]

    assert binary_search(items, "Mia") == 3


def test_binary_search_returns_none_when_target_missing():
    items = ["Adam", "Ben", "Chris", "Mia", "Zoe"]

    assert binary_search(items, "Sarah") is None


def test_selection_sort_orders_numbers():
    numbers = [7, 3, 9, 2, 5]

    result = selection_sort(numbers=numbers)

    assert result == [2, 3, 5, 7, 9]


def test_selection_sort_handles_already_sorted_numbers():
    numbers = [2, 3, 5, 7, 9]

    result = selection_sort(numbers=numbers)

    assert result == [2, 3, 5, 7, 9]


def test_selection_sort_handles_empty_list():
    numbers = []

    result = selection_sort(numbers=numbers)

    assert result == []
