#include <iostream>
#include "src/header/solution.h"

int main(){

    shared_ptr<vector<shared_ptr<int>>> input;
    shared_ptr<Solution> solution;
    shared_ptr<vector<shared_ptr<int>>> output;

    input = make_shared<vector<shared_ptr<int>>>();
    input->push_back(make_shared<int>(2));
    input->push_back(make_shared<int>(1));
    input->push_back(make_shared<int>(3));
    cout << "Input: " << to_string(input) << endl;

    solution = make_shared<BFS_Solution>();
    output = solution->solve(input);
    cout << "BFS solution: " << to_string(output) << endl;

    solution = make_shared<DFS_Solution>();
    output = solution->solve(input);
    cout << "DFS solution: " << to_string(output) << endl;

    input = make_shared<vector<shared_ptr<int>>>();
    input->push_back(make_shared<int>(4));
    input->push_back(make_shared<int>(2));
    input->push_back(make_shared<int>(7));
    input->push_back(make_shared<int>(1));
    input->push_back(make_shared<int>(3));
    input->push_back(make_shared<int>(6));
    input->push_back(make_shared<int>(9));
    cout << "Input: " << to_string(input) << endl;

    solution = make_shared<BFS_Solution>();
    output = solution->solve(input);
    cout << "BFS solution: " << to_string(output) << endl;

    solution = make_shared<DFS_Solution>();
    output = solution->solve(input);
    cout << "DFS solution: " << to_string(output) << endl;

    return 0;
}