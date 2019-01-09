#
# Write code to remove duplicates from an unsorted linked list.
# How would you solve this problem if a temporary buffer is not allowed?
#
import pytest
from linked_list import array_to_linked
from linked_list import linked_list_node


# With a buffer/reference
def remove_dups(node):
    ref = set()
    prev = linked_list_node()
    current = node
    while(current is not None):
        if current.value in ref:
            prev.next_node = current.next_node
        else:
            ref.add(current.value)
            prev = current
        current = current.next_node

    return node


def remove_dups_no_buf(node):
    current = node
    head = current

    while current is not None:
        runner = current
        while runner.next_node is not None:
            if runner.next_node.value == current.value:
                runner.next_node = runner.next_node.next_node
            else:
                runner = runner.next_node
        current = current.next_node

    return head


@pytest.mark.parametrize("arr, expected, func", [
    ([1, 2, 3, 4, 5], '1->2->3->4->5', remove_dups),
    ([1, 1, 1, 1, 1], '1', remove_dups),
    ([1, 2, 1, 2, 1], '1->2', remove_dups),
    ([1, 2, 3, 4, 5, 6, 6], '1->2->3->4->5->6', remove_dups),
    ([1, 1, 1, 2, 3, 4, 5], '1->2->3->4->5', remove_dups),
    ([1, 2, 3, 4, 5], '1->2->3->4->5', remove_dups_no_buf),
    ([1, 1, 1, 1, 1], '1', remove_dups_no_buf),
    ([1, 2, 1, 2, 1], '1->2', remove_dups_no_buf),
    ([1, 2, 3, 4, 5, 6, 6], '1->2->3->4->5->6', remove_dups_no_buf),
    ([1, 1, 1, 2, 3, 4, 5], '1->2->3->4->5', remove_dups_no_buf)
])
def test_remove_dups(arr, expected, func):
    LL = array_to_linked(arr)
    LL.set(func(LL))
    assert str(LL) == expected
