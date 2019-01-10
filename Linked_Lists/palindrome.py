#
# Implement a function to check if a linked list is a palindrome.
#
import pytest
from linked_list import array_to_linked
from linked_list import linked_list_node


def pally_checker(ll):
    runner = ll
    current = ll
    ref = []

    while runner is not None and runner.next_node is not None:
        ref.append(current.value)
        current = current.next_node
        runner = runner.next_node.next_node

    # If runner does not end as None, then the linked list has odd elements
    # We can skip the middle value
    if runner is not None:
        current = current.next_node

    while current is not None:
        val = ref.pop()
        if val != current.value:
            return False
        current = current.next_node

    return True


@pytest.mark.parametrize("arr, expected", [
    ([1, 2, 1, 2, 1], True),
    ([1, 1, 1, 1], True),
    ([1], True),
    ([1, 3, 3, 1], True),
    ([1, 1, 2], False),
    ([1, 2], False),
    ([5, 1, 5, 5], False)
])
def test_palindrome_checker(arr, expected):
    LL = array_to_linked(arr)
    assert pally_checker(LL) == expected
