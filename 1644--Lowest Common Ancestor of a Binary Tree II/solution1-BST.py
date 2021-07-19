# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path1 = find_path(root, p)
        path2 = find_path(root, q)
        return find_LCA(path1, path2)


def build_path(root, p):
    queue = [root]
    path = [[root, root]]
    find = False

    while len(queue) != 0:

        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
            path.append([node, node.left])
            if node.left == p:
                find = True
                break

        if node.right is not None:
            queue.append(node.right)
            path.append([node, node.right])
            if node.right == p:
                find = True
                break

    if find:
        return path
    else:
        return None


def find_path(root, p):
    path = build_path(root, p)

    if path is None:
        return None

    curr = p
    result = [p]

    for i in range(len(path) - 1, -1, -1):
        if path[i][1] == curr:
            result.append(path[i][0])
            curr = path[i][0]

    return result


def find_LCA(path1, path2):
    if path1 is None or path2 is None:
        return None

    if len(path1) > len(path2):
        path1 = path1[len(path1) - len(path2):]
    else:
        path2 = path2[len(path2) - len(path1):]

    for i in range(len(path1)):
        if path1[i] == path2[i]:
            return path1[i]