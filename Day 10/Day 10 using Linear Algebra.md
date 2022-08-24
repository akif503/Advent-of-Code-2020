# Day 10 using Linear Algebra

An **Adjacency matrix** is a *square* matrix where each element $A_{ij}$ represents if there is a direct edge between the vertices $i$ and $j$. 
And the each element exponent of the matrix: $A^n_{ij}$ represents the number of  paths of length $n$ from $i$ to $j$. So, adding all the path lengths from $0$ to $n$ from $i$ to $j$ will give use the total number of paths from $i$ to $j$. So, an element of matrix $M$ will represent the total number of paths from $i$ to $j$, such that - 
$$
M = I + A + A^2 + A^3 + \dots
$$
 However, we don't know the value of maximum $n$. However, if we take $n$ to be infinite (can we?) we can rearrange the above equation, by taking $A$ common from the terms containing an $A$, which will produce the same series in the right side, so we can replace that series with $M$, then we can write -
$$
M = I + AM
$$
From there we can further reduce it to - 
$$
M = (I - A)^{-1}
$$
Thus, we can now calculate $M$ directly using this formula.

**Notes**: If we take $n$ to be the number of vertices, we can calculate the sum. It takes $O(n^3)$ time to produce matrix $A^{i+1}$ from $A^i$ and there would be $n$ terms. So, the total complexity of the process will be $n \times O(n^3) = O(n^4)$ time. However, the solution using the above inverse equation requires $O(n^3)$ time (as it is the time required to calculate and inverse).  

Although, using *one dimensional look-back 3 recurrence* the time complexity is $O(n)$. 

However, in a more general case, where there isn't the *Tribonacci structure* present in the graph like our problem. This is a much better method to calculate the number of paths between 2 vertices. Because the best DP solution using the *Held-Karp* algorithm would solve this problem in $O(n^2*2^n)$ time, which is worse than $O(n^3)$. 

**Questions**:

1. Will $i$ > $n$ make $A^n = 0$ because there is no such vector, or will it wrap around and calculate edges multiple times?) 