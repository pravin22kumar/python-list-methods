"""Basic examples of common Python list operations."""


def demonstrate_list_methods():
    """Print examples of basic list operations."""
    items = ["apple", "banana", "cherry"]

    print("Starting list:", items)

    items.append("date")
    print("Append():", items)

    items.insert(1, "blueberry")
    print("Insert():", items)

    items.remove("banana")
    print("Remove():", items)

    removed_item = items.pop()
    print("Pop():", items, "removed", removed_item)

    print("Index():", items.index("apple"))
    print("Count():", items.count("apple"))

    copied_items = items.copy()
    print("Copy():", copied_items)

    items.sort()
    print("Sort():", items)

    items.reverse()
    print("Reverse():", items)

    second_list = ["elderberry", "fig"]
    items.extend(second_list)
    print("Extend():", items)

    items.clear()
    print("Clear():", items)


if __name__ == "__main__":
    demonstrate_list_methods()
