# [Delete Nodes with Greater on Right](https://www.geeksforgeeks.org/problems/delete-nodes-having-greater-value-on-right/1)
## Easy
Given a singly linked list, remove all nodes that have a node with a greater value anywhere to their right in the list. Return the head of the modified linked list.
Examples:
Input: LinkedList = 12-&gt;15-&gt;10-&gt;11-&gt;5-&gt;6-&gt;2-&gt;3
Output: 15-&gt;11-&gt;6-&gt;3
Explanation: Since, 12, 10, 5 and 2 are the elements which have greater elements on the following nodes. So, after deleting them, the linked list would like be 15, 11, 6, 3.

Input: LinkedList = 10-&gt;20-&gt;30-&gt;40-&gt;50-&gt;60
Output: 60Explanation: All the nodes except the last node has a greater value node on its right, so all the nodes except the last node must be removed.
Constraints:1 ≤ size of linked list ≤ 1061 ≤ element of linked list ≤ 106Note: Try to solve the problem without using any extra space.