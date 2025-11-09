import unittest

from solucao import Nodo, Action


class TestNodo(unittest.TestCase):
    def test_childs_are_correctly_created(self):
        root = Nodo(estado="1234_5678", pai=None, acao=None, custo=0)
        children = root.filhos()

        expected_up_child = Nodo(
            estado="1_3425678", pai=root, acao=Action.UP.value, custo=1
        )
        expected_down_child = Nodo(
            estado="1234756_8", pai=root, acao=Action.DOWN.value, custo=1
        )
        expected_left_child = Nodo(
            estado="123_45678", pai=root, acao=Action.LEFT.value, custo=1
        )
        expected_right_child = Nodo(
            estado="12345_678", pai=root, acao=Action.RIGHT.value, custo=1
        )

        expected_children = {
            expected_up_child,
            expected_down_child,
            expected_left_child,
            expected_right_child,
        }

        self.assertSetEqual(expected_children, children)

    def test_correctly_compare_parents(self):
        root = Nodo(estado="1234_5678", pai=None, acao=None, custo=0)
        self.assertTrue(all(root is c.pai for c in root.filhos()))

    def test_parent_of_children_nodes(self):
        root = Nodo(estado="1234_5678", pai=None, acao=None, custo=0)
        up_child = Nodo(estado="1_3425678", pai=root, acao=Action.UP.value, custo=1)

        self.assertTrue(all(up_child is c.pai for c in up_child.filhos()))

    def test_hash_for_same_object_is_equal(self):
        root = Nodo(estado="1234_5678", pai=None, acao=None, custo=0)
        up_child = Nodo(estado="1_3425678", pai=root, acao=Action.UP.value, custo=1)

        self.assertEqual(hash(root), hash(up_child.pai))

    def test_hash_for_different_object_is_different(self):
        root = Nodo(estado="1234_5678", pai=None, acao=None, custo=0)
        up_child = Nodo(estado="1_3425678", pai=root, acao=Action.UP.value, custo=1)

        self.assertNotEqual(hash(root), hash(up_child))

    def test_hash_for_children_nodes(self):
        root = Nodo(estado="1234_5678", pai=None, acao=None, custo=0)
        up_child = Nodo(estado="1_3425678", pai=root, acao=Action.UP.value, custo=1)
        down_child = Nodo(estado="1234756_8", pai=root, acao=Action.DOWN.value, custo=1)

        down_child_from_up_child = Nodo(
            estado="1234_5678", pai=up_child, acao=Action.DOWN.value, custo=2
        )
        up_child_from_down_child = Nodo(
            estado="1234_5678", pai=down_child, acao=Action.UP.value, custo=2
        )

        self.assertNotEqual(hash(up_child), hash(down_child_from_up_child))
        self.assertNotEqual(hash(down_child), hash(up_child_from_down_child))
        self.assertNotEqual(
            hash(down_child_from_up_child), hash(up_child_from_down_child)
        )


if __name__ == "__main__":
    unittest.main()
