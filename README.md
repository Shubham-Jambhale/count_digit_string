# count_digit_string

# Question
Lydia being a professor would like to explain students a concept of sequence of digit strings,
given integer n, return the nth term of the count digit sequence, Let’s help students in implementing a recursion approach for the given problem. For example, the given digit string "3322251"can be interpreted as two 3’s, three 2’s, one 5 and one 1, In numerical string form this can
be written “23321511”, Now for any given integer n, return the nth term of count_digit_string sequence. (Constraints: 1<= n<= 30) 

# Example 1:

Input n = 1

Output: “1”

This is the Base case

# Example 2:

Input n= 4

Output: “1211”

Explanation:

count_digit_string(1) = “1”

count_digit_string(2) = Number of “1” = one 1 = “11”

count_digit_string(3) = Number of “11” = two 1’s = 21

count_digit_string(4) = Number of “21” = one 2 and one 1 = “1211”


