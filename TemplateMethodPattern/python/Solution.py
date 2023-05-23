import abc
from typing import *

class TreeNode:
    def __init__(self, val:Optional[int]=0, leftChild:'TreeNode'=None, rightChild:'TreeNode'=None) -> None:
        self.val = val
        self.leftChild = leftChild
        self.rightChild = rightChild


class Solution(metaclass=abc.ABCMeta):
    def solve(self, input:List[int]) -> List[Union[int, None]]:
        if not input:
            return input
        
        root = self.listToTree(input, 0)
        root = self.invert(root)
        output = list()
        self.treeToList(output, root, 0)

        return output

        
    def listToTree(self, input:List[Union[int, None]], index:int) -> TreeNode:
        root = None
        if input[index] is not None:
            root = TreeNode(input[index])
            if 2 * index + 2 < len(input):
                root.rightChild = self.listToTree(input, 2 * index + 2)

            if 2 * index + 1 < len(input):
                root.leftChild = self.listToTree(input, 2 * index + 1)

        return root
    
    @abc.abstractmethod
    def invert(self, root:TreeNode):
        return NotImplemented
    
    def treeToList(self, output:list[Union[int, None]], root:TreeNode, index:int):
        if root is not None:
            while index >= len(output):
                output.append(None)

            output[index] = root.val
            self.treeToList(output, root.leftChild, 2*index+1)
            self.treeToList(output, root.rightChild, 2*index+2)


class BFS_Solution(Solution):
    def invert(self, root: TreeNode):
        queue:list[TreeNode] = list()
        queue.append(root)
        
        while queue:
            if queue[0].leftChild is not None:
                queue.append(queue[0].leftChild)

            if queue[0].rightChild is not None:
                queue.append(queue[0].rightChild)

            temp = queue[0].leftChild
            queue[0].leftChild = queue[0].rightChild
            queue[0].rightChild = temp
            queue.pop(0)

        return root
    

class DFS_Solution(Solution):
    def invert(self, root: TreeNode):
        if root is not None:
            temp = self.invert(root.leftChild)
            root.leftChild = self.invert(root.rightChild)
            root.rightChild = temp

        return root

