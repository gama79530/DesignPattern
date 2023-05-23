package TemplateMethodPattern.java_.Solution;

import java.util.*;

public abstract class Solution {
    public List<Integer> solve(List<Integer> input){
        if(input.isEmpty())
            return new ArrayList<>();

        TreeNode root = listToTree(input, 0);
        root = invert(root);
        List<Integer> output = new ArrayList<>();
        treeToList(output, root, 0);

        return output;
    }
    
    protected TreeNode listToTree(List<Integer> input, int index){
        TreeNode root = null;
        if(input.get(index) != null){
            root = new TreeNode(input.get(index));
            if(2 * index + 2 < input.size()){
                root.rightChild = listToTree(input, 2*index+2);
            }
            
            if(2 * index + 1 < input.size()){
                root.leftChild = listToTree(input, 2*index+1);
            }
        }

        return root;
    }

    protected abstract TreeNode invert(TreeNode root);

    protected void treeToList(List<Integer> output, TreeNode root, int index){
        if(root != null){
            while(index >= output.size()){
                output.add(null);
            }
            output.set(index, root.val);
            treeToList(output, root.leftChild, 2*index+1);
            treeToList(output, root.rightChild, 2*index+2);
        }
    }
}
