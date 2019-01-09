#
# Write code to partition a linked list around a value x, such that all nodes
# less than x come before all nodes greater than or equal to x. If x is
# contained within the list, the values of x only need to be right after the
# elements less than x. The partition element x can appear anywhere in the
# 'right partition'; it does not need to appear between the left and right
# partitions
#
# EX:
# x     : 5
# Input : 3->5->8->5->10->2->1
# Output: 3->1->2->10->5->5->8
#
import pytest
from linked_list import array_to_linked
from linked_list import linked_list_node


# Definitely not as optimal as partitioning the linked list in place but
# easier to keep track of
def party(node, x):
    smaller = linked_list_node()
    bigger = linked_list_node()

    while node is not None:
        if node.value < x:
            smaller.append(linked_list_node(node.value))
        else:
            bigger.append(linked_list_node(node.value))
        node = node.next_node

    # I know. I'm lazy today. Gimme a break.
    smaller.pop_head()
    bigger.pop_head()

    print "Smaller: " + str(smaller)
    print "Bigger : " + str(bigger)

    current = smaller
    while current.next_node is not None:
        current = current.next_node
    current.next_node = bigger

    return smaller


@pytest.mark.parametrize("arr, x, expected", [
    ([3, 5, 8, 5, 10, 2, 1], 5, '3->2->1->5->8->5->10')
])
def test_party(arr, x, expected):
    LL = array_to_linked(arr)
    result = party(LL, x)
    assert str(result) == expected
