#ifndef SOLUTION_HEADER_INCLUDED
#define SOLUTION_HEADER_INCLUDED

#include <memory>
#include <vector>
#include <string>

using namespace std;

typedef struct TreeNode{
    int val = 0;
    shared_ptr<TreeNode> leftChild;
    shared_ptr<TreeNode> rightChild;

    TreeNode() = default;
    TreeNode(int val);
    TreeNode(int val, shared_ptr<TreeNode> &leftChild, shared_ptr<TreeNode> &rightChild);
    TreeNode(int val, shared_ptr<TreeNode> &&leftChild, shared_ptr<TreeNode> &&rightChild);
} TreeNode;

class Solution{
public:
    shared_ptr<vector<shared_ptr<int>>> solve(shared_ptr<vector<shared_ptr<int>>> input);

protected:
    shared_ptr<TreeNode> listToTree(shared_ptr<vector<shared_ptr<int>>> input, int index);
    virtual shared_ptr<TreeNode> invert(shared_ptr<TreeNode> root) = 0;
    void treeToList(shared_ptr<vector<shared_ptr<int>>> output, shared_ptr<TreeNode> root, int index);
};

class BFS_Solution: public Solution{
protected:
    shared_ptr<TreeNode> invert(shared_ptr<TreeNode> root);
};

class DFS_Solution: public Solution{
    shared_ptr<TreeNode> invert(shared_ptr<TreeNode> root);
} ;

string to_string(shared_ptr<vector<shared_ptr<int>>> treeArray);

#endif