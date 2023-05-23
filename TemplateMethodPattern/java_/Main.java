package TemplateMethodPattern.java_;

import java.util.*;
import TemplateMethodPattern.java_.Solution.*;

class Main{
    public static void main(String[] args) {
        List<Integer> input = null;
        Solution solution = null;
        List<Integer> output = null;
        
        input = Arrays.asList(2, 1, 3);
        System.out.print("Input: ");
        System.out.println(input);
        
        solution = new BFS_Solution();
        output = solution.solve(input);
        System.out.print("BFS solution: ");
        System.out.println(output);

        solution = new DFS_Solution();
        output = solution.solve(input);
        System.out.print("DFS solution: ");
        System.out.println(output);

        input = Arrays.asList(4, 2, 7, 1, 3, 6, 9);
        System.out.print("Input: ");
        System.out.println(input);
        
        solution = new BFS_Solution();
        output = solution.solve(input);
        System.out.print("BFS solution: ");
        System.out.println(output);

        solution = new DFS_Solution();
        output = solution.solve(input);
        System.out.print("DFS solution: ");
        System.out.println(output);
    }
}