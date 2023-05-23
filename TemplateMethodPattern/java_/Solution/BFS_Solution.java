package TemplateMethodPattern.java_.Solution;

import java.util.*;

public class BFS_Solution extends Solution{

    @Override
    protected TreeNode invert(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        TreeNode temp;

        while(!queue.isEmpty()){
            if(queue.peek().leftChild != null){
                queue.add(queue.peek().leftChild);
            }
            if(queue.peek().rightChild != null){
                queue.add(queue.peek().rightChild);
            }
            temp = queue.peek().leftChild;
            queue.peek().leftChild = queue.peek().rightChild;
            queue.peek().rightChild = temp;
            queue.remove();
        }

        return root;
    }
}
