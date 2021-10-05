# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        maps = {}

        for i in range(len(voyage)):
            maps[voyage[i]] = i

        res = []

        def helper(node, left, right):
            if node is None or left > right or left >= len(voyage):
                res.append(-1)
                return

            if left == right:
                if node.val == voyage[left]:
                    return
                else:
                    res.append(-1)
                    return

            if voyage[left] == node.val:
                if node.left and node.right:
                    if node.left.val in maps and node.right.val in maps and left + 1 < len(voyage):
                        if node.left.val == voyage[left + 1]:
                            helper(node.left, left + 1, maps[node.right.val] - 1)
                            helper(node.right, maps[node.right.val], right)
                        elif node.right.val == voyage[left + 1]:
                            res.append(node.val)
                            helper(node.right, left + 1, maps[node.left.val] - 1)
                            helper(node.left, maps[node.left.val], right)
                        else:
                            res.append(-1)
                            return
                    else:
                        res.append(-1)
                        return

                elif node.left:
                    if node.left.val == voyage[left + 1]:
                        helper(node.left, left + 1, right)
                    else:
                        res.append(-1)
                        return
                elif node.right:
                    if node.right.val == voyage[left + 1]:
                        helper(node.right, left + 1, right)
                    else:
                        res.append(-1)
                        return

                else:
                    res.append(-1)
                    return
            else:
                res.append(-1)
                return

        helper(root, 0, len(voyage) - 1)
        for i in res:
            if i == -1:
                res = [-1]
                break

        return res





