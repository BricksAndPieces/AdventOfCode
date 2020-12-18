"""
--- Day 18: Operation Order ---
As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you are interrupted
by the child sitting next to you. They're curious if you could help them with their math homework.

Unfortunately, it seems like this "math" follows different rules than you remember.

The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (*),
and parentheses ((...)). Just like normal math, parentheses indicate that the expression inside must be evaluated before
it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the operator,
and multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition, the
operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
      9   + 4 * 5 + 6
         13   * 5 + 6
             65   + 6
                 71
Parentheses can override this order; for example, here is what happens if parentheses are added to form 1 + (2 * 3) +
(4 * (5 + 6)):

1 + (2 * 3) + (4 * (5 + 6))
1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     7      +     44
            51
Here are a few more examples:

2 * 3 + (4 * 5) becomes 26.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.
Before you can help with the homework, you need to understand it yourself. Evaluate the expression on each line of the
homework; what is the sum of the resulting values?

--- Part Two ---
You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the
next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with.
Instead, addition is evaluated before multiplication.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
  3   *   7   * 5 + 6
  3   *   7   *  11
     21       *  11
         231
Here are the other examples from above:

1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
2 * 3 + (4 * 5) becomes 46.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.
What do you get if you add up the results of evaluating the homework problems using these new rules?
"""

import re
from aoc import *


def solve_equation(eq: str, part1):
    if eq.isdigit():
        return int(eq)

    if '(' in eq:
        start = eq.rindex('(')
        end = eq[start:].index(')') + start
        new_eq = eq[:start] + str(solve_equation(eq[start + 1:end], part1)) + eq[end + 1:]
        return solve_equation(new_eq, part1)

    nums = re.findall(r'\d+', eq)
    if part1:
        add = '*' not in eq or ('*' in eq and '+' in eq and eq.index('+') < eq.index('*'))
        result = int(nums[0]) + int(nums[1]) if add else int(nums[0]) * int(nums[1])
        return solve_equation(f'{result}{eq[(len(nums[0]) + len(nums[1]) + 1):]}', part1)
    else:
        op = '+' if '+' in eq else '*'
        index = eq.index(op)
        c = eq[:index].count('*' if op == '+' else '+')
        result = int(nums[c]) + int(nums[c + 1]) if op == '+' else int(nums[c]) * int(nums[c + 1])
        return solve_equation(f'{eq[:index - len(nums[c])]}{result}{eq[index + len(nums[c + 1]) + 1:]}', part1)


inputs = puzzle_input(18, 2020, sample=False).replace(' ', '').split('\n')
results = [solve_equation(eq, True) for eq in inputs]
print(f'Part 1: {sum(results)}')

results = [solve_equation(eq, False) for eq in inputs]
print(f'Part 2: {sum(results)}')
