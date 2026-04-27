# SearchSortLab.py
# Name: Valentina Rodriguez
# Date: 04/25/2026
# Assignment: Lab 13 – Searching and Sorting


def linearSearch(data, target):
    """Return the index of target if found, otherwise return -1."""

    for index, value in enumerate(data):
        if value == target:
            return index

    return -1


def bubbleSort(data, trackStats=False):
    """Sort the list using bubble sort and return the sorted list.

    If trackStats is True, return a tuple: (sorted_list, stats_dict).
    """

    n = len(data)
    comparisons = 0
    swaps = 0
    passes = 0

    for i in range(n):
        swapped = False
        passes += 1
        for j in range(0, n - i - 1):
            comparisons += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swaps += 1
                swapped = True

        # If no swaps happened, the list is already sorted.
        if not swapped:
            break

    if trackStats:
        stats = {
            "passes": passes,
            "comparisons": comparisons,
            "swaps": swaps,
        }
        return data, stats

    return data


def main():
    # Test lists
    sortedList = [1, 2, 3, 4, 5]
    reversedList = [5, 4, 3, 2, 1]
    randomList = [3, 1, 4, 2, 5]
    lists = {
        "sortedList": sortedList,
        "reversedList": reversedList,
        "randomList": randomList,
    }

    print("=== Linear Search Results ===")
    for listName, values in lists.items():
        print(f"{listName}: {values}")
        print("  search for 4 ->", linearSearch(values, 4))
        print("  search for 10 ->", linearSearch(values, 10))

    print("\n=== Bubble Sort Results ===")
    sortStats = {}
    for listName, values in lists.items():
        sortedValues, stats = bubbleSort(values.copy(), trackStats=True)
        sortStats[listName] = stats
        print(f"{listName} sorted -> {sortedValues}")
        print(
            "  stats:"
            f" passes={stats['passes']},"
            f" comparisons={stats['comparisons']},"
            f" swaps={stats['swaps']}"
        )

    hardestList = max(sortStats, key=lambda name: sortStats[name]["swaps"])

    print("\n=== Reflection Answers ===")
    print(
        "1) Which list took the most work to sort?",
        f"{hardestList} took the most work because it had",
        f"the most out-of-order values (swaps={sortStats[hardestList]['swaps']}).",
    )
    print(
        "2) Why was sortedList fastest?",
        "It was already in order, so bubble sort made no swaps and stopped early.",
    )
    print(
        "3) What does linear search do when value is missing?",
        "It checks each item and returns -1 when the target is not found.",
    )


if __name__ == "__main__":
    main()
