#
# This file contains the class for a singly linked list
#
import pytest


class linked_list_node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __len__(self):
        if self.value is None and self.next_node is None:
            return 0
        current = self
        num = 1
        while current.next_node is not None:
            current = current.next_node
            num += 1
        return num

    def __str__(self):
        string = ""
        current = self
        while current.next_node is not None:
            print string
            string += str(current.value) + '->'
            current = current.next_node
        string += str(current.value)
        return string

    def append(self, value):
        current = self
        while current.next_node is not None:
            current = current.next_node
        current.next_node = linked_list_node(value)
        return self

    def delete_node(node, value):
        current = node
        if (current.value == value):
            return current.next_node

        while current.next_node is not None:
            if(current.next_node.value == value):
                current.next_node = current.next_node.next_node
                return node
            current = current.next_node
        return node

    def pop_head(self):
        self.value = self.next_node.value
        self.next_node = self.next_node.next_node
        return self

    def pop_tail(self):
        current = self
        while current.next_node.next_node is not None:
            current = current.next_node
        current.next_node = None
        return self

    def set(self, node):
        self.value = node.value
        self.next_node = node.next_node


def array_to_linked(arr):
    if isinstance(arr, list) or isinstance(arr, tuple):
        head = linked_list_node(arr[0])
        current = head
        for i in range(1, len(arr)):
            node = linked_list_node(arr[i])
            current.next_node = node
            current = node
        return head
    print arr + " is not an array or tuple."


class Test_linked_lists:
    empty = linked_list_node()
    node1 = linked_list_node(1)
    node2 = linked_list_node(2)
    node3 = linked_list_node(3)
    node4 = linked_list_node(4)
    node1.next_node = node2
    node2.next_node = node3
    node3.next_node = node4

    @pytest.mark.parametrize("arr, expected", [
        ([1, 2, 3, 4, 5], '1->2->3->4->5'),
        (['m', 'o', 'n', 'k', 'e', 'y'], 'm->o->n->k->e->y'),
        (['foo', 'bar', 'fizz', 'buzz'], 'foo->bar->fizz->buzz')
    ])
    def test_array_init(self, arr, expected):
        node = array_to_linked(arr)
        assert str(node) == expected

    @pytest.mark.parametrize("node, expected", [
        (node1, 4),
        (node2, 3),
        (node3, 2),
        (node4, 1),
        (empty, 0)
    ])
    def test_len(self, node, expected):
        assert len(node) == expected

    @pytest.mark.parametrize("node, value, expected", [
        (node1, 9, '1->2->3->4->9')
    ])
    def test_append(self, node, value, expected):
        node.append(value)
        assert str(node) == expected

    @pytest.mark.parametrize("node, value, expected", [
        (node1, 9, '1->2->3->4'),
        (node1, 3, '1->2->4')
    ])
    def test_del(self, node, value, expected):
        node.delete_node(value)
        assert str(node) == expected

    @pytest.mark.parametrize("arr, expected", [
        ([1, 2, 3, 4, 5], '2->3->4->5'),
        (['m', 'o', 'n', 'k', 'e', 'y'], 'o->n->k->e->y'),
        (['foo', 'bar', 'fizz', 'buzz'], 'bar->fizz->buzz')
    ])
    def test_pop_head(self, arr, expected):
        LL = array_to_linked(arr)
        LL.pop_head()
        assert str(LL) == expected

    @pytest.mark.parametrize("arr, expected", [
        ([1, 2, 3, 4, 5], '1->2->3->4'),
        (['m', 'o', 'n', 'k', 'e', 'y'], 'm->o->n->k->e'),
        (['foo', 'bar', 'fizz', 'buzz'], 'foo->bar->fizz')
    ])
    def test_pop_tail(self, arr, expected):
        LL = array_to_linked(arr)
        LL.pop_tail()
        assert str(LL) == expected
