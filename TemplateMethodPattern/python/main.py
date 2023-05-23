from Solution import *

if __name__ == '__main__':
    input = [2, 1, 3]
    print(f'Input: {input}')

    solution = BFS_Solution()
    output = solution.solve(input)
    print(f'BFS solution: {output}')
    
    solution = DFS_Solution()
    output = solution.solve(input)
    print(f'DFS solution: {output}')
    
    input = [4, 2, 7, 1, 3, 6, 9]
    print(f'Input: {input}')
    
    solution = BFS_Solution()
    output = solution.solve(input)
    print(f'BFS solution: {output}')
    
    solution = DFS_Solution()
    output = solution.solve(input)
    print(f'DFS solution: {output}')
    