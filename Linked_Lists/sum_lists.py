#
# You have 2 numbers represented by a linked list, where each node contains a
# single digit. The digits are stored in reverse order, such that the 1's
# digit is at the head of the list. Write a function that adds the 2 numbers
# and returns the sum as a linked list.
#
# EX:
# Input:  (7->1->6) + (5->9->2). That is, 617 + 295.
# Output: (2->1->9). That is, 912.
#
# Now suppose the digits are stored in forward order. Repeat the above problem
#
# EX:
# Input:  (6->1->7) + (2->9->5). That is, 617 + 295.
# Output: (9->1->2). That is, 912.
#
import pytest
from linked_list import array_to_linked
from linked_list import linked_list_node


def sum_reversed(l1, l2):
    sum = linked_list_node()
    carry = 0

    while l1 is not None or l2 is not None or carry != 0:

        print "L1   : " + str(l1)
        print "L2   : " + str(l2)
        print "carry: " + str(carry)
        print "sum  : " + str(sum)

        val = 0
        val += l1.value if l1 is not None else 0
        val += l2.value if l2 is not None else 0
        val = (val + carry) % 10

        carry += l1.value if l1 is not None else 0
        carry += l2.value if l2 is not None else 0
        carry /= 10

        sum.append(val)

        if l1 is not None:
            l1 = l1.next_node

        if l2 is not None:
            l2 = l2.next_node

    sum.pop_head()
    return sum


@pytest.mark.parametrize("arr1, arr2, expected", [
    ([7, 1, 6], [5, 9, 2], '2->1->9'),
    ([1, 1, 1, 1, 1], [2, 2, 3], '3->3->4->1->1'),
    ([2, 2, 3], [1, 1, 1, 1, 1], '3->3->4->1->1'),
    ([1], [2], '3'),
    ([7], [6], '3->1'),
    ([9, 9, 9, 9], [1], '0->0->0->0->1')
])
def test_reversed(arr1, arr2, expected):
    LL1 = array_to_linked(arr1)
    LL2 = array_to_linked(arr2)
    LL_sum = sum_reversed(LL1, LL2)

    assert str(LL_sum) == expected
