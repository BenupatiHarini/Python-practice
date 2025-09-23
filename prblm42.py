# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add values + carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            # Move forward
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next


# -------- Example Run --------
def printList(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example input: l1 = [2,4,3], l2 = [5,6,4]
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

sol = Solution()
output = sol.addTwoNumbers(l1, l2)
print("Output:", printList(output))  # Output: [7, 0, 8]
