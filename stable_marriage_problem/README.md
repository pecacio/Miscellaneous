# Stable Marriage Problem
https://en.wikipedia.org/wiki/Stable_marriage_problem \
It is the problem of finding a stable matchong between two equally sized sets of elements given an ordering of preferences of each element.\
A matching is a bijection from elements from one set to the elements of the other.\
\
A matching is not stable if:
1. There is an element A of the first matched set whuch prefers some element B of the second matched set over the element already matched to A.
2. B also prefers the element A over the element already matched to B\
In other words a matching is stable when there does not exist any match (A,B) whch both prefer each other over their current partners.\
\
\
Example:\
m1,m2,m3,m4 be the males and w1,w2,w3,w4 be the females.\
\
![example](https://github.com/pecacio/Miscellaneous/blob/main/stable_marriage_problem/Stable_marriage_example.png)

The first table contains the preferences of the males (i.e., choices of m1,m2m,m3,m4 in the corresponding rows).\
The second table contains the preferences of the females (i.e., choices of w1,w2,w3,w4 in the corresponding rows).\
\
A stable matching solution is :\
m1-->w3\
m2-->w1\
m2-->w2\
m3-->w4\
(here the choices of the men are given priority)\
\
There can be many solutions to such problems:\
\n(When the choices of women are given priority)\
w1-->m2\
w2-->m3\
w3-->m1\
w4-->m4
