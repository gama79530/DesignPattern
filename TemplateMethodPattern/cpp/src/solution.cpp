#include <queue>
#include "header/solution.h"

TreeNode::TreeNode(int val){
    this->val = val;
}

TreeNode::TreeNode(int val, shared_ptr<TreeNode> &leftChild, shared_ptr<TreeNode> &rightChild){
    this->val = val;
    this->leftChild = leftChild;
    this->rightChild = rightChild;
}

TreeNode::TreeNode(int val, shared_ptr<TreeNode> &&leftChild, shared_ptr<TreeNode> &&rightChild){
    this->val = val;
    this->leftChild = leftChild;
    this->rightChild = rightChild;
}

shared_ptr<vector<shared_ptr<int>>> Solution::solve(shared_ptr<vector<shared_ptr<int>>> input){
    if(input->empty())
        return make_shared<vector<shared_ptr<int>>>();

    shared_ptr<TreeNode> root = listToTree(input, 0);
    root = invert(root);
    shared_ptr<vector<shared_ptr<int>>> output = make_shared<vector<shared_ptr<int>>>();
    treeToList(output, root, 0);

    return output;
}

shared_ptr<TreeNode> Solution::listToTree(shared_ptr<vector<shared_ptr<int>>> input, int index){
    shared_ptr<TreeNode> root;
    if((*input)[index] != nullptr){
        root = make_shared<TreeNode>(*((*input)[index]));
        if(2 * index + 2 < input->size()){
            root->rightChild = listToTree(input, 2*index+2);
        }
        if(2 * index + 1 < input->size()){
            root->leftChild = listToTree(input, 2*index+1);
        }
    }
    return root;
}

void Solution::treeToList(shared_ptr<vector<shared_ptr<int>>> output, shared_ptr<TreeNode> root, int index){
    if(root != nullptr){
        while(index >= output->size()){
            output->push_back(shared_ptr<int>());
        }
        (*output)[index] = make_shared<int>(root->val);
        treeToList(output, root->leftChild, 2*index+1);
        treeToList(output, root->rightChild, 2*index+2);
    }
}

shared_ptr<TreeNode> BFS_Solution::invert(shared_ptr<TreeNode> root){
    queue<shared_ptr<TreeNode>> q;
    q.push(root);
    shared_ptr<TreeNode> temp;

    while(!q.empty()){
        if(q.front()->leftChild != nullptr){
            q.push(q.front()->leftChild);
        }
        if(q.front()->rightChild != nullptr){
            q.push(q.front()->rightChild);
        }
        temp = q.front()->leftChild;
        q.front()->leftChild = q.front()->rightChild;
        q.front()->rightChild = temp;
        q.pop();
    }

    return root;
}

shared_ptr<TreeNode> DFS_Solution::invert(shared_ptr<TreeNode> root){
    shared_ptr<TreeNode> temp;
    if(root != nullptr){
        temp = invert(root->leftChild);
        root->leftChild = invert(root->rightChild);
        root->rightChild = temp;
    }

    return root;
}

string to_string(shared_ptr<vector<shared_ptr<int>>> treeArray){
    string output = "[";
    for(auto it=treeArray->begin(); it != treeArray->end(); it++){
        output += ((*it == nullptr ? "null" : to_string(**it)) + ", ");
    }
    output.pop_back();
    output.pop_back();
    output += "]";
    return output;
}
