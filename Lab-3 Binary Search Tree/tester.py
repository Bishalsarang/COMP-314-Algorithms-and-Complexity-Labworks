import unittest
from bst import Node, BST

class BinarySearchTestcase(unittest.TestCase):
        def test_BST(self):
                bt = BST()
                l = [(5, "e"),
                     (2, "b"),
                     (18, "e"),
                     (-4, "f"),
                     (3, "f"),
                     (21, "g"),
                     (19, "h"),
                     (25, "k"),

                     ]
                # Insert key, value in BST Node
                for key, value in l:
                        bt.insert(key, value)
                # Assert for size,largest_Key, smallest_key, inorder path, postorderpath and preorder path
                self.assertEqual(bt.size, 8)
                self.assertEqual(bt.largest_key(), 25)
                self.assertEqual(bt.smallest_key(), -4)
                self.assertListEqual(bt.inorder(), sorted(l))
                self.assertListEqual(bt.preorder(), [(5, 'e'), (2, 'b'), (-4, 'f'), (3, 'f'), (18, 'e'), (21, 'g'), (19, 'h'), (25, 'k')])
                self.assertListEqual(bt.postorder(),[(-4, 'f'), (3, 'f'), (2, 'b'), (19, 'h'), (25, 'k'), (21, 'g'), (18, 'e'), (5, 'e')])

                # Delete a node and assert for size and inorder path
                bt.deletenode(2)
                self.assertEqual(bt.size, 7)
                del l[1]
                self.assertListEqual(bt.inorder(), sorted(l))
                     
if __name__ == "__main__":
        unittest.main()
