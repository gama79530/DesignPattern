package TemplateMethodPattern.java_.Solution;

public class DFS_Solution extends Solution{

    @Override
    protected TreeNode invert(TreeNode root) {
        TreeNode temp;

        if(root != null){
            temp = invert(root.leftChild);
            root.leftChild = invert(root.rightChild);
            root.rightChild = temp;
        }

        return root;
    }
    
}
