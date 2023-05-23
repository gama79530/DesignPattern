package TemplateMethodPattern.java_.Solution;

public class TreeNode {
    int val;
    public TreeNode leftChild;
    public TreeNode rightChild;

    public TreeNode(){
        val = 0;
        leftChild = null;
        rightChild = null;
    }

    public TreeNode(int val){
        this.val = val;
        leftChild = null;
        rightChild = null;
    }

    public TreeNode(int val, TreeNode leftChild, TreeNode rightChild){
        this.val = val;
        this.leftChild = leftChild;
        this.rightChild = rightChild;
    }
}
