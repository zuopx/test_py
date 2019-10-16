import unittest

import src.da.problem.tree as ptree
import src.da.datastructure.tree as dtree


class TestTree(unittest.TestCase):

    def setUp(self):
        tree = [dtree.TreeNode(i) for i in range(10)]
        tree[0].left = tree[1]
        tree[1].right = tree[2]
        tree[2].left = tree[3]
        tree[2].right = tree[4]
        tree[4].left = tree[8]
        tree[4].right = tree[5]
        tree[5].left = tree[6]
        tree[5].right = tree[7]
        tree[8].left = tree[9]
        self.tree = tree

    def test_get_depth_and_width(self):
        depth, width = ptree.get_depth_and_width(self.tree[0])
        self.assertEqual(depth, 6)
        self.assertEqual(width, 3)

if __name__ == "__main__":
    unittest.main()
