import src.da.datastructure.tree as dtree


def get_depth_and_width(root: dtree.TreeNode):
    """Ask for the depth and width of a tree.

    width: maximum number of nodes per tier
    """
    def _depth_first_traversal(root, d, node_nums: dict):
        if root:
            node_nums.setdefault(d, 0)
            node_nums[d] += 1
            _depth_first_traversal(root.left, d + 1, node_nums)
            _depth_first_traversal(root.right, d + 1, node_nums)

    node_nums = {}
    _depth_first_traversal(root, 0, node_nums)

    print(node_nums)
    return len(node_nums), max(node_nums.values())


if __name__ == "__main__":
    get_depth_and_width(None)
