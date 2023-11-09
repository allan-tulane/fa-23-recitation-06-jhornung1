# CMPS 2200 Recitation 06
## Answers

**Name:** Jacob Hornung


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**

The recurrence relation would be W(n) = W(n-1) + W(n-2) + 1. This is because the recurrnce is divided like that after every recursive call. Solving the recurrence we get W(n) = O(n^2).

- **3)**

The recurrence relation for span would be S(n) = S(n-1) + 1, as each split of the recurrence function can be solved in parallel. Solving this recurrence relation, we get S(n) = O(n).

- **4)**

Obviously, the pattern is generally a decrease in numbers. The second number in the list is always the largest number. And finally, the most interesting, it never changes, it just gets longer. Like the sequence of a small value for a small value of n, is what ends the list of larger values of n.

- **6

The max number of times that fib_top_down can be called is two times, as the recursive call only splits twice. Because of this, we know that fib_top_down has work of W(n) = O(n) and span is equal to S(n) = O(n) as well.

- **8)**

The value of $F_i$ is only read once, because the algorithm reads through iterative. This then means that work is equal to O(n) and span is equal ot O(1).