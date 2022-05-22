from LinkedList import LinkedList


def main():
    my_linked_list = LinkedList()
    list_a = [1, 2, 5, 6]
    for element in list_a:
        my_linked_list.add(element)
    print(f"Original list: {my_linked_list}")

    my_linked_list.addFirst(3)
    print(f"addFirst: {my_linked_list}")

    my_linked_list.addLast(10)
    print(f"addLast: {my_linked_list}")

    my_linked_list.add(12)
    print(f"add: {my_linked_list}")

    my_linked_list.insert(2, "inserted")
    print(f"insert: {my_linked_list}")

    my_linked_list.removeFirst()
    print(f"removeFirst: {my_linked_list}")

    my_linked_list.removeLast()
    print(f"removeLast: {my_linked_list}")

    my_linked_list.removeAt(1)
    print(f"removeAt: {my_linked_list}")

    my_linked_list.contains(6)

    # fikk ikke til
    # my_linked_list, remove(5)
    # print(f"remove: {my_linked_list}")

    get = my_linked_list.get(3)
    print(f"Element at index 3: {get}")

    index = my_linked_list.indexOf(10)
    print(f"Index of 10 is: {index}")

    last_index = my_linked_list.lastIndexOf(6)
    print(f"Last index of 6 is: {last_index}")

    my_linked_list.set(2, "Replaced element!")
    print(f"Set: {my_linked_list}")

    my_linked_list.clear()


main()
